import subprocess

print('Perform Windows firewall audit')
fwprocess = subprocess.run(['powershell','Show-NetFiewallFule'], stdout=subprocess.PIPE)
results = str(fwprocess.stdout)

bannedapps = ['FTP']
for item in bannedapps:
    if item in results:
        print("Application "+item+" found, not permitted by the company")
