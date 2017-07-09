
import pygame
from pygame.locals import *
import sys

pygame.init()
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
dark_blue=(0,0,140)
dark_purple=(140,0,100)
white=(255,255,255)
black=(0,0,0)

human_creator = False
HumanList=[]
walls_creator = False
wallsList=[]
polygon=[]
class MainWindow:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.display=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Caption")
        self.display.fill(white)


class Leiste:
    def __init__(self, breite, farbe):
        self.breite=breite
        self.farbe=farbe
        pygame.draw.rect(mainWindow.display, farbe, (mainWindow.width-self.breite,0,mainWindow.width,mainWindow.height))
        pygame.display.update()
    def position(self):
        return mainWindow.width-self.breite,0

class Button:
    def __init__(self, msg, positionX, positionY, farbe=green, breite=100, hoehe=50 ):
        self.msg=msg
        self.positionX = positionX
        self.positionY = positionY
        self.farbe = farbe
        self.breite = breite
        self.hoehe = hoehe
        self.msg=msg
        font = pygame.font.Font('freesansbold.ttf', 14)
        self.text = font.render(self.msg, True, black)

        ###Schalter zum Erstellen von Humans
    def human(self):
        pygame.event.get()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.positionX < mouse[0] < self.positionX+self.breite and self.positionY < mouse[1] < self.positionY+self.hoehe:
            pygame.draw.rect(mainWindow.display, self.farbe, (self.positionX, self.positionY, self.breite, self.hoehe))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click[0] == 1:
                    global human_creator
                    if human_creator==True:
                        print("Human Erstellen ist aus")
                        human_creator=False
                    else:

                        print("Human Erstellen")
                        human_creator=True

        else:
            pygame.draw.rect(mainWindow.display, self.farbe, (self.positionX, self.positionY, self.breite, self.hoehe))

        ##FONT
        mainWindow.display.blit(self.text, (self.positionX+self.breite//2-self.text.get_width()//2 , self.positionY+self.hoehe//2- self.text.get_height()//2))

        ###Human mit click erstellen
        if event.type == pygame.MOUSEBUTTONDOWN and human_creator==True:
            if click[0]==1:

                global HumanList
                if mouse[0]<breite-mainLeiste.breite:
                    HumanList+=[(mouse)]
                    pygame.draw.circle(mainWindow.display, black, (mouse), 3, 0)





    def walls(self):
        pygame.event.get()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.positionX < mouse[0] < self.positionX+self.breite and self.positionY < mouse[1] < self.positionY+self.hoehe:
            pygame.draw.rect(mainWindow.display, self.farbe, (self.positionX, self.positionY, self.breite, self.hoehe))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click[0] == 1:
                    global walls_creator
                    if walls_creator==True:
                        print("Waende Erstellen ist aus")
                        walls_creator=False
                    else:

                        print("Waende Erstellen")
                        walls_creator=True
        else:
            pygame.draw.rect(mainWindow.display, self.farbe,(self.positionX, self.positionY, self.breite, self.hoehe))

        ##FONT
        mainWindow.display.blit(self.text, (self.positionX + self.breite // 2 - self.text.get_width() // 2, self.positionY + self.hoehe // 2 - self.text.get_height() // 2))

        #### waende erstellen mit klick

        if event.type == pygame.MOUSEBUTTONDOWN and walls_creator==True and click[0]==1:
            global wallsList
            global polygon
            if mouse[0]<breite-mainLeiste.breite:

                polygon+=[(mouse)]
                pygame.draw.circle(mainWindow.display, black, (mouse), 1, 0)

        elif event.type == pygame.MOUSEBUTTONDOWN and walls_creator == True and click[2]==1:
            global wallsList
            global polygon
            if mouse[0] < breite - mainLeiste.breite:
                wallsList+=[(polygon)]
                pygame.draw.polygon(mainWindow.display, black, polygon, 0)
                polygon=[]






#Frames etc
clock = pygame.time.Clock()


#objekte werdern erzeugt
breite=1000
hoehe=800
mainWindow = MainWindow(breite,hoehe)
mainLeiste = Leiste(200,dark_blue)
button1= Button("Human",850,100,dark_purple)
button2=Button("Walls",850,250, dark_purple )
mainWindow
mainLeiste
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        button1.human()
        button2.walls()



    pygame.display.update()
    
