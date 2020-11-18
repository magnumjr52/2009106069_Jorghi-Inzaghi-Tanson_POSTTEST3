print("Buatlah program yang menerima bilangan N dan menuliskan bilangan 10^x terkecil yang lebih dari N!")
print("")
print("Jawaban :")

N = int(input("Bilangan ke-N : "))
x = 1

while 10**x < N:
    x += 1

print("Saat N = %s, Bilangan 10^x terkecil yang lebih dari N = %s" %(N, 10**x))