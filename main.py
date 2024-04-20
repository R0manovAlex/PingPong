import pygame




pygame.init()

background = (162, 118, 228)
win_width = 600
win_height = 600
window = pygame.display.set_mode((win_height, win_width))




pygame.display.update()
pygame.display.set_caption('PingPong')


game_over = False
x1 = 300 
y1 = 300 
x1_change = 0
clock = pygame.time.Clock()

if event.key == pygame.K_LEFT:
               x1_change = -10 
               y1_change = 0

while not game_over:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           game_over = True
       if event.type == pygame.KEYDOWN:




pygame.display.update()
clock.tick(60)





pygame.quit()
quit()
