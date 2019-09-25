from graph import *

eyeOffsetX = 50
eyeOffsetY = 20

penColor('black')
brushColor('yellow')
circle(200, 200, 100)
brushColor('red')
circle(200 - eyeOffsetX, 200 - eyeOffsetY, 20)
circle(200 + eyeOffsetX, 200 - eyeOffsetY, 15)
brushColor('black')
circle(200 - eyeOffsetX, 200 - eyeOffsetY, 10)
circle(200 + eyeOffsetX, 200 - eyeOffsetY, 7)
polygon([(149, 250), (250, 250), (250, 270), (149, 270)])
polygon([(221, 176), (219, 166), (298, 137), (301, 145)])
polygon([(177, 176), (182, 167), (103, 118), (100, 127)])
run()
