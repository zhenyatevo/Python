with open('fileForMainUnderWordStepik.txt','r') as inf:
    d={}
    for line in inf:
        line = line.split(' ')
        for c in line:
            if c in d:
                d[c] = d[c]+1
            else:
                d[c] = 1
value = sorted(d.values())[-1]
for key in d.keys():
    if d[key] == value:
        print(key,value)
        break

        
    

    

