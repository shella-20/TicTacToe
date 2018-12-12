import pygame, sys, os
import random, time
from tkinter import *
import os

# displaying the game
h_display = 400
v_display = 400
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((h_display, v_display))
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 128)
red = (255, 64, 64)

class Game:
    def __init__(self):
        self.x = "X"
        self.o = "O"
        self.pointX = 0
        self.pointY = 0
        self.tieCount = 0
        self.turn = self.x
        self.display = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.displayCo = [(100, 100), (200, 100), (300, 100), (100, 200), (200, 200), (300, 200), (100, 300), (200, 300), (300, 300)]

    # making a grid
    def drawLine(self):
        for i in range(50, 450, 100):
            pygame.draw.line(gameDisplay, black, (i, 50), (i, 350), 2)
            pygame.draw.line(gameDisplay, black, (50, i), (350, i), 2)

    # making a x and o text
    def displayText(self, text, place):
        font = pygame.font.SysFont("Arial", 100, True)
        text_ = font.render(text, True, black)
        rect = text_.get_rect()
        rect.center = place
        gameDisplay.blit(text_, rect)

    # change turn algorithm for x player and o player
    def check(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for i in range(50, 350, 100):
            if mouse[0] > i and mouse[1] > 50 and mouse[0] < i+100 and mouse[1] < 150:
                pygame.draw.rect(gameDisplay, white, [i, 50, 100, 100])
                if click[0] == 1:
                    if mouse[0] >= 50 and mouse[1] >= 50 and mouse[0] <= 150 and mouse[1] <= 150:
                        if self.display[0] != self.x and self.display[0] != self.o:
                            self.display[0] = self.turn
                            self.turnChange()
                    if mouse[0] >= 150 and mouse[1] >= 50 and mouse[0] <= 250 and mouse[1] <= 150:
                        if self.display[1] != self.x and self.display[1] != self.o:
                            self.display[1] = self.turn
                            self.turnChange()
                    if mouse[0] >= 250 and mouse[1] >= 50 and mouse[0] <= 350 and mouse[1] <= 150:
                        if self.display[2] != self.x and self.display[2] != self.o:
                            self.display[2] = self.turn
                            self.turnChange()
            if mouse[0] > i and mouse[1] > 150 and mouse[0] < i+100 and mouse[1] < 250:
                pygame.draw.rect(gameDisplay,white, [i, 150, 100, 100])
                if click[0] == 1:
                    if mouse[0] >= 50 and mouse[1] >= 150 and mouse[0] <= 150 and mouse[1] <= 250:
                        if self.display[3] != self.x and self.display[3] != self.o:
                            self.display[3] = self.turn
                            self.turnChange()
                    if mouse[0] >= 150 and mouse[1] >= 150 and mouse[0] <= 250 and mouse[1] <= 250:
                        if self.display[4] != self.x and self.display[4] != self.o:
                            self.display[4] = self.turn
                            self.turnChange()
                    if mouse[0] >= 250 and mouse[1] >= 150 and mouse[0] <= 350 and mouse[1] <= 250:
                        if self.display[5] != self.x and self.display[5] != self.o:
                            self.display[5] = self.turn
                            self.turnChange()
            if mouse[0] > i and mouse[1] > 250 and mouse[0] < i+100 and mouse[1] < 350:
                pygame.draw.rect(gameDisplay, white, [i, 250, 100, 100])
                if click[0] == 1:
                    if mouse[0] >= 50 and mouse[1] >= 250 and mouse[0] <= 150 and mouse[1] <= 350:
                        if self.display[6] != self.x and self.display[6] != self.o:
                            self.display[6] = self.turn
                            self.turnChange()
                    if mouse[0] >= 150 and mouse[1] >= 250 and mouse[0] <= 250 and mouse[1] <= 350:
                        if self.display[7] != self.x and self.display[7] != self.o:
                            self.display[7] = self.turn
                            self.turnChange()
                    if mouse[0] >= 250 and mouse[1] >= 250 and mouse[0] <= 350 and mouse[1] <= 350:
                        if self.display[8] != self.x and self.display[8] != self.o:
                            self.display[8] = self.turn
                            self.turnChange()

    # change turn for player x and player o also counting if the turn is max and no one is winning then it would be tied.
    def turnChange(self):
        if self.turn == self.x:
            self.turn = self.o
        else:
            self.turn = self.x
        self.tieCount += 1

    # turn changer for player x and player o
    def turnChanger(self):
        if self.turn == self.x:
            self.turn = self.o
        else:
            self.turn = self.x

    # showing text in the game
    def textShower(self):
        for i in range(9):
            if self.display[i] == self.x or self.display[i] == self.o:
                self.displayText(self.display[i], self.displayCo[i])

    # checking the game it will be tied or not
    def gameCheck(self):
        if self.display[0] != "0" and self.display[0] == self.display[1] and self.display[1] == self.display[2] or \
           self.display[3] != "0" and self.display[3] == self.display[4] and self.display[4] == self.display[5] or \
           self.display[6] != "0" and self.display[6] == self.display[7] and self.display[7] == self.display[8]:
            self.gameOver()
        elif self.display[0] != "0" and self.display[0] == self.display[3] and self.display[3] == self.display[6] or \
           self.display[1] != "0" and self.display[1] == self.display[4] and self.display[4] == self.display[7] or \
           self.display[2] != "0" and self.display[2] == self.display[5] and self.display[5] == self.display[8]:
            self.gameOver()
        elif self.display[0] != "0" and self.display[0] == self.display[4] and self.display[4] == self.display[8] or \
           self.display[2] != "0" and self.display[2] == self.display[4] and self.display[4] == self.display[6]:
            self.gameOver()
        elif self.tieCount == 9:
            self.gameTie()

    # check who is the winner and it will add the point in the bottom if the game
    def gameOver(self):
        font = pygame.font.SysFont("Arial", 40, True)
        self.turnChanger()
        self.pointAdder()
        text_ = font.render(("Player " + self.turn + " is Win!"), True, red)
        rect = text_.get_rect()
        rect.center = (200, 25)
        gameDisplay.fill(white)
        self.marker()
        self .drawLine()
        self.textShower()
        gameDisplay.blit(text_, rect)
        pygame.display.update()
        time.sleep(2)
        self.tieCount = 0
        self.display = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.turnChanger()

    # check if the turn is already 9 and the game will be tied
    def gameTie(self):
        font = pygame.font.SysFont("Arial", 40, True)
        self.turnChanger()
        text_ = font.render("Game Tied!", True, red)
        rect = text_.get_rect()
        rect.center = (200, 25)
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [50, 50, 300, 300]) # making the background red if tied
        self.drawLine()
        self.textShower()
        gameDisplay.blit(text_, rect)
        pygame.display.update()
        time.sleep(2)
        self.tieCount = 0
        self.display = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.turnChanger()

    # if the player already win, the winning row/column will be shown and the background will be colored green
    def marker(self):
        if self.display[0] != "0" and self.display[0] == self.display[1] and self.display[1] == self.display[2]:
            pygame.draw.rect(gameDisplay, green, [50, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [250, 50, 100, 100])
        elif self.display[3] != "0" and self.display[3] == self.display[4] and self.display[4] == self.display[5]:
            pygame.draw.rect(gameDisplay, green, [50, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [250, 150, 100, 100])
        elif  self.display[6] != "0" and self.display[6] == self.display[7] and self.display[7] == self.display[8]:
            pygame.draw.rect(gameDisplay, green, [50, 250, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 250, 100, 100])
            pygame.draw.rect(gameDisplay, green, [250, 250, 100, 100])
        elif self.display[0] != "0" and self.display[0] == self.display[3] and self.display[3] == self.display[6]:
            pygame.draw.rect(gameDisplay, green, [50, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [50, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [50, 250, 100, 100])
        elif self.display[1] != "0" and self.display[1] == self.display[4] and self.display[4] == self.display[7]:
            pygame.draw.rect(gameDisplay, green, [150, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 250, 100, 100])
        elif self.display[2] != "0" and self.display[2] == self.display[5] and self.display[5] == self.display[8]:
            pygame.draw.rect(gameDisplay, green, [250, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [250, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [250, 250, 100, 100])
        elif self.display[0] != "0" and self.display[0] == self.display[4] and self.display[4] == self.display[8]:
            pygame.draw.rect(gameDisplay, green, [50, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [250, 250, 100, 100])
        elif self.display[2] != "0" and self.display[2] == self.display[4] and self.display[4] == self.display[6]:
            pygame.draw.rect(gameDisplay, green, [250, 50, 100, 100])
            pygame.draw.rect(gameDisplay, green, [150, 150, 100, 100])
            pygame.draw.rect(gameDisplay, green, [50, 250, 100, 100])

    # display the text of point counter
    def points(self):
        font = pygame.font.SysFont("Arial", 30)
        text_ = font.render(("Points : X = " + str(self.pointX) + ", O = " + str(self.pointY)), True, black)
        rect = text_.get_rect()
        rect.center = (125, 375)
        gameDisplay.blit(text_, rect)

    # showing the text who is the first turn
    def turnShower(self):
        font = pygame.font.SysFont("Arial", 30)
        text_ = font.render(("Player Turn : " + self.turn), True, black)
        rect = text_.get_rect()
        rect.center = (100, 25)
        gameDisplay.blit(text_, rect)

    # counting the points
    def pointAdder(self):
        if self.turn == self.x:
            self.pointX += 1
        else:
            self.pointY += 1

# add a binding function with numbers; if you press key '1' it will be shown in the first row and first column in the game
# also the game's functioning in this def
def main():
    pygame.init()
    pygame.display.set_caption("TicTacToe")
    game = Game()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1 or e.key == pygame.K_KP1:
                    if game.display[0] == "0":
                        game.display[0] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_2 or e.key == pygame.K_KP2:
                    if game.display[1] == "0":
                        game.display[1] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_3 or e.key == pygame.K_KP3:
                    if game.display[2] == "0":
                        game.display[2] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_4 or e.key == pygame.K_KP4:
                    if game.display[3] == "0":
                        game.display[3] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_5 or e.key == pygame.K_KP5:
                    if game.display[4] == "0":
                        game.display[4] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_6 or e.key == pygame.K_KP6:
                    if game.display[5] == "0":
                        game.display[5] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_7 or e.key == pygame.K_KP7:
                    if game.display[6] == "0":
                        game.display[6] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_8 or e.key == pygame.K_KP8:
                    if game.display[7] == "0":
                        game.display[7] = game.turn
                        game.turnChange()
                elif e.key == pygame.K_9 or e.key == pygame.K_KP9:
                    if game.display[8] == "0":
                        game.display[8] = game.turn
                        game.turnChange()

        gameDisplay.fill(white)
        game.points()
        game.turnShower()
        game.check()
        game.drawLine()
        game.textShower()
        game.gameCheck()
        pygame.display.update()
        clock.tick(40)



if __name__ == "__main__":
    main()

sys.exit()
pygame.quit()
exit()
