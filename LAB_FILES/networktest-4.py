from telnetlib import Telnet
# Test a service is running
with Telnet('add.ip.address.here', 110) as tn:
    tn.interact()
