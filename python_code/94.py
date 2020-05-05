import re

addr = '192.168.0.1'

ip = re.search(r'(([01]{0,1}\d{0,1}\d| 2[0-4]\d \
    |25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',addr)
print(ip)

# 95
a = "abbbccc"
a = re.sub(r'b+','b', a)
print(a)

# 97 
# 前者是贪心匹配，后者是非贪心匹配