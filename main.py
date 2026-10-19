def f(x, y, z, w):
    return x and (y <= z) and ((not y) <= ((not z) == w))

print("x y z w F")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, y, z, w, f"{"1" if f(x, y, z, w) else 0}")