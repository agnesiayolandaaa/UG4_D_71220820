kalimat = input('Masukkan sebuah kalimat: ')

kata = kalimat.split()
kata_terpanjang = max(kata, key=len)

print('Kata terpanjang dalam kalimat tersebut adalah:', kata_terpanjang)