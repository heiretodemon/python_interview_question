class Solution(object):
    def reverse(self, x):
        if -10<x<10:
            return x
        str_x = str(x)
        # 输入为正数
        if str_x[0]!='-':
            str_x = str_x[::-1]
            x = int(str_x)
        else: # 输入为负数
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x if -2147483648<x<2147483647 else 0

if __name__ == '__main__':
    s = Solution()
    a = input("please input: ")
    reverse_int = s.reverse(int(a))
    print(reverse_int)