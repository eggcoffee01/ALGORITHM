def bm_match(txt, pat):
    skip = [None] * 256

    for pt in range(256):
        skip[pt] = len(pat)
    
    for pt in range(len(pat) - 1):
        skip[ord(pat[pt])] = len(pat) - pt - 1
    
    
    pt = len(pat) - 1
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        if skip[ord(txt[pt])] > len(pat) - pp:
            pt += skip[ord(txt[pt])]
        else:
            pt += len(pat) - pp
    
    return -1
    


if __name__ == "__main__":

    s1 = input()
    s2 = input()

    idx = bm_match(s1, s2)
 
    print(idx)