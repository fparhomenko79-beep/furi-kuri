n = f"{400:b}"
print(n)
res = ""
for i in range(len(n)):
    res += str(1 - int(n[i]))
print(int(res, 2))