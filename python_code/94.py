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

# 98
# 贪婪与非贪婪模式影响的是被量词修饰的子表达式的匹配行为，
# 贪婪模式在整个表达式匹配成功的前提下，尽可能多的匹配，
# 而非贪婪模式在整个表达式匹配成功的前提下，尽可能少的匹配。非贪婪模式只被部分NFA引擎所支持。

# 99
# https://blog.csdn.net/u011665991/article/details/80221451

# 102
'''
    import re
    pattern = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    pattern.sub('',test) 
'''

# 103
'''
python re模块里有四种都是匹配字符串的
match:
    匹配string开头，成功则返回match object,失败则返回None,只匹配一个；
search:
    在string中进行搜索，成功返回Match object, 失败返回None, 只匹配一个。
findall:
    在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，
    每个list item是由每个匹配的所有组组成的list。
finditer:
    在string中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object。

参考：https://blog.csdn.net/tp7309/article/details/72823258
'''