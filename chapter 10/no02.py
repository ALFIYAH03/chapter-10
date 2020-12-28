#chapter10
#no02

file = open('text2.txt', 'a')

x = True
while (x == True):
    nim = input ('masukan NIM : ')
    namaMhs = input('Masukan Nama MHS : ')
    alamat = input('Masukan Alamat : ')

    file.write(nim + '|' + namaMhs + '|' + alamat + '\n')
    ulangi = input('input lagi (y/n : \n')

    if(ulangi.lower() == 'y') :
        x = True
    elif (ulangi.lower == 'n'):
        x = False
    else :
        print('inputan anda tidak valid')
        continue

file.close()
file.readline()
