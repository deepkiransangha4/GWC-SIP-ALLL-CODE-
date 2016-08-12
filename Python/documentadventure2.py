"""
Don’t forget to change spaces to tabs
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
	return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False
x_speed = 5
y_speed = 5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
class Circle():
	def __init__(self, mouse_position):
		'''self. (self dot) calls the local variable, you put it in "init" because the 
		variables are used throughout the class (remembers data associated with itself)'''
		self.mouse_position = mouse_position
		self.x_pos = mouse_position[0]
		self.y_pos = mouse_position[1]
	def draw(self):
		global screen
		global RED
		pygame.draw.circle(screen, WHITE, self.mouse_position, 40, 5)
	def move(self, x_speed, y_speed):
		#screen.fill(BLACK)
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.x_pos += x_speed
		self.y_pos += y_speed
		
		
circle_list = []

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	pressed = pygame.mouse.get_pressed()
	position = pygame.mouse.get_pos()

	#print(pressed)
	if pressed[0] == 1:
		circles = Circle(position)
		print(position)
		screen.fill(BLACK)
		circle_list.append(circles)
		#the class is just a blueprint whereas object is the actual thing which is why you use circles (object) and not Circle (class)
		circles.draw()
		circles.move(x_speed, y_speed)
		

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	

	# --- Drawing code should go here




	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

