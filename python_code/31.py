import re

def word_fre(filepath):
    fre = {}

    with open(filepath) as f:
        for line in f:
            line = re.sub('\W+', ' ', line) # \W匹配任意非数字和字母字符,都将其替换为空格
            print(line)
            words = line.split()
            for word in words:
                if not fre.get(word):
                    fre[word] = 1
                else:
                    fre[word] +=1
    
    num_ten = sorted(fre.items(), key=lambda x:x[1], reverse=True)[:10]
    num_ten = [x[0] for x in num_ten]
    return num_ten

from collections import Counter

def word_fre2(filepath):
    with open(filepath) as f:
        return list(map(lambda x: x[0], Counter(re.sub('\W+', 
        ' ', f.read()).split()).most_common(10)))

if __name__ == '__main__':
    filepath = "31.txt"
    print(word_fre2(filepath))