import board, neopixel, time
from datetime import datetime, timedelta

pixels = neopixel.NeoPixel(board.D18,12)
earlyDays = ["Mon","Tue","Wed","Fri"]
weekend = ["Sun", "Sat"]

#thing = "go"

def timeComp(h, m, mMax, nowHour, nowMin):
	#global thing
	print("timeComp has been called")
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

def lightsOff():
	pixels.fill((0,0,0))

def goodMorning():
	for x in range(5,256,5):
		#print(f"x is {x}")
		for y in range(12):
			#print(f"y is {y}")
			pixels[y] = (x,x,0)
			time.sleep(0.1)

def goodNight():
	for x in range(5,256,5):
		brightness = 256 - x
		#print(f"Brightness is {brightness}")
		for y in range(12):
			pixels[y]=(0,0,brightness)
			time.sleep(0.5)
			#print(f"y is {y}")


#goodMorning()
#goodNight()
#goodMorning()
#lightsOff()

def main():
	while True: # thing != "stop":		
		now = datetime.now()
		nowDay = str(now.strftime("%a"))
		nowHour = int(now.strftime("%H"))
		nowMin = int(now.strftime("%M"))
		print(f"It is {nowDay}, at {nowHour}:{nowMin}\n")

		if nowDay in earlyDays:
			print("earlyDays\n")
			timeComp(6,00,20,nowHour,nowMin)
		elif nowDay in weekend:
			timeComp(9,30,45,nowHour,nowMin)
		else:
			print("Today is Thursday")
			timeComp(10,30,45,nowHour,nowMin)

main()
