
# Dig for gold
# Based on Whack-a-mole game using pygame by Kimberly Todd

from pygame import *
from pygame.sprite import *
from random import *


       

bgcolor = (40, 40, 60)    #Color taken from background of sprite

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        p =pygame.image.load("player.png")
        self.image = pygame.transform.scale(p, (75,75))
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self, x_pos, y_pos):

        self.rect.center = (x_pos,y_pos)

    
class Ice(Player):
    def __init__(self, row, col):
        Sprite.__init__(self)
        ice = image.load('ice.png').convert()
        self.image = pygame.transform.scale(ice, (80,80))
        self.rect = self.image.get_rect()
        self.rect.center = (row, col)
class Ball(Player):
     def __init__(self):
        Sprite.__init__(self)
        p =pygame.image.load("ball.png")
        self.image = pygame.transform.scale(p, (50,50))
        self.rect = self.image.get_rect(center=(-20,-20))

     def hit(self, target):
        return self.rect.colliderect(target)


#######################################################################################
init()

screen = display.set_mode((900, 700))
display.set_caption('Climb through the Ice')

# hide the mouse cursor so we only see shovel
mouse.set_visible(False)


f = font.Font(None, 25)
DELAY = 1000;
##### Constructors ######
player = Player()
ball = Ball()
ice = []

screen_rect = screen.get_rect()
rows = range(300,850,100)
cols = range(100,650,100)
for i in rows:
    for j in cols:
        ice.append(Ice(i, j))



# creates a group of sprites so all can be updated at once aka every time i mention sprites, i'm talking about gold and shovel. 
sprites = RenderPlain(player, ice,ball)

x_pos=30
y_pos=30
repeat=True
hits=0
time.set_timer(USEREVENT + 1, DELAY)
# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

         
    elif e.type == KEYDOWN: 
    
      
        if e.key == K_UP:
            y_pos -= 20
        if e.key == K_DOWN:
            y_pos += 20
            
        player.move(x_pos, y_pos)
        
       
        if e.key == K_SPACE: 
            x = x_pos
            

            while repeat == True:
                ball.move(x, y_pos)
                sprites.update()
                sprites.draw(screen)
                pygame.display.update()
                screen.fill(bgcolor)
                x+=20
                if x > screen_rect.right:
                    mixer.Sound("splash.wav").play()
                    ball.move(-15,-15)
                    break

                for i in ice:
                    if ball.hit(i): 
                        repeat = False
                        i.kill()
                        ball.move(-15,-15)
                        i.move(0,0)
                        mixer.Sound("hit.wav").play()
                        hits+=1
                        break
                
                    
            
            repeat = True
            time.set_timer(USEREVENT + 1, DELAY)      
                
    # elif e.type == USEREVENT +1:



    # refill background color so that we can paint sprites in new locations
           # draw text to screen.  Can you move it?
    screen.fill(bgcolor)
    t = f.render("Score: " + str(hits), False, (255,255,255))
    screen.blit(t, (320, 0))
    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    pygame.display.update()





#### commit wednesday morning