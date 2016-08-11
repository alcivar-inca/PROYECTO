import pygame

pygame.init()
pantalla=pygame.display.set_mode((1000,600))
reloj=pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 20, True)
texto_Puntaje=fuente.render("Puntaje: ", True, (0,0,0))
texto_Tiempo=fuente.render("Tiempo: ", True, (0,0,0))
salir=False


while salir != True:
	for evento in pygame.event.get():
		if evento.type==pygame.QUIT:
			salir=True
	
	reloj.tick(15)
	segundos=pygame.time.get_ticks()/1000
	contador=fuente.render(str(segundos), True, (0,0,0))


	pantalla.fill((255, 255, 255))
	pantalla.blit(texto_Puntaje, (10, 10))
	pantalla.blit(texto_Tiempo, (850, 10))
	pantalla.blit(contador, (940,10))
	pygame.display.update()
pygame.quit()