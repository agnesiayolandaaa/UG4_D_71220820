def aritmatika(a, b, c):
    return (c/2)*(2*a + (c-1)*b)

a = int(input("Masukkan bilangan awal : "))
b = int(input("Masukkan selisih bilangan : "))
c = int(input("Masukkan banyaknya suku : "))

print("Total dari deret aritmatika tersebut adalah:", aritmatika(a, b, c))