# [] - Criar uma tela 

import pygame  # Importa a biblioteca Pygame

# --- Setup inicial ---
pygame.init()  # Inicializa todos os módulos do pygame

# Cria a janela do jogo com largura=720 e altura=640
screen = pygame.display.set_mode((720, 640))

# Cria um relógio para controlar o FPS (frames por segundo)
clock = pygame.time.Clock()

# Variável que controla o loop principal
running = True

# --- Loop principal do jogo ---
while running:
    # 1. Verificação de eventos (teclado, mouse, fechar janela, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o jogador clicar no "X"
            running = False            # Fecha o loop do jogo

    # 2. Atualização do estado do jogo / desenho na tela
    screen.fill((128, 0, 128))  # Pinta a tela inteira de roxo (RGB)

    # 3. Atualização da tela
    pygame.display.flip()  # Mostra tudo o que foi desenhado

    # 4. Controla a taxa de atualização (máx. 60 FPS)
    clock.tick(60)

# --- Encerramento ---
pygame.quit()  # Fecha a janela e finaliza o pygame



