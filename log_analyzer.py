failed_users = {}
blocked_users = []
BRUTE_FORCE_THRESHOLD = 4

file = open("log.txt", "r")

for line in file:
    if "FAILED" in line:
        username = line.split("user=")[1].strip()

        if username in failed_users:
            failed_users[username] = failed_users[username] + 1
        else:
            failed_users[username] = 1

file.close()

print("=== RAPPORT DE SÉCURITÉ ===")

for user, count in failed_users.items():
    if count >= BRUTE_FORCE_THRESHOLD:
        blocked_users.append(user)
        print("🚨 BRUTE FORCE DÉTECTÉE :", user, "-", count, "échecs → COMPTE BLOQUÉ")
    else:
        print("ℹ️", user, "-", count, "échecs")

print("\nUtilisateurs bloqués :", blocked_users)
