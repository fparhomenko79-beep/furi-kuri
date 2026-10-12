from turtle import *

K = 30

screensize(2000, 2000)
tracer(0)
lt(90)

rt(30)

for i in range(3):
    rt(150)
    fd(6 * K)
    rt(30)
    fd(12 * K)

up()
for i in range(-20, 20):
    for j in range(-20, 20):
        goto(i * K, j * K)
        dot(5, "red")

done()