import requests

with open('fileFORRequestsStepik.txt','r') as inf:
    url = inf.readline().strip()

    
    r = requests.get(url).text.splitlines()
    counter = 0
    for line in r:
        counter+=1
print(counter)
