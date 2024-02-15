import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('fileFORUrlsStepik.txt') as inf:
    l = inf.readline().strip()

r = requests.get(l)
r = link + r.text

flag = True
while(flag):
    r = requests.get(r)
    if (r.text.count('.txt')):
        print(r.text) # Что бы было видно что консоль не просто висит
        r = link + r.text
    else:
        flag = False
        print(r.text)
