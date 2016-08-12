from PIL import Image
puppy = Image.open("caseyneistat.jpeg")
#im.mode(RGB)
puppy.rotate(360).show()
width = 500
height = 700
Darkblue = (18, 6, 133)
Lightblue = (84, 232, 188)
red = (189, 45, 232)
yellow = (255, 223, 113)


#pixels2 = im.load()
#pixels = list(im.getdata())
#color = pixels[4, 5] # x = 4, y = 5 (0-indexed, of course)

pixels = list(puppy.getdata())

'''R = getRed(pixels)
G = getGreen()
B = getBlue()'''

#for i in range(91):
#	intensity +=2
#x = 0
#y = 0

'''for i in range(0, len(pixels)-1):
		x+=1
		y+=1
		z+=1
		list = pixels[x] + pixels[y] + pixels[z]'''
'''r = pixels[0]
g = pixels[1]
b = pixels[2]'''

pixels2 = []
x = -1

for p in pixels:
	x +=1
	r = p[0]
	g = p[1]
	b = p[2]
	sum = r + g + b
	if sum <= 182:
		pixels2.append(Darkblue)
	elif sum > 182 and sum < 364:
		pixels2.append(Lightblue)
	elif sum > 364 and sum < 546:
		pixels2.append(yellow)
	else:
		pixels2.append(red)
		
image_out = Image.new(puppy.mode,puppy.size)
image_out.putdata(pixels2)
image_out.save("output.jpg", "jpeg")
image_out.show()
		
'''Darkblue = (18, 6, 133)
Lightblue = (61, 246, 255)
red = (232, 50, 48)
yellow = (255, 223, 113)'''
		
		
		
	
	
	
	

	
	
