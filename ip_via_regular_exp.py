import os
import re
f = os.popen("ipconfig")
#print f
data = f.read()
f.close()
ips = re.findall(r"Default Gateway.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data)
print ips[0].split()[-1]
