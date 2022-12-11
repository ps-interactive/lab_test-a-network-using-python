import subprocess

print('Perform Linux firewall audit')
fwprocess = subprocess.run(['sudo','ufw','status'], stdout=subprocess.PIPE)
results = str(fwprocess.stdout)

# Check port compliance with company policy
bannedports = ['20','21','80','110','4444']
for item in bannedports:
    if item in results:
        print("port "+item+" found, not permitted by the company")

# Check for IPv6, company does not use this protocol
if "(v6)" in results:
    print("IPv6 rules identified, recommend remove IPv6 network")

# Count rules
denyrulescount = results.count('DENY')
if denyrulescount == 0:
    print("No DENY rules found!!!")
else:
    print(denyrulescount+" DENY rules found for review")

print("{rules} Anywhere rules identified for review".format(rules=results.count("Anywhere")))
