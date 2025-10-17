import turtle as t
s = t.getscreen()
t.title('Đồ họa con rùa')

pen= t.getpen()

pen.pensize(5)
for i in range(4):
    pen.forward(100)
    pen.right(90)

t.mainloop()