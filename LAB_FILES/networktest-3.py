import subprocess

print('Perform regular ping, 3 times')
pingprocess = subprocess.Popen(['ping','-c','3','add.ip.address.here'])
print(str(pingprocess.stdout))
