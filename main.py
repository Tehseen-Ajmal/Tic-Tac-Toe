# import tkinter as tk

import random
import time
import pygame


# >>> TIC TAC TOE <<<
def tic_tac_toe_game():
    game_playing = 'yes'
    pygame.init()
    screen = pygame.display.set_mode((1270, 650))
    pygame.display.set_caption("Tic Tac Toe")

    screen.fill('white')
    back = pygame.transform.smoothscale(pygame.image.load('pf/tic_bg1.jpeg'), (1270, 650))
    b_rect = back.get_rect(center=(635, 325))
    o_turn = pygame.transform.scale(pygame.image.load('pf/o_turn.png'), (300, 100))
    o_turn_rect = o_turn.get_rect(center=(160, 50))

    you_win = pygame.transform.scale(pygame.image.load('pf/you_win.png'), (640, 200))
    you_win_rect = you_win.get_rect(center=(635, 325))

    you_lose = pygame.transform.scale(pygame.image.load('pf/you_lose.png'), (640, 200))
    you_lose_rect = you_win.get_rect(center=(635, 325))

    o_win = pygame.transform.scale(pygame.image.load('pf/o_win.png'), (640, 200))
    o_win_rect = o_win.get_rect(center=(635, 325))

    x_win = pygame.transform.scale(pygame.image.load('pf/x_wins.png'), (640, 200))
    x_win_rect = x_win.get_rect(center=(635, 325))

    draw = pygame.transform.scale(pygame.image.load('pf/draw.png'), (640, 200))

    x_turn = pygame.transform.scale(pygame.image.load('pf/x_turn.png'), (300, 100))
    x_turn_rect = x_turn.get_rect(center=(1100, 50))
    menu_screen = pygame.transform.scale(pygame.image.load('pf/tic_name.png'), (600, 244))
    menu_rect = menu_screen.get_rect(center=(635, 85))
    player_1 = pygame.transform.scale(pygame.image.load('pf/1_player.png'), (280, 280))
    player_1_rect = player_1.get_rect(center=(410, 350))
    easy = pygame.transform.scale(pygame.image.load('pf/normal_level.png'), (260, 260))
    easy_rect = easy.get_rect(center=(410, 450))
    medium = pygame.transform.scale(pygame.image.load('pf/hard_level.png'), (260, 260))
    medium_rect = medium.get_rect(center=(870, 450))

    difficulty = pygame.transform.scale(pygame.image.load('pf/difficulty.png'), (300, 150))
    diff_rect = difficulty.get_rect(center=(635, 150))

    player_2 = pygame.transform.scale(pygame.image.load('pf/2_player.png'), (300, 300))
    player_2_rect = player_2.get_rect(center=(870, 350))

    tic_board = pygame.transform.scale(pygame.image.load('pf/tic_tac_board.png'), (600, 600))
    tic_board_rect = tic_board.get_rect(center=(635, 325))

    tic_circle = pygame.transform.scale(pygame.image.load('pf/tic_tac_circle.png'), (150, 150))
    tic_circle_rect = tic_circle.get_rect(center=(635, 325))

    tic_cross = pygame.transform.scale(pygame.image.load('pf/tic_tac_cross.png'), (150, 150))
    tic_cross_rect = tic_cross.get_rect(center=(635, 325))

    tic_pos = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos_rect = tic_pos.get_rect(center=(635, 325))
    tic_pos0_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos1_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos2_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos3_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos4_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos5_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos6_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos7_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))
    tic_pos8_ = pygame.transform.scale(pygame.image.load('pf/tic_position.png'), (150, 150))

    data = ['', '', '', '', '', '', '', '', '']
    data_1 = [[], [], []]
    position = [(tic_cross_rect.x - 200, tic_cross_rect.y - 200), (tic_cross_rect.x, tic_cross_rect.y - 200),
                (tic_cross_rect.x + 200, tic_cross_rect.y - 200),
                (tic_cross_rect.x - 200, tic_cross_rect.y), (tic_cross_rect.x, tic_cross_rect.y),
                (tic_cross_rect.x + 200, tic_cross_rect.y),
                (tic_cross_rect.x - 200, tic_cross_rect.y + 200), (tic_cross_rect.x, tic_cross_rect.y + 200),
                (tic_cross_rect.x + 200, tic_cross_rect.y + 200)]

    tic_pos_l = [tic_pos0_, tic_pos1_, tic_pos2_, tic_pos3_, tic_pos4_, tic_pos5_, tic_pos6_, tic_pos7_, tic_pos8_]
    tic_pos0 = tic_pos0_.get_rect(center=(position[0][0] + 76, position[0][1] + 76))
    tic_pos1 = tic_pos1_.get_rect(center=(position[1][0] + 76, position[1][1] + 76))
    tic_pos2 = tic_pos2_.get_rect(center=(position[2][0] + 76, position[2][1] + 76))
    tic_pos3 = tic_pos3_.get_rect(center=(position[3][0] + 76, position[3][1] + 76))
    tic_pos4 = tic_pos4_.get_rect(center=(position[4][0] + 76, position[4][1] + 76))
    tic_pos5 = tic_pos5_.get_rect(center=(position[5][0] + 76, position[5][1] + 76))
    tic_pos6 = tic_pos6_.get_rect(center=(position[6][0] + 76, position[6][1] + 76))
    tic_pos7 = tic_pos7_.get_rect(center=(position[7][0] + 76, position[7][1] + 76))
    tic_pos8 = tic_pos8_.get_rect(center=(position[8][0] + 76, position[8][1] + 76))

    clock = pygame.time.Clock()
    run = 1
    co = 1
    menu = 1
    winning = 0
    while run:
        screen.blit(back, b_rect)

        count = data.count('')
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = 0
# Restart--------------------------------------------------------------------------------------------------------
        if menu == 2:
            time.sleep(1.5)
            run = 1
            co = 1
            menu = 1
            winning = 0
            data = ['', '', '', '', '', '', '', '', '']
            data_1 = [[], [], []]
            game_playing = 'yes'
# Start ----------------------------------------------------------------------------------------------------------
        if menu == 1:
            player = 0
            screen.fill('white')
            screen.blit(menu_screen, menu_rect)
# PLayer Selection -----------------------------------------------------------------------------------------------
            screen.blit(player_1, (player_1_rect))
            screen.blit(player_2, (player_2_rect))
            if player_1_rect.collidepoint(pygame.mouse.get_pos()):
                player_1 = pygame.transform.scale(pygame.image.load('pf/1_player1.png'), (300, 300))
                if pygame.mouse.get_pressed()[0]:
                    player = 1
                    menu = 00
                    time.sleep(0.3)
            else:
                player_1 = pygame.transform.scale(pygame.image.load('pf/1_player.png'), (280, 280))
            if player_2_rect.collidepoint(pygame.mouse.get_pos()):
                player_2 = pygame.transform.scale(pygame.image.load('pf/2_player1.png'), (330, 330))
                if pygame.mouse.get_pressed()[0]:
                    player = 2
                    menu = ''
                    time.sleep(0.3)
            else:
                player_2 = pygame.transform.scale(pygame.image.load('pf/2_player.png'), (310, 310))
        elif menu == 0:
            screen.blit(back, b_rect)
            screen.blit(menu_screen, menu_rect)
            screen.blit(difficulty, diff_rect)
# Difficulty Level -----------------------------------------------------------------------------------------------
            if easy_rect.collidepoint(pygame.mouse.get_pos()):
                easy = pygame.transform.scale(pygame.image.load('pf/normal_level1.png'), (300, 300))
                if pygame.mouse.get_pressed()[0]:
                    tic_level = 'easy'
                    menu = ''
                    time.sleep(0.3)
            else:
                easy = pygame.transform.scale(pygame.image.load('pf/normal_level.png'), (260, 260))
            if medium_rect.collidepoint(pygame.mouse.get_pos()):
                medium = pygame.transform.scale(pygame.image.load('pf/hard_level1.png'), (300, 300))
                if pygame.mouse.get_pressed()[0]:
                    tic_level = 'hard'
                    time.sleep(0.3)
                    menu = ''
            else:
                medium = pygame.transform.scale(pygame.image.load('pf/hard_level.png'), (260, 260))
            screen.blit(easy, easy_rect)
            screen.blit(medium, medium_rect)
        elif menu == 'retry':
            time.sleep(1)
# Results Display ------------------------------------------------------------------------------------------------
            screen.blit(back, b_rect)
            if winning == 'bot':
                screen.blit(you_lose, you_lose_rect)
            elif winning == 'play':
                screen.blit(you_win, you_win_rect)
            elif winning == 'play1':
                screen.blit(o_win, o_win_rect)
            elif winning == 'play2':
                screen.blit(x_win, x_win_rect)
            else:
                screen.blit(draw, x_win_rect)
            menu = 2
        else:
#Gameplay ----------------------------------------------------------------------------------------------------------
            if game_playing == 'yes' or game_playing == 0:

                for i in range(-1, 9):
                    if i == -1:
                        pass
                    else:
                        if data[i] == 0:
                            screen.blit(tic_circle, position[i])
                        if data[i] == 1:
                            screen.blit(tic_cross, position[i])
                        if data.count('') == 0:
                            game_playing = 0
                        screen.blit(tic_pos_l[i], (position[i][0], position[i][1]))

                if game_playing == 0:
                    game_playing = 'no'
                    menu = 'retry'
                    if player == 1:
#Results Logic BOT/PLayer ----------------------------------------------------------------------------------------
                        if data[0] == data[1] == data[2] == 1 or data[3] == data[4] == data[5] == 1 or data[6] == data[
                            7] == data[8] == 1:
                            winning = 'bot'
                        elif data[0] == data[3] == data[6] == 1 or data[1] == data[4] == data[7] == 1 or data[2] == \
                                data[5] == data[8] == 1:
                            winning = 'bot'
                        elif data[0] == data[4] == data[8] == 1 or data[2] == data[4] == data[6] == 1:
                            winning = 'bot'
                        elif data[0] == data[1] == data[2] == 0 or data[3] == data[4] == data[5] == 0 or data[6] == \
                                data[7] == data[8] == 0:
                            winning = 'play'
                        elif data[0] == data[3] == data[6] == 0 or data[1] == data[4] == data[7] == 0 or data[2] == \
                                data[5] == data[8] == 0:
                            winning = 'play'
                        elif data[0] == data[4] == data[8] == 0 or data[2] == data[4] == data[6] == 0:
                            winning = 'play'
                        else:
                            winning = 'draw'
#Results Logic Multiplayer -----------------------------------------------------------------------------------------------------
                    elif player == 2:
                        if data[0] == data[1] == data[2] == 1 or data[3] == data[4] == data[5] == 1 or data[6] == data[
                            7] == data[8] == 1:
                            winning = 'play2'
                        elif data[0] == data[3] == data[6] == 1 or data[1] == data[4] == data[7] == 1 or data[2] == \
                                data[5] == data[8] == 1:
                            winning = 'play2'
                        elif data[0] == data[4] == data[8] == 1 or data[2] == data[4] == data[6] == 1:
                            winning = 'play2'
                        elif data[0] == data[1] == data[2] == 0 or data[3] == data[4] == data[5] == 0 or data[6] == \
                                data[7] == data[8] == 0:
                            winning = 'play1'
                        elif data[0] == data[3] == data[6] == 0 or data[1] == data[4] == data[7] == 0 or data[2] == \
                                data[5] == data[8] == 0:
                            winning = 'play1'
                        elif data[0] == data[4] == data[8] == 0 or data[2] == data[4] == data[6] == 0:
                            winning = 'play1'
                        else:
                            winning = 'draw'
                else:
#Inputs ----------------------------------------------------------------------------------------------------------
                    if co % 2 != 0:
                        screen.blit(o_turn, (o_turn_rect))
                        if tic_pos0.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            0] == '':
                            data[0] = 0
                            co += 1
                        elif tic_pos1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            1] == '':
                            data[1] = 0
                            co += 1
                        elif tic_pos2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            2] == '':
                            data[2] = 0
                            co += 1
                        elif tic_pos3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            3] == '':
                            data[3] = 0
                            co += 1
                        elif tic_pos4.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            4] == '':
                            data[4] = 0
                            co += 1
                        elif tic_pos5.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            5] == '':
                            data[5] = 0
                            co += 1
                        elif tic_pos6.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            6] == '':
                            data[6] = 0
                            co += 1
                        elif tic_pos7.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            7] == '':
                            data[7] = 0
                            co += 1
                        elif tic_pos8.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                            8] == '':
                            data[8] = 0
                            co += 1
                        data_1 = [data[:3], data[3:6], data[6:]]
#2nd Player Input ----------------------------------------------------------------------------------------------------
                    elif co % 2 == 0:
                        screen.blit(x_turn, x_turn_rect)
                        if player == 2:
                            if tic_pos0.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and data[
                                0] == '':
                                data[0] = 1
                                co += 1
                            elif tic_pos1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        1] == '':
                                data[1] = 1
                                co += 1
                            elif tic_pos2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[2] == '':
                                data[2] = 1
                                co += 1
                            elif tic_pos3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        3] == '':
                                data[3] = 1
                                co += 1
                            elif tic_pos4.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        4] == '':
                                data[4] = 1
                                co += 1
                            elif tic_pos5.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        5] == '':
                                data[5] = 1
                                co += 1
                            elif tic_pos6.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        6] == '':
                                data[6] = 1
                                co += 1
                            elif tic_pos7.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        7] == '':
                                data[7] = 1
                                co += 1
                            elif tic_pos8.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and \
                                    data[
                                        8] == '':
                                data[8] = 1
                                co += 1
                        elif tic_level == 'hard':
                            data_1 = [data[:3], data[3:6], data[6:]]
# Hard Bot 1st move ---------------------------------------------------------------------------------------------
                            if co == 2:
                                a = [i for i in range(9) if data[i] == '']
                                random.choice(a)
                                x = random.choice(a)
                                data[x] = 1


# Hard Bot logic ----------------------------------------------------------------------------------------------------------
                            elif data_1[0][0] == data_1[0][1] == 1 and data_1[0][2] == '':
                                data[2] = 1
                            elif data_1[0][0] == data_1[0][2] == 1 and data_1[0][1] == '':
                                data[1] = 1
                            elif data_1[0][1] == data_1[0][2] == 1 and data_1[0][0] == '':
                                data[0] = 1


                            elif data_1[1][0] == data_1[1][1] == 1 and data_1[1][2] == '':
                                data[5] = 1
                            elif data_1[1][0] == data_1[1][2] == 1 and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[1][2] == 1 and data_1[1][0] == '':
                                data[3] = 1


                            elif data_1[2][0] == data_1[2][1] == 1 and data_1[2][2] == '':
                                data[8] = 1
                            elif data_1[2][0] == data_1[2][2] == 1 and data_1[2][1] == '':
                                data[7] = 1
                            elif data_1[2][1] == data_1[2][2] == 1 and data_1[2][0] == '':
                                data[6] = 1


                            elif data_1[0][0] == data_1[1][0] == 1 and data_1[2][0] == '':
                                data[6] = 1
                            elif data_1[0][1] == data_1[1][1] == 1 and data_1[2][1] == '':
                                data[7] = 1
                            elif data_1[0][2] == data_1[1][2] == 1 and data_1[2][2] == '':
                                data[8] = 1


                            elif data_1[1][0] == data_1[2][0] == 1 and data_1[0][0] == '':
                                data[0] = 1
                            elif data_1[1][1] == data_1[2][1] == 1 and data_1[0][1] == '':
                                data[1] = 1
                            elif data_1[1][2] == data_1[2][2] == 1 and data_1[0][2] == '':
                                data[2] = 1


                            elif data_1[0][0] == data_1[2][0] == 1 and data_1[1][0] == '':
                                data[3] = 1
                            elif data_1[0][1] == data_1[2][1] == 1 and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[0][2] == data_1[2][2] == 1 and data_1[1][2] == '':
                                data[5] = 1


                            elif data_1[0][0] == data_1[1][1] == 1 and data_1[2][2] == '':
                                data[8] = 1
                            elif data_1[0][0] == data_1[2][2] == 1 and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[2][2] == 1 and data_1[0][0] == '':
                                data[0] = 1


                            elif data_1[2][0] == data_1[1][1] == 1 and data_1[0][2] == '':
                                data[2] = 1
                            elif data_1[2][0] == data_1[0][2] == 1 and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[0][2] == 1 and data_1[2][0] == '':
                                data[6] = 1




                            elif data_1[0][0] == data_1[0][1] != '' and data_1[0][2] == '':
                                data[2] = 1
                            elif data_1[0][0] == data_1[0][2] != '' and data_1[0][1] == '':
                                data[1] = 1
                            elif data_1[0][1] == data_1[0][2] != '' and data_1[0][0] == '':
                                data[0] = 1


                            elif data_1[1][0] == data_1[1][1] != '' and data_1[1][2] == '':
                                data[5] = 1
                            elif data_1[1][0] == data_1[1][2] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[1][2] != '' and data_1[1][0] == '':
                                data[3] = 1


                            elif data_1[2][0] == data_1[2][1] != '' and data_1[2][2] == '':
                                data[8] = 1
                            elif data_1[2][0] == data_1[2][2] != '' and data_1[2][1] == '':
                                data[7] = 1
                            elif data_1[2][1] == data_1[2][2] != '' and data_1[2][0] == '':
                                data[6] = 1


                            elif data_1[0][0] == data_1[1][0] != '' and data_1[2][0] == '':
                                data[6] = 1
                            elif data_1[0][1] == data_1[1][1] != '' and data_1[2][1] == '':
                                data[7] = 1
                            elif data_1[0][2] == data_1[1][2] != '' and data_1[2][2] == '':
                                data[8] = 1


                            elif data_1[1][0] == data_1[2][0] != '' and data_1[0][0] == '':
                                data[0] = 1
                            elif data_1[1][1] == data_1[2][1] != '' and data_1[0][1] == '':
                                data[1] = 1
                            elif data_1[1][2] == data_1[2][2] != '' and data_1[0][2] == '':
                                data[2] = 1


                            elif data_1[0][0] == data_1[2][0] != '' and data_1[1][0] == '':
                                data[3] = 1
                            elif data_1[0][1] == data_1[2][1] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[0][2] == data_1[2][2] != '' and data_1[1][2] == '':
                                data[5] = 1


                            elif data_1[0][0] == data_1[1][1] != '' and data_1[2][2] == '':
                                data[8] = 1
                            elif data_1[0][0] == data_1[2][2] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[2][2] != '' and data_1[0][0] == '':
                                data[0] = 1


                            elif data_1[2][0] == data_1[1][1] != '' and data_1[0][2] == '':
                                data[2] = 1
                            elif data_1[2][0] == data_1[0][2] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[0][2] != '' and data_1[2][0] == '':
                                data[6] = 1


                            elif data_1[0].count(1) > 0 and data_1[0].count('') > 0:
                                a = [i for i in range(3) if data[i] == '']
                                data[random.choice(a)] = 1
                            elif data_1[1].count(1) > 0 and data_1[1].count('') > 0:
                                a = [i for i in range(3, 6) if data[i] == '']
                                data[random.choice(a)] = 1
                            elif data_1[2].count(1) > 0 and data_1[2].count('') > 0:
                                a = [i for i in range(6, 9) if data[i] == '']
                                data[random.choice(a)] = 1
                            else:
                                a = []
                                for i in range(9):
                                    if data[i] == '':
                                        a.append(i)
                                if len(a) > 0:
                                    random.choice(a)
                                    x = random.choice(a)
                                    data[x] = 1
                            co += 1
                        else:
#Easy Bot ----------------------------------------------------------------------------------------------------------
                            if data_1[0][0] == data_1[1][0] != '' and data_1[2][0] == '':
                                data[6] = 1
                            elif data_1[0][1] == data_1[1][1] != '' and data_1[2][1] == '':
                                data[7] = 1
                            elif data_1[0][2] == data_1[1][2] != '' and data_1[2][2] == '':
                                data[8] = 1


                            elif data_1[1][0] == data_1[2][0] != '' and data_1[0][0] == '':
                                data[0] = 1
                            elif data_1[1][1] == data_1[2][1] != '' and data_1[0][1] == '':
                                data[1] = 1
                            elif data_1[1][2] == data_1[2][2] != '' and data_1[0][2] == '':
                                data[2] = 1


                            elif data_1[0][0] == data_1[2][0] != '' and data_1[1][0] == '':
                                data[3] = 1
                            elif data_1[0][1] == data_1[2][1] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[0][2] == data_1[2][2] != '' and data_1[1][2] == '':
                                data[5] = 1


                            elif data_1[0][0] == data_1[1][1] != '' and data_1[2][2] == '':
                                data[8] = 1
                            elif data_1[0][0] == data_1[2][2] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[2][2] != '' and data_1[0][0] == '':
                                data[0] = 1


                            elif data_1[2][0] == data_1[1][1] != '' and data_1[0][2] == '':
                                data[2] = 1
                            elif data_1[2][0] == data_1[0][2] != '' and data_1[1][1] == '':
                                data[4] = 1
                            elif data_1[1][1] == data_1[0][2] != '' and data_1[2][0] == '':
                                data[6] = 1


                            elif data_1[0].count(1) > 0 and data_1[0].count('') > 0:
                                a = [i for i in range(3) if data[i] == '']
                                data[random.choice(a)] = 1
                            elif data_1[1].count(1) > 0 and data_1[1].count('') > 0:
                                a = [i for i in range(3, 6) if data[i] == '']
                                data[random.choice(a)] = 1
                            elif data_1[2].count(1) > 0 and data_1[2].count('') > 0:
                                a = [i for i in range(6, 9) if data[i] == '']
                                data[random.choice(a)] = 1
                            else:
                                a = []
                                for i in range(9):
                                    if data[i] == '':
                                        a.append(i)
                                if len(a) > 0:
                                    random.choice(a)
                                    x = random.choice(a)
                                    data[x] = 1

                            co += 1

                screen.blit(tic_board, (tic_board_rect))
                if data[0] == data[1] == data[2] == 0 or data[0] == data[1] == data[2] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos0.midleft), (tic_pos2.midright), 10)
                    game_playing = 0

                elif data[3] == data[4] == data[5] == 0 or data[3] == data[4] == data[5] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos3.midleft), (tic_pos5.midright), 10)
                    game_playing = 0

                elif data[6] == data[7] == data[8] == 0 or data[6] == data[7] == data[8] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos6.midleft), (tic_pos8.midright), 10)
                    game_playing = 0

                elif data[0] == data[3] == data[6] == 0 or data[0] == data[3] == data[6] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos0.midtop), (tic_pos6.midbottom), 10)
                    game_playing = 0

                elif data[1] == data[4] == data[7] == 0 or data[1] == data[4] == data[7] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos1.midtop), (tic_pos7.midbottom), 10)
                    game_playing = 0

                elif data[2] == data[5] == data[8] == 0 or data[2] == data[5] == data[8] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos2.midtop), (tic_pos8.midbottom), 10)
                    game_playing = 0

                elif data[0] == data[4] == data[8] == 0 or data[0] == data[4] == data[8] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos0.center), (tic_pos8.center), 10)
                    game_playing = 0

                elif data[2] == data[4] == data[6] == 0 or data[2] == data[4] == data[6] == 1:
                    pygame.draw.line(screen, 'black', (tic_pos2.center), (tic_pos6.center), 10)
                    game_playing = 0
        pygame.display.update()
        clock.tick(60)


tic_tac_toe_game()
