'''
File Name: 2048.py
Date: 2016/01/27
Author: YQbeyond
Description: 2048 game use python
'''

import pygame
from pygame.locals import *
import math
import random
import datetime
from sys import exit

steps = 0 # steps
SIZE = 4
Matrix = [] # 4x4 matrix
Target = 2048

background_image = 'img/bg.jpg'
SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
font = pygame.font.SysFont('arial', 24)
background = pygame.image.load(background_image).convert()

def init():
    global SIZE, Matrix
    Matrix = [[0 for i in range(SIZE)] for j in range(SIZE)] # 4x4 matrix

def join_together(row):
    if len(row) <= 1:
        return row
    finish = False
    while not finish:
        for i in range(1, len(row)):
            if row[i] == row[i-1]:
                row[i-1] *= 2
                row.remove(row[i])
                break
            if i == len(row) - 1:
                finish = True
        if len(row) <= 1:
            break
    return row

def rand_new(direct):
    global Matrix, SIZE
    rand_black = [Matrix.index(row) for row in Matrix if 0 in row]
    if len(rand_black) > 0:
        if direct == 'l':
            Matrix[random.choice(rand_black)][SIZE - 1] = random.choice([2, 4])
        elif direct == 'r':
            Matrix[random.choice(rand_black)][0] = random.choice([2, 4])

    rand_black = []
    for j in range(SIZE):
        for i in range(SIZE):
            if Matrix[i][j] == 0:
                rand_black.append(j)
                break
    if len(rand_black) > 0:
        if direct == 'u':
            Matrix[SIZE - 1][random.choice(rand_black)] = random.choice([2, 4])
        elif direct == 'd':
            Matrix[0][random.choice(rand_black)] = random.choice([2, 4])

def move(direct):
    global SIZE, Matrix
    if direct == 'l':
        for i in range(SIZE):
            tmp_row = [e for e in Matrix[i] if e != 0]
            if len(tmp_row) >= 1:
                tmp_row = join_together(tmp_row)
            for j in range(SIZE):
                if j < len(tmp_row):
                    Matrix[i][j] = tmp_row[j]
                else:
                    Matrix[i][j] = 0

    elif direct == 'r':
        for i in range(SIZE):
            tmp_row = [e for e in Matrix[i] if e != 0]
            if len(tmp_row) >= 1:
                tmp_row.reverse()
                tmp_row = join_together(tmp_row)
                tmp_row.reverse()
            for j in range(SIZE):
                if j < 4 - len(tmp_row):
                    Matrix[i][j] = 0
                else:
                    Matrix[i][j] = tmp_row[j + len(tmp_row) - 4]

    elif direct == 'u':
        for j in range(SIZE):
            tmp_col = []
            for i in range(SIZE):
                if (Matrix[i][j] != 0):
                    tmp_col.append(Matrix[i][j])
            if len(tmp_col) >= 1:
                tmp_col = join_together(tmp_col)
            for i in range(SIZE):
                if i < len(tmp_col):
                    Matrix[i][j] = tmp_col[i]
                else:
                    Matrix[i][j] = 0

    elif direct == 'd':
        for j in range(SIZE):
            tmp_col = []
            for i in range(SIZE):
                if (Matrix[i][j] != 0):
                    tmp_col.append(Matrix[i][j])

            if len(tmp_col) >= 1:
                tmp_col.reverse()
                tmp_col = join_together(tmp_col)
                tmp_col.reverse()
            for i in range(SIZE):
                if i < 4 - len(tmp_col):
                    Matrix[i][j] = 0
                else:
                    Matrix[i][j] = tmp_col[i + len(tmp_col) - 4]


def draw_matrix():
    global Matrix, SIZE
    x = y = 40
    for i in range(SIZE + 1):
        pygame.draw.rect(screen, (0, 0, 0), (x, y+400/SIZE*i, 401, 4))
        pygame.draw.rect(screen, (0, 0, 0), (x+400/SIZE*i, y, 4, 401))
    x = y = 40
    for i in range(SIZE):
        for j in range(SIZE):
            text = font.render('', True, (0, 0, 0))
            if Matrix[i][j] != 0:
                text = font.render(str(Matrix[i][j]), True, (0, 0, 0))
            margin_width = (400 / SIZE - text.get_width()) / 2
            margin_height = (400 / SIZE - text.get_height()) / 2
            screen.blit(text, (x + margin_width, y + margin_height))
            x = x +  400 / SIZE
        y = y + 400 / SIZE
        x = 40

def judge():
    global Matrix, Target
    for i in range(SIZE):
        for j in range(SIZE):
            if (Matrix[i][j] == Target):
                Target = Matrix * 2
                return True
    return False

def no_move(arr):
    global SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            if arr[i][j] == 0:
                return False
    for i in range(SIZE - 1):
        for j in range(SIZE - 1):
            if arr[i][j] == arr[i][j+1] or arr[i][j] == arr[i+1][j]:
                return False
    for j in range(SIZE - 1):
        if arr[SIZE-1][j] == arr[SIZE-1][j+1]:
            return False
    for i in range(SIZE - 1):
        if arr[i][SIZE-1] == arr[i+1][SIZE-1]:
            return False
    return True

def process(direct):
    global steps
    steps += 1
    move(direct)
    rand_new(direct)


init()
start = datetime.datetime.now()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                process('l')
            elif event.key == K_RIGHT:
                process('r')
            elif event.key == K_UP:
                process('u')
            elif event.key == K_DOWN:
                process('d')

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    draw_matrix()
    pygame.draw.rect(screen, (0, 0, 0), (480, 0, 2, 480))
    text = font.render("STEPS: " + str(steps), True, (0,0,0))
    x = (160 - text.get_width()) / 2
    screen.blit(text, (480 + x, 100))
    text = font.render("TIME: " + str((datetime.datetime.now() - start).seconds), True, (0,0,0))
    x = (160 - text.get_width()) / 2
    screen.blit(text, (480 + x, 200))

    pygame.display.update()

    res = judge()
    if res == True:
        ans = raw_input('Congratulations! You have reached to ' + str(Target) + '. Continue?(y/n)')
        if ans == 'Y' or ans == 'y':
            init()
        elif ans == 'N' or ans == 'n':
            exit()
    elif no_move(Matrix):
        ans = raw_input('Sorry, You failed. Restart?(y/n)')
        if ans == 'Y' or ans == 'y':
            init()
        elif ans == 'N' or ans == 'n':
            exit()
