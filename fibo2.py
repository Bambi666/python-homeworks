fi = [0, 1]

index = int(input("your number: "))

for i in range(0, index + 2):
    fibo = fi[-2] + fi[-1]
    fi.append(fibo)

print(fi[index])
