import turtle
import time

#import turtle object from the turtle library and import the randint from the random library
from turtle import Turtle
from random import randint

screen = turtle.Screen();
turtle = Turtle();

#Setup the grass
screen.bgcolor("forestgreen");
turtle.color("white");
turtle.speed(0);
turtle.penup();
turtle.goto(-120, 150);
turtle.write("TURTLE RACE", font=("Arial", 20, "bold"));
turtle.penup();

#Setup the dirt
turtle.goto(-200, -150);
turtle.color("chocolate");
turtle.begin_fill();
turtle.pendown();
turtle.forward(400);
turtle.right(90);
turtle.forward(60);
turtle.right(90);
turtle.forward(400);
turtle.end_fill();

#Setup finish line
square_size = 15
finish_line = 170

turtle.color("black");
turtle.shape("square");
turtle.penup();

#Stamping the finish line
for i in range(10):
  turtle.goto(finish_line, (140 - (i * square_size * 2)));
  turtle.stamp();
  
for j in range(9):
  turtle.goto(finish_line + square_size, ((140 - square_size) - (j * square_size * 2)));
  turtle.stamp();
  
turtle.hideturtle();

#Setup turtles
myTurtle1 = Turtle();
myTurtle1.speed(0);
myTurtle1.color("red");
myTurtle1.shape("turtle");
myTurtle1.penup();
myTurtle1.goto(-170, 100);
myTurtle1.pendown();


myTurtle2 = Turtle();
myTurtle2.speed(0);
myTurtle2.color("yellow");
myTurtle2.shape("turtle");
myTurtle2.penup();
myTurtle2.goto(-170, 50);
myTurtle2.pendown();


myTurtle3 = Turtle();
myTurtle3.speed(0);
myTurtle3.color("cyan");
myTurtle3.shape("turtle");
myTurtle3.penup();
myTurtle3.goto(-170, 0);
myTurtle3.pendown();


myTurtle4 = Turtle();
myTurtle4.speed(0);
myTurtle4.color("purple");
myTurtle4.shape("turtle");
myTurtle4.penup();
myTurtle4.goto(-170, -50);
myTurtle4.pendown();



time.sleep(1);

#Move turtles
for i in range(110):
  myTurtle1.forward(randint(1, 5));
  myTurtle2.forward(randint(1, 5));
  myTurtle3.forward(randint(1, 5));
  myTurtle4.forward(randint(1, 5));



winnerTurtle = Turtle();
winnerTurtle.hideturtle();
winnerTurtle.penup();
winnerTurtle.setx(0);
winnerTurtle.sety(0);





raceTurtleMap={}
raceTurtleMap[("Red")]=myTurtle1;
raceTurtleMap[("Yellow")]=myTurtle2;
raceTurtleMap[("Cyan")]=myTurtle3;
raceTurtleMap[("Purple")]=myTurtle4;

keys = raceTurtleMap.keys();
print(keys);

winnerTurtleColor = ""
for i in range(len(keys)):
  eachKey = keys[i];
  eachTurtle = raceTurtleMap[eachKey];
  if (eachTurtle.xcor() > winnerTurtle.xcor()):
    winnerTurtle = eachTurtle;
    winnerTurtleColor = eachKey;
    

print(winnerTurtleColor);


winnerTurtleMessage = "WINNER: " + winnerTurtleColor + " Turtle";
turtle.color("white");
turtle.speed(0);
turtle.penup();
turtle.goto(-120, -100);
turtle.write(winnerTurtleMessage, font=("Arial", 20, "bold"));
