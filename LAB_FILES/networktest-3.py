import subprocess

print('Perform regular ping, 3 times')
pingprocess1 = subprocess.Popen(['ping','-c','3','add.ip.address.here'])
print(str(pingprocess1.stdout))

pingprocess2 = subprocess.Popen(['ping','-c','3','add.ip.address.here'])
print(str(pingprocess2.stdout))
