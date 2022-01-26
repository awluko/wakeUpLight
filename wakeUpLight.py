######################################
# wakeUpLight.py is a script that runs on a wake up light using a NeoPixel ring and a Raspberry Pi Zero WH
######################################

import board, neopixel # Specific to the Raspberry Pi, comment out for testing
import time, json
from datetime import datetime

# Sets the pixels variable to the D18 pin on the board and establishes that there are 12 LEDs. These values may need to change
pixels = neopixel.NeoPixel(board.D18,12)

def settings_load():
	# Loads the settings.json file to pull the current alarm settings
	print("Pulling settings")
	with open("settings.json", "r", encoding="utf-8") as f:
		settings = json.load(f)
	return settings

# Compares the times set based on the day versus the current time. 
def wakeUp(t = 900):
	# Executes the wake up protocol from goodMorning, sleeping, and lightsOff
	try:
		print("Calling goodMorning")
		goodMorning()
		# Default for t is 900 seconds or 15 minutes
		print(f"Sleeping for {int(t/60)} minutes")
		time.sleep(t)
		print("Slept successfully, turning lights off")
		lightsOff()
		print("Done\n")
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
			time.sleep(0.25)
	time.sleep(300)
	lightsOff()

def main():

	# Pull JSON file for settings
	settings = settings_load()

	# Pull the current time
	now = datetime.now()
	nowDay = str(now.strftime("%a")) # Day of the week, shorthand (e.g. Mon)
	nowHour = int(now.strftime("%H")) # Hour of the day, 24 hour clock
	nowMin = int(now.strftime("%M")) # Minute of the hour
	print(f"It is {nowDay}, at {nowHour}:{nowMin}\n")

	# Establish current settings
	sHour = settings[nowDay]["h"]
	sMin = settings[nowDay]["m"]
	print(f'Current day/time:\nDay: {nowDay}\n'
		  f'Hour: {nowHour}\nMin: {nowMin}\n\nSettings:\n'
		  f'Hour: {sHour}\nMin: {sMin}\n')

	if nowHour == sHour and nowMin == sMin:
		print("Time matches.")
		wakeUp(120)
	elif nowHour == 22 and nowMin == 0:
		# Triggers the goodnight reminder
		print("Time for bed.")
		goodNight()
	else:
		print("Not the right time, waiting 60 seconds.")
		time.sleep(60)

while True:
	main()
