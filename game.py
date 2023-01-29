from ast import Pass
import string
from turtle import Shape
import pygame 
import sys

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (57, 145, 95)
FONT = pygame.font.Font('font/Pixeltype.ttf',30)
SHOP_TEXT_COLOR = (0, 255,0)


#user stats
user_phys = 0
user_int = 0
user_tech = 0
user_agl = 0
user_str = 0

user_cash = 300
user_wins = 0
day = 0

#upgrade cost/value
phys_buy = 10
int_buy = 10
tech_buy = 10
agl_buy = 10
str_buy = 10

phys_sell = 0
int_sell = 0
tech_sell = 0
agl_sell = 0
str_sell = 0






screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False
SHOP_BACKGROUND = pygame.image.load('shopBackground.png')
SHOP_BACKGROUND = pygame.transform.scale(SHOP_BACKGROUND, (800,600))


#draw shop functions
def draw_shop():
    screen.fill(BACKGROUND_COLOR) 
    screen.blit(SHOP_BACKGROUND, (0,0))

    for y in range(1, 6):
        pygame.draw.rect(screen, (255,0,0), (60, y*100, 180, 60)) #label box
        pygame.draw.rect(screen, (255,0,0), (260, y*100, 60, 60)) #buy box
        pygame.draw.rect(screen, (255,0,0), (340, y*100, 60, 60)) #SELL BOX

    #text label for stat bars and buy/sell boxes
    phys_text = FONT.render('Physicality', False, (0, 255, 233))
    screen.blit(phys_text, (80,120))
    phys_num = FONT.render(str(user_phys), False, (0, 255, 0))
    screen.blit(phys_num, (210,120))
    buy_text = FONT.render('Buy $' + str(phys_buy), False, (0, 255, 0))
    screen.blit(buy_text, (280,120))
    sell_text = FONT.render('Sell $' + str(phys_sell), False, (0, 255, 0))
    screen.blit(sell_text, (350,120))

    #text label for cash/wins/day
    cash_text = FONT.render('Cash: $' + str(user_cash), False, (0, 255, 0))
    screen.blit(cash_text, (680,20))
    wins_text = FONT.render('Wins: ' + str(user_wins), False, (0, 255, 0))
    screen.blit(wins_text, (680,40))
    days_text = FONT.render('Day: ' + str(day), False, (0, 255, 0))
    screen.blit(days_text, (680,60))





while not game_over:
    
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
        
    draw_shop()           

    pygame.display.update()
