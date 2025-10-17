import turtle as t
s = t.getscreen()
t.title('Đồ họa con rùa')
pen = t.getpen()
pen.pensize(1)
t.reset()
for alpha in range(0,360,15):
    t.seth(alpha)
    t.circle(100)

t.mainloop()