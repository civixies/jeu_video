import pygame
from game import Game
pygame.init()


# Fenetre
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080,650))

# arriere plan
background = pygame.image.load('assets/bg.jpg')
#charger notre jeu
game = Game()

running = True

# boucle
while running:
    # arriere plan du jeu
    screen.blit(background, (0,-200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    #récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #appliquer l'image du groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l'esnsemble des images de mon groupe de monstre
    game.all_monsters.draw(screen)

    #a tester une fois la classe complete
    #screen.blit(player.image, Player.rect(self))

    # vérifier si le joueur souhaite aller à gauche ou à droite.
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme
    for event in pygame.event.get():
        #L'evenement est fermture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermture du jeu")

        # detecter si un joueur lache du touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



# reprendre à la vidéo 4: 11 minutes et 20 secondes