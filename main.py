import pygame
import sys
import os
import random

pygame.init()
width,height=1000,600
screen=pygame.display.set_mode((width,height))
dirname=os.path.dirname(__file__)
# start_bg=pygame.transform.scale(pygame.image.load(fr"{dirname}\assets\background.jpg"),(width,height))

rock_button=pygame.image.load(fr"{dirname}\assets\rock.png")
paper_button=pygame.image.load(fr"{dirname}\assets\paper.png")
scissor_button=pygame.image.load(fr"{dirname}\assets\scissor.png")

rock_img=pygame.image.load(fr"{dirname}\assets\p_rock.png")
paper_img=pygame.image.load(fr"{dirname}\assets\p_paper.png")
scissor_img=pygame.image.load(fr"{dirname}\assets\p_scissor.png")

rock_img2=pygame.image.load(fr"{dirname}\assets\pc_rock.png")
paper_img2=pygame.image.load(fr"{dirname}\assets\pc_paper.png")
scissor_img2=pygame.image.load(fr"{dirname}\assets\pc_scissors.png")
# rock_rect=rock_img.get_rect()
# paper_img=pygame.image.load(fr"{dirname}\assets\paper.png")
# scissor_img=pygame.image.load(fr"{dirname}\assets\scissor.png")
FPS=pygame.time.Clock()
text=pygame.font.SysFont('comicsans',40)
player_win=0
computer_win=0

player_choice=""

class hand:
    def __init__(self,str,img):
        self.str=str
        self.img=img

p_rock=hand("rock",rock_img)
p_paper=hand("paper",paper_img)
p_scissor=hand("scissor",scissor_img)

pc_rock=hand("Rock",rock_img2)
pc_paper=hand("Paper",paper_img2)
pc_scissor=hand("Scissor",scissor_img2)

pc_hands=[pc_rock,pc_paper,pc_scissor]

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()

            if rock.collidepoint(pos):
                screen.blit(rock_img,(width//2-rock_button.get_width()//2-350,height//2-rock_button.get_width()//2))
                player_choice="Rock"

            if paper.collidepoint(pos):
                screen.blit(paper_img,(width//2-rock_button.get_width()//2-350,height//2-rock_button.get_width()//2))
                player_choice="Paper"

            if scissor.collidepoint(pos):
                screen.blit(scissor_img,(width//2-rock_button.get_width()//2-350,height//2-rock_button.get_width()//2))
                player_choice="Scissor"

            if player_choice!="":
                print(f"player:{player_choice}")
                computer_choice=random.choice(pc_hands)
                print(f"computer:{computer_choice.str}")


                # print(f"Computer:{computer_choice}")
                screen.blit(computer_choice.img,(width//2-scissor_button.get_width()//2+350,height//2-rock_button.get_width()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                # pygame.draw.rect(screen,(0,0,0),(0,height-50,width,height))
                screen.fill((0,0,0))

            if player_choice=="Rock" and computer_choice.str=="Scissor" or player_choice=="Paper" and computer_choice.str=="Rock" or player_choice=="Scissor" and computer_choice.str=="Paper":
                player_win+=1
                pygame.display.update()

            if computer_choice.str=="Rock" and player_choice=="Scissor" or computer_choice.str=="Paper" and player_choice=="Rock" or computer_choice.str=="Scissor" and player_choice=="Paper":
                computer_win+=1
                pygame.display.update()

            # if player_choice=="Paper" and computer_choice.str=="Rock":
            #     player_win+=1
            #     pygame.display.update()


            # if player_choice=="Scissor" and computer_choice.str=="Paper":
            #     player_win+=1
            #     pygame.display.update()
                
            if player_choice==computer_choice.str:
                pass

            # else:
            #     computer_win+=1

            # if player_choice==computer_choice.str:
            #     pass

            

    keys=pygame.key.get_pressed()
    # start_screen=screen.blit(start_bg,(0,0))
    # screen.fill((0,0,0))

    score_text=text.render(f"{player_win}:{computer_win}",1,(255,255,255))
    screen.blit(score_text,(width//2-score_text.get_width()//2,10))

    rock=screen.blit(rock_button,(width//2-rock_button.get_width()//2-350,height-150))
    paper=screen.blit(paper_button,(width//2-paper_button.get_width()//2,height-150))
    scissor=screen.blit(scissor_button,(width//2-scissor_button.get_width()//2+350,height-150))
    
    border=pygame.draw.rect(screen,(255,255,255),(width//2,50,10,height-200))
    # pygame.display.flip()
    pygame.display.update()
    FPS.tick(120)