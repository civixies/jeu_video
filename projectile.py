import pygame

#creer la notion de projectile

class Projectile(pygame.sprite.Sprite):
    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.orgin_image = self.image
        self.angle = 0
    
    def rotate(self):
        #Tourner le projectile
        self.angle += 20
        self.image = pygame.transform.rotozoom(self.orgin_image,self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #vérifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()