import pygame
from pygame.math import Vector2

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def draw(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.reset_game()

    def reset_game(self):
        self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.snake.direction = Vector2(0,0)
        self.pos= Vector2(10,10)
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(0,0,255),snake_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:]



class FRUIT:
    def __init__(self):
        self.pos= Vector2(10,10)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)


pygame.init()

cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            elif event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
            elif event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)



    screen.fill((175,215,70))
    main_game.draw()


    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()