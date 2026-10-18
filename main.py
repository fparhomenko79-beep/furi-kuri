def f(x: int, y: int, z: int, w: int, u: int):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))

print("x y z w u")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    res = f(x, y, z, w, u)
                    if not res:
                        print(x, y, z, w, u, res)
