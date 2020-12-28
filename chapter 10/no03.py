#chapter10
#no03

file = open ('text2.txt', 'r')
line = file.readlines()

dict = {}
listDict = []

for x in range(len(line)) :
    y = line[x].split('|')
    y[2] = y[2].replace('\n','')

    dict = {'nim' : y[0], 'nama' : y[1], 'alamat' :y[2]}

    listDict.append(dict)

print(listDict)
