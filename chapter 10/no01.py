#chapter10
#no01

file = open('text1.txt', 'r')

text1 = file.readlines()

genap = []
ganjil = []

for a in range (len(text1)) :
    if('\n' in text1[a] == True):
        text1[a].replace('\n', '')
        
        if(int(text1[a]%2 == 0)):
           genap.append(text1[a])
        else :
            ganjil.append(text1[a])

    else :
        if(int(text1[a])%2 == 0):
            genap.append(text1[a])
        else :
            ganjil.append(text1[a])

print('Banyaknya bilangan genap : {0}'.format(len(genap)))
print ('Banyaknya bilangan ganjil : {0}'.format(len(ganjil)))
