import nmap
import subprocess

nm = nmap.PortScanner()
print('Perform default port scan')
nm.scan('add.ip.address.here')
print(nm.scaninfo())
