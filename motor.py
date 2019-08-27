import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(07, GPIO.OUT)
pwm=GPIO.PWM(07, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(07, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(07, False)
	pwm.ChangeDutyCycle(0)

if __name__== "__main__":
	counter = 1
	down = False
	angle = 0
	while(counter <= 6):
		#if(angle <= 180 ):
			#if(angle == 180):
			#	down = true
			#else if(angle < 180 and down = false):
			#	angle -= 60
			#else:
			#	angle += 60
		
		#else if(angle == 180 and down == true):
		#	angle-= 60	
		if(angle == 180):
			down = True
		elif(angle == 0):
			down = False
		if(down == False):
			angle += 60
		else:
			angle -= 60		 
		SetAngle(angle)
		counter +=1
	pwm.stop()
	GPIO.cleanup()
	
