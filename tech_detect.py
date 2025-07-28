# modules/tech_detect.py

import subprocess

def detect_tech(domain):
    try:
        result = subprocess.check_output(["whatweb", domain], stderr=subprocess.DEVNULL)
        return result.decode().strip()
    except Exception as e:
        return f"[ERROR] Tech detection failed: {e}"
