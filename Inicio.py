import pygame
pygame.init()

ancho = 1000
alto = 600

#   Clase para graficar un rectangulo que sigue al cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,2,2)

    def actualizar (self):
        self.left,self.top=pygame.mouse.get_pos()

        
#   Clase para crear un sprite de la imagen inicioa juego
class Boton (pygame.sprite.Sprite):
    def __init__(self, imagen, x=200, y=200): #    Constructor
        self.boton_Normal= imagen
        ancho, alto = self.boton_Normal.get_size()
        self.boton_Seleccion=pygame.transform.scale(self.boton_Normal, (int(ancho*1.1), int(alto*1.1)))
        self.boton_actual=self.boton_Normal

        self.rect=self.boton_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)


    def actualizar (self, pantalla, cursor): #  Funcion para verificar si existe colicion entre el rectangulo que sigue al mouse y el boyon iniciar
        if cursor.colliderect(self.rect):
            self.boton_actual=self.boton_Seleccion
        else:
            self.boton_actual=self.boton_Normal
        pantalla.blit(self.boton_actual, self.rect) 



#   Clase principal que contine el juego
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("EPN ADVENTURE")
    reloj=pygame.time.Clock()
    fondo_inicio = pygame.image.load("fondo_inicio.jpg")
    boton_Iniciar=pygame.image.load("jugar.png")
    boton1=Boton(boton_Iniciar, 400, 200)
    cursor1= Cursor()

    sonido_1 = pygame.mixer.music.load("musica_Inicio.mp3") #sonido de fondo de juego primer nivel 
    sonido_1 = pygame.mixer.music.play(1)


    salir=False
    while salir!=True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir=True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    sonido_1=pygame.mixer.music.stop()


        reloj.tick(20)
        pantalla.fill((0,0,0))
        pantalla.blit(fondo_inicio, (0, 0))
        cursor1.actualizar()
        boton1.actualizar(pantalla,cursor1)
        pygame.display.update() 


    pygame.display.update()

main()

