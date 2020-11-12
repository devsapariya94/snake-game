import pygame
x=pygame.init()
import random
win=pygame.display.set_mode((900,600))


font=pygame.font.SysFont(None,55)
def text(text, color, x,y):
    stext=font.render(text, True, color)
    win.blit(stext,[x,y])
def plot(win, color,snlist,ss):
    for x,y in snlist:
        pygame.draw.rect(win, color,[x, y, ss, ss])
    

def game():
    white=(255,255,255)
    red=(255,0,0)
    black=(0,0,0)
    clock=pygame.time.Clock()
    sx=20
    sy=60
    ss=32
    fps=60
    svx=0
    svy=0
    fx=random.randint(10,860)
    fy=random.randint(50,520)

    
    pygame.display.set_caption("Snake")
    pygame.display.update()
    exit_game=False
    game_over=False
    score=0
    speed=5
    snlist=[]
    snlen=1
    with open("highscore.txt","r")as f:
        highscore=f.read()
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    svx=speed
                    svy=0
                if event.key==pygame.K_LEFT:
                    svx=-speed
                    svy=0
                if event.key==pygame.K_DOWN:
                    svy=speed
                    svx=0
                if event.key==pygame.K_UP:
                    svy=-speed
                    svx=0
            

        sx=sx+svx
        sy=sy+svy

        if abs(sx-fx)<18 and abs(sy-fy)<18:
            score+=10
        
            fx=random.randint(10,860)
            fy=random.randint(50,520)
            snlen+=5
            if score> int(highscore):
                highscore=score
        win.fill(black)
        pygame.draw.rect(win, white,[10, 50, 880,500 ])
        text("score: "+str(score)+"  High Score: "+str(highscore), red , 5,5)
        
        plot(win, black,snlist,ss)
        head=[]
        head.append(sx)
        head.append(sy)
        snlist.append(head)
        if len(snlist)>snlen:
            del(snlist[0])

        eye=snlist[-1]
        pygame.draw.circle(win, (151,151,151),[eye[0]+16, eye[1]+16], 16)
     
        if head in snlist[:-1]:
            game_over=True
        if sx<9 or sx>861 or sy<49 or sy>521:
            game_over=True
        pygame.draw.rect(win, red,[fx, fy, ss, ss])
        
        if game_over==True:
            win.fill(black)
            text('game over',white,10,10)
            text("your score: "+str(score), red , 50,50)
            with open("highscore.txt","w")as f:
                f.write(str(highscore))
            time.sleep(2)    
            for event in pygame.event.get():
                    
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    game()
                   
        pygame.display.update()
    
        clock.tick(fps)
    pygame.quit()
game()
