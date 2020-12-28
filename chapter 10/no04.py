#chapter10
#no04

mencariNIM = input('Masukan NIM yang dicari : ')

file = open('text2.txt', 'r')

y = file.readlines()

for x in range(len(y)):
    if (mencariNIM in y[x]):
        status ='Ada'
        break
    else:
        status = 'Tidak Ada'
        continue

if(status == 'Ada'):
    z = y[x].split('|')
    print('\nData Mahasiswa')
    print('NIM     :', z[0])
    print('Nama    :', z[1])
    print('Alamat  :', z[2])

else:
    print('Data Mahasiswa tidak ditemukan')
