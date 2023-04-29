for TEST in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i] != s[~i]: print(0, i+1); break
    else: print(1, len(s)//2 + 1)