import subprocess

print('Perform custom port scan')
# reference command: sudo nmap -sS -v -v -Pn 172.31.37.140
dumpprocess = subprocess.Popen(['sudo','nmap','-sS','-v','-v','-Pn','add.ip.address.here'], start_new_session=True, stdout=subprocess.PIPE)
print(dumpprocess.stdout)

# , str(dumpprocess.pid)
