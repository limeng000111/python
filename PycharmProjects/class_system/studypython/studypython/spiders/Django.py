#!/usr/bin/python

with open(r'c:\Users\dell\Desktop\senduser.csv','r+') as f:
    fp = f.read().split(',')

    csv = []
    for i in fp:
        csv.append(i)
    print(csv)
    doc = open(r'c:\Users\dell\Desktop\python.txt','a')
    for i in csv:
        print(i, file=doc)

