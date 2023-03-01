bilangan = input("Masukkan sekumpulan bilangan (pisahkan dengan koma):")

list_bil = bilangan.split(",")

list_bil_int = list(map(int, list_bil))

bilangan_terbesar = max(list_bil_int)
bilangan_terkecil = min(list_bil_int)

print("Bilangan terbesar dari kumpulan bilangan yang di input adalah " + str(bilangan_terbesar))
print("Bilangan terkecil dari kumpulan bilangan yang di input adalah " + str(bilangan_terkecil))