import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()
x=[]
y=[]
for i in range(-20,21,3):
    x.append(i)
    y.append(-2*i*i + 3*i + 5)


plt.plot(x,y)

st.pyplot(fig)









import sys
sys.exit()

col1, col2, col3 = st.columns(3)


with col1:
    c1= st.radio('선의 색을 선택하시오',['red', 'green', 'blue', ' orange'])

with col2:
    s1= st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])

with col3:
    m1= st.radio('마커의 형태를 선택하시오',['p','s','p','h'])
fig, ax = plt.subplots()

x=[]
y=[]
for i in range(-20,21,2):
    x.append(i)
    y.append(-2*i*i+3*i+5)

#plt.plot(x,y,'r:h')
plt.plot(x,y,color=c1, linestyle=s1, marker=m1)

st.pyplot(fig)



import sys
sys.exit()
























# color = st.radio('선의 색을 선택하시오', [ 'red', ' green', 'blue'])

# fig, ax = plt.subplots()

# x = []
# y = []
# ysin=[]
# for i in range(-20, 21, 1):
#     x.append(i)
#     y.append(3*i*i - 5*i + 2)
#     ysin.append(1200*np.sin(i))



# plt.plot(x,y color = color = c1, label = ' 2nd Equation')
# plt.plot( x,y, 'rs-' , color = c1, label = '2nd Equation')
# plt.plot( x,ysin, 'go--' , label = 'sin fumction')
# plt.legend()
# plt.xlabel('x-axis')
# plt.ylabel('2nd Equation & sin Function')
# plt.xlim([-15,15])
# plt.ylim([-2000,2000])
# st.pyplot(fig)



# import sys
# sys.exit()













# import streamlit as st
# # import random
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# x=[]
# for i in range(-100, 100):
#     x.append(i/10.0)

# col=st.columns(3)
# with col[0]:
#     a=st.number_input('Insrt a', step = 1)

# with col[1]:
#     b=st.number_input('Insrt b', step = 1)

# with col[2]:
#     c=st.number_input('Insrt c', step = 1)

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)

# plt.plot(x,y)

# st.pyplot(fig)



































# import turtle
# t=turtle.Turtle()
# t.shape('turtle')


# def tree(length):
#     if length>5:
#         t.forward(length)
#         t.right(20)
#         tree(length-15)
#         t.left(40)
#         tree(length-15)
#         t.right(20)
#         t.backward(length)

# t=turtle.Turtle()
# t.left(90)

# t.color('green')
# t.speed(0)
# tree(90)        
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)

# def shape(sh):
#     for j in range(sh):
#             t.fd(1+5*i)
#             t.left(360/sh)




# sh = 5
# while True:
#     for i in range(30):
#             if i < 10:
#                  shape(3)
#             elif i < 20:
#                  shape(4)
#             elif i < 30:
#                  shape(5)     
       
#         t.color((r.random(),r.random(),r.random()))
#         t.goto(i*20,0)



# turtle.done()




























# screen = turtle.Screen()

# iml = 'rabbit.gif'
# screen.addshape(iml)

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()


# t1.shape(iml)
# t2.shape('turtle')

# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300,-100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(1)

# for i in range(50):
#     d1=random.randint(1,30)
#     t1.fd(d1)
#     d2=random.randint(1,30)
#     t2.fd(d2)


# turtle.done()


# for _ in range(6):
#     a1=r.randint(1,45)
#     a1
#     a2 = r. random()
#     a1,a2 

# a = 0
# n = 10
# for i in range(n):
#     c = r.choice('abcedf')
#     if c == 'a':
#         a = a + 1

# a/n, '%'


# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# turtle.done()

# def rec(x, y, lx, ly):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)

# rec(-200,0,100, 50)
# rec(0,0,100, 150)
# rec(200,0,100, 50)




# turtle.done()





# colors = ['red','purple','blue','yellow','orange','green']

# # turtle.bgcolor('black')
# t.width(2)


# length=5
# for i in range(100):
#     t.forward(length)
#     t.right(89)
#     # t.pencolor(colors[length%6])
#     length +=5





# for i in range(1,10):
#     if i%3==1:
#         i



# def user_ sum(n):
#     s=0
#     for i in range(1,n+1):
#         s = s + 1

#         s


# user_sum(100)
# user_sum(200)










































# s =70
# if s >= 90:
#     st.write('귀하의 점수는'+ str(s)+' 점으로 :blue[A등급]입니다')
# elif s >=80:
#     '귀하의 점수는'+ str(s) +'점으로 :green[B등급]입니다'
# elif s >=70:
#     '귀하의 점수는'+ str(s) +'점으로 :orange[c등급]입니다'
# elif s >=60:
#     '귀하의 점수는'+ str(s) +'점으로 :blue[D등급]입니다'
# else:
#     '귀하의 점수는'+ str(s) +'점으로 :red[F등급]입니다'


# s = 0
# for i in range(1,101,2):
#     #'s=', s, 'i = ', i
#     #s = s + 1
#     s+=i
#     #'s + i = ', s
# s

# '7과 4의 연산'

# '덧셈', 7+4
# '뺄셈', 7-4
# '곱셈', 7*4
# '나눗셈', 7/4
# '몫', 7//4
# '나머지', 7%4
# '거듭제곱', 2**4













# import turtle

# t= turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# t.circle(100)

# turtle.done()


























# import turtle
# t=turtle.Turtle()
# t.shape('turtle')

# r=90
# t.left(60)
# t.forward(r)
# t.right(120)
# t.forward(r)

# t.right(30)
# t.forward(r)

# t.right(90)
# t.forward(r)
# t.right(90)
# t.forward(r)
# t.right(90)
# t.forward(r)

# turtle.done()


# t=turtle.Turtle()
# t.fillcolor('blue')
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# distane=150
# angle=45
# for i in range(8):
#     t.forward(distance)
#     t.left(angle)


# print('Hello')
# st.write('Hello')
# st.write('강아지'+'고양이')
# st.write('1'+'1')
# st.write(2)

# st.write('스트림릿......') 
# st.image('im.jfif')
# st.title("streamlit image")




