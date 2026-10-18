
import csv
from collections import Counter

# Location of our sample authentication logs
file_path = "projects/sample-authentication-logs.csv"

total_attempts = 0
successful_logins = 0
failed_logins = 0
failed_users = Counter()
failed_ips = Counter()

# Read and analyse the authentication logs
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_attempts += 1

        if row["status"] == "SUCCESS":
            successful_logins += 1

        elif row["status"] == "FAILED":
            failed_logins += 1
            failed_users[row["username"]] += 1
            failed_ips[row["source_ip"]] += 1

# Display the results
print("=== Authentication Log Analysis ===")
print(f"Total login attempts: {total_attempts}")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")

print("\n=== Users with Failed Logins ===")
for username, count in failed_users.most_common():
    print(f"{username}: {count} failed attempts")

print("\n=== Source IPs with Failed Logins ===")
for ip, count in failed_ips.most_common():
    print(f"{ip}: {count} failed attempts")
