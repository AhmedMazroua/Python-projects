from collections import defaultdict

LOG_FILE = "suspicious_login/sample_log.txt"

FAILED_LIMIT = 3
SENSITIVE_PATHS = ["/admin", "/login"]
BLACKLIST = ["45.33.32.1"]

failed_attempts = defaultdict(int)

print("\n--- Suspicious Activity Report ---\n")

with open(LOG_FILE, "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        ip = parts[0]
        status = parts[2]
        path = parts[3]

        # Track failed logins
        if status == "FAILED":
            failed_attempts[ip] += 1

        # Blacklisted IP detection
        if ip in BLACKLIST:
            print(f"[BLACKLISTED IP ACCESS] {ip} accessed {path}")

        # Sensitive path access
        if path in SENSITIVE_PATHS and status == "SUCCESS":
            print(f"[SENSITIVE ACCESS] {ip} accessed {path}")

# Check brute force attempts
for ip, count in failed_attempts.items():
    if count >= FAILED_LIMIT:
        print(f"[BRUTE FORCE ALERT] {ip} had {count} failed login attempts")

print("\nScan complete.")