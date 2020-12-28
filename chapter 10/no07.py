#chapter10
#no07

def decrypt(teks, n):
    listTeks = list(teks)

    for x in range(len(listTeks)):
        if(listTeks[x] != ''):
            if(ord(listTeks[x]) - n <= 90):
               asciiCode = ord(listTeks[x])
               decrypted = asciiCode - n
               listTeks[x] = chr(decrypted)

            else:
                asciiCode = ord(listTeks[x])
                decrypted = (asciiCode + 26) - n
                listTeks[x] = chr(decrypted)

        else:
            continue

    result = ''.join(listTeks)

    return result
try:
    teks = input('Masukan teks yang ingin dienskripsi :')
    n = int (input('Berapa jumlah geseran enskripsi :'))

    hasil = decrypt(teks, n)
    print('\nHasil enkripsi dari teks {0} adalah : {1}'.format(teks, hasil))

except ValueError:
    print('Masukan khusus bilangan bulat')
