#Imports everything from the TurtleWorld module in the swampy package

from swampy.TurtleWorld import *	



#Create a TurtleWorld assigned to 'world' and a Turtle assigned to 'bob'

world = TurtleWorld()   
bob = Turtle()


# bob refers to an instance of a Turtle as defined in module 'TurtleWorld'
#   'instance' means a member of a set; this Turtle is one of the set of 
#   possible Turtles

print bob    # output: '<TurtleWorld.Turtle instance at 0xb7bfbf4c>'



#Draw a right angle

fd(bob, 100)   #Take 100 steps forward
lt(bob)        #Take a left turn
fd(bob, 100)   #Take 100 steps forward again
lt(bob)        #Take a left turn
fd(bob, 100)   #Take 100 steps forward again
lt(bob)        #Take a left turn
fd(bob, 100)   #Take 100 steps forward again



#Example of 'for' statement
for i in range(4):
    print 'Hello!'


#Rewrite square drawing using a for statement
fd(bob, 100)
for i in range(3):
   lt(bob)
   fd(bob, 100) 

#Tell TurtleWorld to wait for the user to do something...

wait_for_user()
