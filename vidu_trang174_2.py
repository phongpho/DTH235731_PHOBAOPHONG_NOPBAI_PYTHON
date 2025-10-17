import turtle as t
s = t.getscreen()
t.title('Đồ họa con rùa')
pen = t.getpen()
pen.pensize(1)
for x in range(100):
    t.forward(x)
    t.left(90)

t.mainloop()