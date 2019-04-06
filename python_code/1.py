import sys

def get_lines():
	with open('1.txt', 'rb') as f:
		return  f.readlines()
		
if  __name__ == '__main__':
	for e in get_lines():
		print(e)  # 打印每一行数据	
		

# 当文件非常大超过当前内存值时
from mmap import mmap

def get_lines(fp):
	with open(fp, "r+") as f:
		m = mmap(f.fileno(), 0)  # 0表示映射整个文件
		tmp = 0
		for i, char in enumerate(m):
			if char == b"\n":
				yield m[tmp:i+1].decode()
				tmp = i+1
				
if __name__ == "__main__":
	for i in get_lines("fp_some_huge_file"):
		print(i)
	