#chapter10
#no05

file = open('text5.txt', 'r')

result = []
for x in file.readlines():
    if('\n'in x):

        replaced = x.replace('\n', '')
        splitted = replaced.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)

    else:

        splitted = x.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)

file.close()

output = open('hasiltext5.txt', 'w')

for x in range(len(result)):
    output.write(str(result[x]) + '\n')

output.close()
print('Hasil penjumlahan dapat dilihat dalam file hasiltext5.txt')
        