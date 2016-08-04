import pygame


#   Clase para la creacion del fondo del juego
class Fondo(pygame.sprite.Sprite):
    def __init__(self): #   Constructor del fondo
        self.imagen=pygame.image.load("fondo_1.gif")
        self.rect=self.imagen.get_rect()

    def actualizar(self,pantalla,movX): #  Metodo para actualizar la pantalla
        self.rect.move_ip(-movX,0)
        pantalla.blit(self.imagen,self.rect)


#clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self): #   Constructor para el movimiento del jugador
        self.imagen1=pygame.image.load("derecha_1.gif")
        self.imagen2=pygame.image.load("derecha_2.gif")
        self.imagen3=pygame.image.load("derecha_3.gif")
        self.imagen4=pygame.image.load("izquierda_1.gif")
        self.imagen5=pygame.image.load("izquierda_2.gif")
        self.imagen6=pygame.image.load("izquierda_3.gif")
         
        # creo la lista de las imaganes el primer indice es la orientacion y el segundo la imagen self.imagenes[self.orientacion][self.imagen_actual]      
        self.imagenes=[[self.imagen1, self.imagen2, self.imagen3],[self.imagen4,self.imagen5, self.imagen6]]
        
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual][0]
        self.rect=self.imagen.get_rect()
        self.rect.left, self.rect.top=(10,420) # Posicion inicial del jugador
        
        #variable par ver si se esta moviendo
        self.estamoviendo=False
        
        # orientacion 0 si va a la derecha y 1 si va la izquierda
        self.orientacion=0


    #   Funcion para mover al jugador
    def mover(self,vx,vy):   
        self.rect.move_ip(vx,vy)


       
    #   Funcion para actualizar la posicion del jugador
    def actualizar(self,superficie,vx,vy,t, x, y):  
        
        # si el jugador no se mueve self.estamoviendo=FALSE
        if (vx,vy)==(0,0): self.estamoviendo=False
        else:self.estamoviendo=True # si se mueve que este en TRUE
        
        # con estas 2 lineas cambio la orientacion
        if vx>0: self.orientacion=0 
        elif vx<0: self.orientacion=1
        
        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if t==1 and self.estamoviendo:
            self.siguiente_Imagen()
            
        # mover el rectangulo    
        if (x<900 and x>0)and (y>420 and y<600):
            self.mover(vx, vy)
        
        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)
        


    #funcion que se encarga de cambiar de imagen    
    def siguiente_Imagen(self):
        self.imagen_actual+=1
        if self.imagen_actual>(len(self.imagenes)-1):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0          
        

#   Funcion principal
def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((1000,600))
    fondo=Fondo()
    salir=False
    reloj= pygame.time.Clock()
    movimiento_X, movimiento_Y =0,0
    velocidad_X =5
    velocidad_Y=20
    limite_Pantalla_X=0
    limite_Jugador_X=10
    limite_Jugador_Y=420

    player1=Player() # Instanciamos un objeto de clase  Player
    
    #auxiliares para el movimiento
    izq_apretada,der_apretada,arriba_apretada,abajo_apretada=False,False,False,False
    t=0
    
    while salir!=True:#BUCLE  PRINCIPAL
        #control de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir=True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    izq_apretada=True
                    movimiento_X=-velocidad_X
                    limite_Jugador_X -= movimiento_X

                if evento.key == pygame.K_RIGHT:
                    der_apretada=True
                    movimiento_X=velocidad_X
                    limite_Jugador_X += movimiento_X

                if evento.key== pygame.K_UP:
                    arriba_apretada=True
                    movimiento_Y=-velocidad_Y
                    limite_Jugador_Y -=movimiento_Y

                if evento.key == pygame.K_DOWN:
                    abajo_apretada=True
                    movimiento_Y=velocidad_Y
                    limite_Jugador_Y +=movimiento_Y

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    izq_apretada=False
                    if der_apretada:movimiento_X=velocidad_X
                    else:movimiento_X=0
                if evento.key == pygame.K_RIGHT:
                    der_apretada=False
                    if izq_apretada:movimiento_X=-velocidad_X
                    else:movimiento_X=0
                if evento.key== pygame.K_UP:
                	arriba_apretada=False
                	if abajo_apretada:movimiento_Y=velocidad_Y
                	else:movimiento_Y=-0
                if evento.key == pygame.K_DOWN:
                	abajo_apretada=False
                	if arriba_apretada:movimiento_Y=-velocidad_Y
                	else:movimiento_Y=0 
                    
                         
        reloj.tick(25)# 25 fps
        
        #auxiliar de la animacion
        t+=1
        if t>1:
            t=0            
        
        pantalla.fill((0,0,0))
        #   Actualizar fondo
        fondo.actualizar(pantalla, movimiento_X)
        # actualizar jugador
        player1.actualizar(pantalla,movimiento_X,movimiento_Y,t, limite_Jugador_X, limite_Jugador_Y)
        print limite_Jugador_X , limite_Jugador_Y
        #actualizar pantalla
        pygame.display.update()

                
    pygame.quit()

main()