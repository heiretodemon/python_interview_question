def str_count(str_data):
    """
    :return: the number of each char
    """
    dict_str = {}
    for i in str_data:
        dict_str[i] = dict_str.get(i, 0) + 1
    return dict_str

if __name__ == '__main__':
    dict_str = str_count('AAAABBBBCCCABC')
    str_count_data = ""
    for k, v in dict_str.items():
        str_count_data += k + str(v)
    print(str_count_data)


# 方法2
from collections import Counter

print("".join(map(lambda x: x[0] + str(x[1]), Counter("AAABBCCCXADS").most_common())))