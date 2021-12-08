#import statements
import turtle as trtl

import random as rand



#variables



wn = trtl.Screen()
# Background Color is turqoise
wn.bgcolor('paleturquoise')
#screen coordinates
trtl.setworldcoordinates(-10,-10,10,10)
#list of shapes for players to pick from
shapes = ['circle','square','triangle']
#different y pos for each of the two players
y_pos = [-5,5]

#list of numbers for each die
dice = [1,2,3,4,5,6]


#list for players
players = []
#functions
#based on the user's input a shape is drawn. each shape is a different color to represent a different player
def draw_shape(shape):
  t = trtl.Turtle()
  if shape == 'circle':
    t.fillcolor("orchid")
    t.begin_fill()
    t.shape('circle')
    t.end_fill()
  elif shape == 'square':
    t.fillcolor("lightgreen")
    t.begin_fill()
    t.shape('square')
    t.end_fill()
  elif shape == 'triangle':
    t.fillcolor("palevioletred")
    t.begin_fill()
    t.shape('triangle')
    t.end_fill()
  return t
#each player will get a different starting position
def player_position(player,x,y):
  player.penup()
  player.goto(x,y)
  player.pendown()
  
#players input the shape that they want to use as their character
def pick_shape():
  text = "please choose a shape from: "
  text = text + str(shapes)[1:-1]
  shape = wn.textinput("input",text)
  return shape







#in a loop that repeats twice so that two players can pick a shape. The shape that the first player choses is removed from the lsit so each player gets a different character.
for i in range(2):
  shape = pick_shape()
  player = draw_shape(shape)
  player_position(player,-9,y_pos[i])
  shapes.remove(shape)
  players.append(player)

t = trtl.Turtle()

print("click 'f'")
def finish_line():
  t.penup()
  t.goto(9,10)
  t.right(90)
  t.pensize(2)
  t.speed(0)
  for i in range (10):
    t.pendown()
    t.forward(1)
    t.penup()
    t.forward(1)

  t.penup()
  t.goto(9,10)

  for i in range (10):
    t.penup()
    t.forward(1)
    t.pencolor("white")
    t.pendown()
    t.forward(1)


current_player = 0
dice_roll = None

#this print statement tell users which key to press in order to move forward.
print("Press on the space bar to move")

#players_list[current] makes sure that we are moving the correct player. If the roll keeps the x value behind the  finish line, then it moves forward the roll value. If it passes the finish line then that means the player has won the game.
def move_player(players_list, current, roll):
  player = players_list[current]
  player.penup()
  position = player.pos()
  if position[0] + roll < 9:
    player.forward(roll)
  else:
    print("Congrats! You won!")
    player.goto(9,position[1])
    wn.onkey(None,' ')

#dice roll using on key (r).A random number from our dice list is produced, and that is the amount of spaces forward the shape will move.
def dice_roll():
  global dice_roll
  global current_player
  global players
  dice_roll = rand.choice(dice)
  move_player(players, current_player, dice_roll)
  if current_player == 0:
    current_player = 1
  else:
    current_player = 0

#events



wn.onkey(dice_roll,' ')
wn.listen()

wn.onkey(finish_line,'f')
wn.listen()

wn.mainloop()
