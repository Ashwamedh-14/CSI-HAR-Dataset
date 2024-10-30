l = []

with open("./libraries.txt", 'r') as myfile:
    myfile.readline()
    myfile.readline()
    for i in myfile.readlines():
        l.append(i.split())

with open("requirements.txt", 'w') as myfile:
    for i in l:
        s = i[0] + '==' + i[1] + '\n'
        myfile.write(s)
        print(s)