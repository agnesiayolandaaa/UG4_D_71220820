bilangan = input("Masukkan sebuah bilangan (pisahkan dengan koma):")

list_bilangan = bilangan.split(",")

list_bilangan_int = list(map(int, list_bilangan))

bilangan_terbesar = max(list_bilangan_int)
bilangan_terkecil = min(list_bilangan_int)

print("Bilangan terbesar dari kumpulan bilangan yang di input adalah " + str(bilangan_terbesar))
print("Bilangan terkecil dari kumpulan bilangan yang di input adalah " + str(bilangan_terkecil))