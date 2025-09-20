# [] - Criar uma tela 

import pygame  # Importa a biblioteca Pygame


#Classes
# Player

class Player(pygame.sprite.Sprite):
    def __init__(self,  pos):
        super().__init__()
        #carregar imagem do player
        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 300
    
    def update (self, dt, keys, screen):
        #Movimento

        if keys[pygame.K_w]:
            self.rect.y -= self.speed*dt
        if keys[pygame.K_s]:
            self.rect.y += self.speed*dt
        if keys[pygame.K_a]:
            self.rect.x -= self.speed*dt
        if keys[pygame.K_d]:
            self.rect.x += self.speed*dt

        # Não sair da tela
        if self.rect.left <0:
            self.rect.left = 0
        
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()

        if self.rect.top <0:
            self.rect.top = 0

        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()






# --- Setup inicial ---
pygame.init()  # Inicializa todos os módulos do pygame

#Variaveis

screen = pygame.display.set_mode((720, 640)) # Cria a janela do jogo com largura=720 e altura=640
pygame.display.set_caption("B-Merchant")

chao_rect = pygame.Rect(0, screen.get_height() - 50, screen.get_width(), 50)
clock = pygame.time.Clock()  # Cria um relógio para controlar o FPS (frames por segundo)
running = True # Variável que controla o loop principal
dt = 0


#Criar grupo de sprites
player = Player((screen.get_width() / 2, screen.get_height() / 2))
all_sprites = pygame.sprite.Group(player)
icone = pygame.image.load('money.png')
background = pygame.image.load('Background.png')
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
pygame.display.set_icon(icone)

# --- Loop principal do jogo ---
while running:
    # 1. Verificação de eventos (teclado, mouse, fechar janela, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o jogador clicar no "X"
            running = False            # Fecha o loop do jogo

    # 2. Atualização do estado do jogo / desenho na tela
    screen.fill((0, 0, 0))  # Pinta a tela inteira com alguma cor
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    

    #Mapeamento das teclas
    keys = pygame.key.get_pressed()
    all_sprites.update(dt, keys, screen)



    

    #Mapa

    #Chão
    pygame.draw.rect(screen, (100, 50, 0), chao_rect)

    if player.rect.bottom > chao_rect.top:
        player.rect.bottom = chao_rect.top


    

    # 3. Atualização da tela
    pygame.display.flip()  # Mostra tudo o que foi desenhado

    # 4. Controla a taxa de atualização (máx. 60 FPS)
    dt = clock.tick(60) / 1000

# --- Encerramento ---
pygame.quit()  # Fecha a janela e finaliza o pygame



