def alternatingCharacters(s):
    if len(set(s)) == 1:
        return len(s) - 1
    
    string = ''.join([s[i] for i in range(len(s) - 1) if s[i] != s[i + 1]])
    return len(s) - len(string) - 1
