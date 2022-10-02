n = int(input())
mas = list(map(int, input().split()))
for i in range(len(mas)):
    mas0 = mas.copy()
    j = i - 1
    key = mas[i]
    while mas[j] > key and j >= 0:
        mas[j + 1] = mas[j]
        j -= 1
    mas[j + 1] = key
    if mas0 != mas:
        print(" ".join(map(str, mas)))
        mas0 = mas
print(mas)
print("end")
