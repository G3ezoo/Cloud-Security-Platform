import yaml
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_rules():
    with open("data/rules.yaml") as f:
        data = yaml.safe_load(f)
    
    if not data or "rules" not in data:
        raise ValueError("rules.yaml is empty or invalid")
    
    return data["rules"]


def load_config():
    with open("data/sample_config.json") as f:
        return json.load(f)


def run_scan():
    rules = load_rules()
    config = load_config()

    findings = []

    for rule in rules:
        key = rule["key"]
        expected = rule["expected"]
        actual = config.get(key)

        if actual != expected:
            findings.append({
                "issue": rule["name"],
                "severity": rule["severity"],
                "framework": rule["framework"],
                "key": key
            })

    return findings