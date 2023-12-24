import random

import pygame
import threading

def bg_music():
    pygame.init()
    pygame.mixer.music.load('price-of-freedom-33106.mp3')
    pygame.mixer.music.play()
x = threading.Thread(target=bg_music)
x.start()



class snake:
    def __init__(self,screen_width,screen_height,block_size,food):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size

        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.snake_head = [screen_width/2,screen_height/2]
        self.snake_body = [[screen_width/2, screen_height/2], [screen_width/2-block_size, screen_height/2], [screen_width/2-(2*block_size), screen_height/2]]
        self.food=food

    def check_if_snake_eats(self):
        if self.snake_head[0] == self.food.x_pos and self.snake_head[1] == self.food.y_pos:
            luck = random.randint(1,10)


            self.snake_body.append([self.snake_head[0],self.snake_body[1]])
            self.food.place_food()
            return True
        else:
            return False

    def change_direction (self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                self.change_to = 'RIGHT'
            if event.key == pygame.K_UP:
                self.change_to = 'UP'
            if event.key == pygame.K_DOWN:
                self.change_to = 'DOWN'

    def move(self):
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

        if self.direction == 'LEFT':
            self.snake_head[0] -= self.block_size

        if self.direction == 'RIGHT':
            self.snake_head[0] += self.block_size

        if self.direction == 'UP':
            self.snake_head[1] -= self.block_size

        if self.direction == 'DOWN':
            self.snake_head[1] += self.block_size

    def check_collision(self):
        if self.snake_head[0] < 0 or self.snake_head[0] >= self.screen_width or self.snake_head[1] < 0 or self.snake_head[1] >= self.screen_height:
            return True

    def update_body(self):
        self.snake_body.insert(0,list(self.snake_head))
        self.snake_body.pop()

class Food:


    def __init__ (self,screen_width,screen_height,block_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size

        self.x_pos=random.randrange(0,screen_width-block_size,block_size)
        self.y_pos=random.randrange(0,screen_height-block_size,block_size)
    def get_x_food_pos(self):
            return self.x_pos

    def get_y_food_pos(self):
            return self.y_pos

    def place_food(self):
            self.x_pos = random.randrange(0, screen_width - block_size, block_size)
            self.y_pos = random.randrange(0, screen_height - block_size, block_size)
class Game:
    def __init__(self, screen_width, screen_height, block_size):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.snake_speed = snake_speed
        self.food=Food(screen_width,screen_height,block_size)
        self.snake = snake(screen_width,screen_height,block_size,self.food)
        self.score = 0
        self.false = False
        self.game_over = self.false

        pygame.init()
        screen_width = 640
        screen_height = 480
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Snake game')
        self.clock = pygame.time.Clock()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.lime = (0, 255, 0)


        self.font = pygame.font.SysFont(None, 25)

    def display_score(self):
        score_text = self.font.render('Score: ' + str(self.score), True, self.white)
        self.screen.blit(score_text, [0, 0])

    def draw_screen(self):
        self.screen.fill(self.black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
        for block in self.snake.snake_body:
            pygame.draw.rect(self.screen, self.lime, [block[0], block[1], block_size, block_size])

        pygame.draw.rect(self.screen,self.red,[self.food.x_pos,self.food.y_pos,block_size,block_size])

        self.display_score()
        pygame.display.update()

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                else:
                    self.snake.change_direction(event)
            self.snake.move()

            self.snake.update_body()
            self.draw_screen()
            self.clock.tick(self.snake_speed)

            if self.snake.check_if_snake_eats():
                self.score += 10

                
            if self.snake.check_collision():
                self.game_over = True

        pygame.quit()
        quit()








screen_width = 640
screen_height = 480
block_size = 10
snake_speed = 15

game = Game(screen_width,screen_height,block_size)
game.run()









