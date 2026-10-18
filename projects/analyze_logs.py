import csv
from collections import Counter

file_path = "projects/sample-authentication-logs.csv"

total_attempts = 0
successful_logins = 0
failed_logins = 0
failed_users = Counter()
failed_ips = Counter()

# Read the CSV file and skip blank lines
with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(line for line in file if line.strip())

    for row in reader:
        total_attempts += 1
        status = row["status"].strip().upper()

        if status == "SUCCESS":
            successful_logins += 1
        elif status == "FAILED":
            failed_logins += 1
            failed_users[row["username"]] += 1
            failed_ips[row["source_ip"]] += 1

# Display the summary
print("=== Authentication Log Analysis ===")
print(f"Total login attempts: {total_attempts}")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")

# Display failed login counts
print("\n=== Users with Failed Logins ===")
for username, count in failed_users.most_common():
    print(f"{username}: {count} failed attempts")

print("\n=== Source IPs with Failed Logins ===")
for ip, count in failed_ips.most_common():
    print(f"{ip}: {count} failed attempts")

# Generate alerts for repeated failures
print("\n=== Failed Login Security Alerts ===")
threshold = 3
alerts_found = False

for username, count in failed_users.most_common():
    if count >= threshold:
        print(f"ALERT: {username} has {count} failed login attempts.")
        alerts_found = True

if not alerts_found:
    print("No users reached the alert threshold.")


