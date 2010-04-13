import time
import pygame
#pygame.mixer.init() 
#pygame.mixer.music.load('korn.wav')
def acti():
	pygame.mixer.init() 
	pygame.mixer.music.load('track 6.wav')
	a = raw_input('presione play(enter) : ')
	if a=='':
		repro()
		quieres()
	else:
		print 'no jodas'
def repro():
	pygame.mixer.music.play()
	#time.sleep(1)

def quieres():
	d=raw_input('sigue tocando : ')
	if d=='si':
		
		vamos()
	else:
		termina()
def termina():
	pygame.mixer.music.stop()
	print 'termina el sonido pero sigues jugando jijij'
	vamos()
			
def vamos():
	h=raw_input('presiona enter para terminar : ')
acti()
