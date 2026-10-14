from turtle import *

K = 30

screensize(2000, 2000)
tracer(0)
lt(90)

for i in range(2):
    fd(7 * K)
    rt(90)
    fd(20 * K)
    rt(90)

up()
fd(3 * K)
rt(90)
fd(7 * K)
lt(90)
down()

for i in range(4):
    rt(90)
    fd(7 * K)

up()
for i in range(-30, 30):
    for j in range(-30, 30):
        goto(i * K, j * K)
        dot(5, "blue")

done()