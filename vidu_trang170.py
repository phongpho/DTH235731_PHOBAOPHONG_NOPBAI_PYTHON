import turtle as t
s = t.getscreen()
t.home()
print('Tọa độ ban đầu: (',t.xcor(),',', t.ycor(),')')
t.forward(100)
print('Tọa độ hiện tại: ', t.pos())
t.setpos(50,50)
print('Tọa độ hiện tại: ', t.pos())
t.backward(100)
print('Tọa độ hiện tại: ', t.pos())

t.mainloop()