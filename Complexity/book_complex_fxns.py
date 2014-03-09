def dnaComplexity(seq, abet, wordsize, wind):
    labet=len(abet)
    L=len(seq)-wind
    vec=zeros(L, float)
    mx=float(labet**wordsize)
    for i in range(L):
        words=[]
        for j in range(i, i+wind+1):
            words.append(seq[j:j+wordsize])
        ct=len(set(words))
        vec[i]=ct/mx
    return vec

