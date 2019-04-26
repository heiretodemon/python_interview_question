def get_missing_letter(word):
    s1 = set('abcdefghijklmnopqrstuvwxyz')
    s2 = set(word.lower())
    miss = "".join(sorted(s1-s2))
    return miss

if __name__ == '__main__':
    print(get_missing_letter('Python'))