import pygame
import time


def run():
    pygame.init()
    screen = pygame.display.set_mode((300,100))
    pygame.display.set_caption('Timer')
    
    time1 = time.time()
    sec = 0
    minutes = 0
    hours = 0
    f1 = pygame.font.Font(None,70)
    while True:
        pygame.draw.rect(screen,(239,228,214),(0,0,600,600))
        if sec < 10:
            sec_pr = '0'+str(sec)
        else:
            sec_pr = sec

        if minutes < 10:
            minutes_pr = '0'+str(minutes)
        else:
            minutes_pr = minutes

        if hours < 10:
            hours_pr = '0'+str(hours)
        else:
            hours_pr = hours
                
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sec = 0
                    minutes = 0
                    hours = 0
                    
        text = str(hours_pr)+":"+str(minutes_pr)+":"+str(sec_pr)
        render = f1.render(text,1,(215,183,170))        
        screen.blit(render,(20,20))
        if time.time()- time1 > 1:
                sec += 1
                if sec == 60:
                        minutes += 1
                        sec = 0
                        if minutes == 60:
                                hours += 1
                                minutes = 0
                time1 = time.time()
        pygame.display.flip()
run()