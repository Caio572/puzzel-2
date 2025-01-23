from scripts.interface import *

root = pygame.display.set_mode([1900,1000]) #1900,1000 ORIGINAL

fase_puzz_2 = Inter_Geral(gp_pos)

loop = True
while loop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            loop = False
            
        elif event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if event.key == pygame.K_ESCAPE:  # Verifica se a tecla ESC foi pressionada
                loop = False

    
        mouse_pos = pygame.mouse.get_pos()
    root.fill((0,0,0))

    if fase_puzz_2.rodando:
        fase_puzz_2.exeucutar(root, event)
    

    pygame.display.flip()

