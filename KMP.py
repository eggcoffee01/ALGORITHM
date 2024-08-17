def makeTable():
    j = 0
    for i in range(1, N):
        while(0 < j and pattern[i] != pattern[j]):
            j = table[j-1]
        if(pattern[i] == pattern[j]):
            j+=1
            table[i] = j

def KMP():
    strlen = len(string)
    patlen = len(pattern)
    i = 0
    j = 0

    while(i < strlen):
        if string[i] == pattern[j]:
            i+=1
            j+=1
        if j == patlen:
            print("Found pattern at index", i-j)
            j = table[j-1]
        elif i < strlen and string[i] != pattern[j]:
            if j != 0:
                j = table[j-1]
            else:
                i+=1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    pattern = "ABABCABAB"
    string = "ABABDABACDABABCABAB"
    N = len(pattern)
    table = [0 for _ in range(N)]
    makeTable()
    KMP()

