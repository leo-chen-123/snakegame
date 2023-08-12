
import random
import turtle
import time


detections = []
t = turtle.Turtle()
t2 = turtle.Turtle()
scoret = turtle.Turtle()
wall = turtle.Turtle()
direction = "right"
eatenamount = 0
def turn_up():
  global direction
  if (direction != "down"):    
    offset = t.heading()
    t.right(offset-90)
    direction = "up"
 
def turn_down():
  global direction
  if (direction != "up"):   
   offset = t.heading()
   t.right(offset+90)
   direction = "down"
  
def turn_left():
  global direction
  if (direction != "right"):   
    offset = t.heading()
    t.right(offset-180)
    direction = "left"
    
def turn_right():
  global direction
  if (direction != "left"):   
   offset = t.heading()
   t.right(offset)
   direction = "right"
   
ingame = True

def quit():
  global ingame
  ingame = False
def controls():
  turtle.listen()
  turtle.onkeypress(turn_up, 'Up')
  turtle.onkeypress(turn_down, 'Down')
  turtle.onkeypress(turn_left, 'Left')
  turtle.onkeypress(turn_right, 'Right')
  turtle.onkeypress(quit, 'q')

wallength=280
def apple():
  x=random.randint(-wallength+40,wallength-40)
  y=random.randint(-wallength+40,wallength-40)
  t2.penup()
  t2.ht()
  t2.goto(x,y)
  t2.pendown()
  t2.circle(10)
  t2.penup()
  t2.left(90)
  t2.forward(10)


def makewall():
  wall.color("red")
  wall.ht()
  wall.speed(0)
  wall.penup()
  wall.forward(wallength)
  wall.pendown()
  wall.left(90)
  wall.forward(wallength)
  wall.left(90)
  wall.forward(wallength*2)
  wall.left(90)
  wall.forward(wallength*2)
  wall.left(90)
  wall.forward(wallength*2)
  wall.left(90)
  wall.forward(wallength)
  wall.penup()
  wall.goto(0,0)
  wall.pendown()
makewall()
controls()

def score(eatenamount, size=12):
    scoret.clear()
    scoret.ht()
    scoret.penup()
    scoret.goto(-290, 290)
    scoret.pendown()
    scoret.write(eatenamount, font=("Arial", size, "normal"))

 




apple()
while ingame==True:
  t.pendown()
  t.forward(4)
  time.sleep(0.005)
  position = t2.pos()
  pos = t.pos()
  if pos in detections or (abs(pos[0])>wallength or abs(pos[1])>wallength):
   ingame=False
   break
  else:
    ingame=True
    detections.append(pos)
  
  
  
  
  if (t.distance(position)) <= 10:
    eaten = True
    t2.clear()
    apple()
    eatenamount += 1
    wallength-= 20
    wall.clear()
    makewall()
    score(str(eatenamount))
    
turtle.mainloop()


