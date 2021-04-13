######################################
# wakeUpLight.py is a script that runs on a wake up light using a NeoPixel ring and a Raspberry Pi Zero WH
######################################

import board, neopixel, time
from datetime import datetime, timedelta

# Sets the pixels variable to the D18 pin on the board and establishes that there are 12 LEDs. These values may need to change
pixels = neopixel.NeoPixel(board.D18,12)
# Lists for day of the week, ideally this will become more dynamic in the future, Thursday isn't on the list because it is not a work day currently
earlyDays = ["Mon","Tue","Fri"]
earlierDays = ["Wed"]
weekend = ["Sun", "Sat"]



# Compares the times set based on the day versus the current time. 
def timeComp(h, m, mMax, nowHour, nowMin):
	print("timeComp has been called")
	# Displays current settings passed to the function
	print(f"\nSettings are:\nh: {h}\nm: {m}\nmMax: {mMax}\nnowHour: {nowHour}\nnowMin: {nowMin}\n")
	try:
		if nowHour == h:
			print("The hour is accurate")
			if nowMin >= m and nowMin <= mMax:
				print("The minute is accurate, calling goodMorning")
				goodMorning()
				print("Sleeping for 15 minutes")
				time.sleep(900)
				print("Slept successfully, turning lights off")
				lightsOff()
				print("Done\n")
			else:
				print("It is too late, waiting to try again")
				time.sleep(300)
				print("Done waiting")
		else:
			print("The hour is wrong, sleeping for 5 minutes\n")
			time.sleep(300)
	except Exception as e:
		print(f"There was an error.\nThe error was {e}")

# Turns off the LEDs
def lightsOff():
	pixels.fill((0,0,0))

# Function that gradually increases the brightness of the LEds
def goodMorning():
	# Goes from 5 to 256 and sets the color and brightness of the LEDs
	for x in range(5,256,3):
		# Sets the LEDs sequentially
		for y in range(12):
			pixels[y] = (x,x,0)
			time.sleep(0.1)

# Turns the LEDs from a bright blue down until the LEDs are off
def goodNight():
	for x in range(5,256,3):
		brightness = 256 - x
		for y in range(12):
			pixels[y]=(0,0,brightness)
			time.sleep(0.5)

def main():
	while True: # Keeps the loop open		
		# Pull the current time
		now = datetime.now()
		nowDay = str(now.strftime("%a")) # Day of the week, shorthand (e.g. Mon)
		nowHour = int(now.strftime("%H")) # Hour of the day, 24 hour clock
		nowMin = int(now.strftime("%M")) # Minute of the hour
		print(f"It is {nowDay}, at {nowHour}:{nowMin}\n")

		if nowDay in earlyDays:
			print("earlyDays\n")
			# Will prompt the goodMorning function to go off when between 0612 and 0625
			timeComp(6,12,25,nowHour,nowMin)
		elif nowDay in earlierDays:
			print("earlierDays\n")
			# Prompts goodMorning() to go off between 0600 and 0615
			timeComp(6,0,15,nowHour,nowMin)
		elif nowDay in weekend:
			# Prompts goodMorning() to go off between 0900 and 0930
			timeComp(9,30,45,nowHour,nowMin)
		else:
			print("Today is Thursday")
			# Prompts goodMorning() to go off between 1030 and 1045
			timeComp(10,30,45,nowHour,nowMin)

main()
