import time, board, neopixel

pixels = neopixel.NeoPixel(board.D18,12)

while True:
	for i in range(12):
		pixels[i] = (0,255,0)
		time.sleep(1)
		pixels[i] = (0,0,0)

