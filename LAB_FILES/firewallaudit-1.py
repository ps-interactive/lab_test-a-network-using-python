import subprocess

print('Perform audit of Linux firewall')
fwprocess = subprocess.run(['sudo','ufw','status'], stdout=subprocess.PIPE)
results = str(fwprocess.stdout)

# Check port are compliance with company policy
bannedports = ['20','21','80','110','4444']
for item in bannedports:
    if item in results:
        print("port "+item+" found and not permitted by the company")

# Check for IPv6, company does not use this protocol
if "(v6)" in results:
    print("IPv6 rules identified, recommend remove IPv6 network if unused")

# Count rules
denyrulescount = results.count('DENY')
if denyrulescount == 0:
    print("No DENY rules found!")
else:
    print(denyrulescount+" DENY rules found for review")

print(result.count("Anywhere")+" Anywhere rules identified")
