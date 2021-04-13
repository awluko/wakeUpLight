import time, board, neopixel

pixels = neopixel.NeoPixel(board.D18,12)

def helloSunshine():
	for x in range(5,256,5):
		print(x)
		for y in range(12):
			pixels[y]=(x,x,0)
			time.sleep(0.1)
			print(y)
helloSunshine()

