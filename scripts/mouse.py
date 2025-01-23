import pygame

class Mouse:
    def __init__(self):
        self.click = False

    def atualizar(self, event):
        # Atualiza a posição do mouse e retângulo baseado nela
        self.mouse_pos = pygame.mouse.get_pos()
        self.x, self.y = 0,0
        self.mouse = pygame.Rect(self.x, self.y, 1, 1)
        

        self.Interacao(event)
        


    def Interacao(self, event):
        
        # Verifica se o mouse colide com uma área e se houve clique
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self.x, self.y = self.mouse_pos
            self.mouse = pygame.Rect(self.x, self.y, 1, 1)
            print(self.x, self.y)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            self.click = False
            
        
        