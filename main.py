from turtle import *

screensize(2000, 2000)
tracer(0)
K = 20

lt(90)

for i in range(70):
    fd(8 * K)
    rt(30)

up()
for i in range(35):
    for j in range(-35, 35):
        goto(i * K, j * K)
        dot(4, "pink")

done()

