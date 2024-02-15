with open('fileForUspevaemostSrednyayaStepik.txt','r') as inf:
    students =0
    math = 0
    ph =0
    ru = 0
    for line in inf:
        students += 1
        line = line.split(';')
        res = int(line[1]) + int(line[2]) + int(line[3])
        math += int(line[1])
        ph += int(line[2])
        ru += int(line[3])
        print(res/3)
    print(math/students,ph/students,ru/students)
            

        
    

    

