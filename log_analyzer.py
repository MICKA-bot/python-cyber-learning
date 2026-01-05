failed_count = 0
success_count = 0
total_count = 0

file = open("log.txt", "r")

for line in file:
    total_count = total_count + 1

    if "FAILED" in line:
        failed_count = failed_count + 1
    elif "SUCCESS" in line:
        success_count = success_count + 1

file.close()

print("Connexions réussies :", success_count)
print("Connexions échouées :", failed_count)
print("Total des tentatives :", total_count)
