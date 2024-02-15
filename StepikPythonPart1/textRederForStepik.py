with open('fileFortextRederForStepik.txt','r') as inf:
    s1 = inf.readline()
    print(s1)
    mn=''
    res=''
    a=s1[0]
    for i in range(1,len(s1)):
        if s1[i] in ['0','1','2','3','4','5','6','7','8','9']:
            mn += s1[i]
        else:
            res+=a*int(mn)
            a = s1[i]
            mn=''
    
    print(res)


