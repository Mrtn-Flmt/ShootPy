import pygame
from game import Game
from player import Player

pygame.init()

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080,720))

# Importer de charger l'arriere plan 
background = pygame.image.load('assets/bg.jpg')

player = Player()
# Charger le jeu
game = Game()

running = True



# Boucle tant que cette condition est vrai
while running:

    # Appliquer l'arriere plan 
    screen.blit(background, (0,-150))

    # Appliquer l'image de mon joueur
    screen.blit(game.player.image, player.rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # Que l'evenement est fermeture du jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("à bientot !")
