fibo1 = 0
fibo2 = 1
fi = []
fi.append(fibo1)
index = int(input("your number: "))

for i in range(0, index + 1):
    fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo
    fi.append(fibo)

print(fi[index + 1])
