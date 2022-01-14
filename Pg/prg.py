from pygame import *


window = display.set_mode((1024, 768))
display.set_caption("Пингпонг")
background = transform.scale(image.load("bg.jpg"), (1024, 768))
run = True
finish = False
fps = 144
clock = time.Clock() 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, model_size_x, model_size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (model_size_x, model_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = model_size_x
        self.size_y = model_size_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_s] and self.rect.y < 750:
            self.rect.y = self.rect.y + self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 750:
            self.rect.y = self.rect.y + self.speed
#class Circle(GameSprite):
    # def update(self):
    #     if self.rect.y != 20 and self.rect.x != 20 and self.rect.y != 750 and self.rect.x != 1000 and self.rect.y > 20 and self.rect.x > 20 and self.rect.y < 750 and self.rect.x < 1000:
    #         self.rect.y = self.rect.y - self.speed
    #         self.rect.x = self.rect.x - self.speed           
    #     elif self.rect.y == 20:
    #         self.rect.y = self.rect.y + self.speed
    #     elif self.rect.y == 750:
    #         self.rect.y = self.rect.y - self.speed
    #     elif self.rect.x == 1000:
    #         self.rect.x = self.rect.x - self.speed
    #     elif self.rect.x == 20:
    #         self.rect.x = self.rect.x + self.speed

player1 = Player1("playerimg.jpg", 30, 400, 30, 130, 4)
player2 = Player2("playerimg.jpg", 970, 400, 30, 130, 4)

ball = GameSprite("Ball.png", 512, 384, 20, 20, 4)
speed_x = 4
speed_y = 4
font.init()
game_font1 = font.SysFont("Arial", 150)
start = True

while run:


    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if start == True:
            window.blit(background,(0,0)) 
            player1.reset()
            player1.update()
            player2.reset()
            player2.update()
            ball.reset()
            ball.update()
            display.update() 
            clock.tick(fps)
            time.delay(5000)
            start = False
            
        if ball.rect.y > 768 - 20 or  ball.rect.y < 0:
            speed_y  = speed_y * -1  
        if ball.rect.x > 1024 - 1:
            lose2 = game_font1.render(
        "Второй игрок проиграл", True, (255, 215, 0)
        )
        if ball.rect.x < 0 + 1:
            lose1 = game_font1.render(
        "Первый игрок проиграл", True, (255, 215, 0)
        )
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x  = speed_x * -1 
        window.blit(background,(0,0))    
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
 
    display.update()    
    clock.tick(fps)


