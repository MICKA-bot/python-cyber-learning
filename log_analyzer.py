failed_users = {}
ALERT_THRESHOLD = 3

file = open("log.txt", "r")

for line in file:
    if "FAILED" in line:
        parts = line.split("user=")
        username = parts[1].strip()

        if username in failed_users:
            failed_users[username] = failed_users[username] + 1
        else:
            failed_users[username] = 1

file.close()

print("Tentatives échouées par utilisateur :")

for user, count in failed_users.items():
    print(user, ":", count)

    if count >= ALERT_THRESHOLD:
        print("🚨 ALERTE :", user, "a", count, "échecs de connexion")
