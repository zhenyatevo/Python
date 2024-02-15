import time
import pygame
import random


pygame.init()
# Наши цвета
color_peach_fuzz = (255, 190, 152)
color_for_bg = (0, 65, 103)
color_humbrol_yellow = (255, 255, 0)
color_greenyellow =(173, 255,47)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Какая-то змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
# Шрифт для игровых сообщений
font_style = pygame.font.SysFont('bahnschrift', 20) 
# Шрифт для счёта
score_font = pygame.font.SysFont("comicsansms", 35)
# Spesial K
special_font1 = pygame.font.SysFont("comicsansms", 30)
special_font2 = pygame.font.SysFont("comicsansms", 20)
special_font3 = pygame.font.SysFont("comicsansms", 15)
event_flag = -1


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, color_greenyellow, [x[0], x[1], snake_block, snake_block])

 
def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 10, dis_height / 2])

   
def specialK(event_flag):
    while event_flag == 1:
        dis.fill(color_peach_fuzz)
        mesg1 = special_font1.render('¡Felicidades! Encontraste el Especial K!', True, color_for_bg)
        mesg2 = special_font2.render('Presiona "P" nuevamente para comenzar un nuevo juego', True, color_for_bg)
        mesg3 = special_font3.render('- Sí, este fondo coincide con el color de tus últimas uñas, el color del año...', True, color_for_bg)
        dis.blit(mesg1, [dis_width / 6, dis_height / 3])
        dis.blit(mesg2, [dis_width / 6, dis_height / 2])
        dis.blit(mesg3, [dis_width / 6, dis_height / 3 * 2])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    event_flag *= -1
                    gameLoop(event_flag)


def Your_score(score):
    value = score_font.render('Ваш счёт: '+ str(score), True, color_humbrol_yellow)
    dis.blit(value,[0, 0])

def gameLoop(event_flag):
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = [] #Создаём список, в котором будем хранить 
#показатель текущей длины змейки.
    Length_of_snake = 1 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(color_for_bg)
            message('Вы проиграли! Нажмите Q для выхода или C для повторной игры', color_humbrol_yellow)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        event_flag *= -1
                        specialK(event_flag)
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(event_flag)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # Ачивка
                    event_flag *= -1
                    specialK(event_flag)
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(color_for_bg)
        pygame.draw.rect(dis, color_peach_fuzz, [foodx, foody, snake_block, snake_block])
        snake_Head = [] #Создаём список, в котором будет храниться 
#показатель длины змейки при движениях.
        snake_Head.append(x1) #Добавляем значения в список при 
#изменении по оси х.
        snake_Head.append(y1) #Добавляем значения в список при 
#изменении по оси y.
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0] #Удаляем первый элемент в списке 
#длины змейки, чтобы она не увеличивалась сама по себе при движениях.
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody: #Указываем, что в случаях, 
#если координаты головы змейки совпадают с координатами еды, еда появляется 
#в новом месте, а длина змейки увеличивается на одну клетку.
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
 
gameLoop(event_flag)
