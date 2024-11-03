import pygame

pygame.init()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw, sh))

offset = 100

old_mouse_x = 6969
old_mouse_y = 6969

player = pygame.Rect((300, 250, offset, offset))

is_mouse_held = False
original = True

mouse_x_list = []
mouse_y_list = []

mouse_x_check = []
mouse_y_check = []


run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_mouse_held = False
                if not original:
                    i = 0
                    checkNumX = 0
                    checkNumY = 0
                    length = min(len(mouse_x_list), len(mouse_x_check))

                    while i < length:
                        if mouse_x_list[i] == mouse_x_check[i]:
                            checkNumX += 1
                        if mouse_y_list[i] == mouse_y_check[i]:
                            checkNumY += 1
                        i += 1

                    if checkNumX == length:
                        print("X succeeded!!!")
                    else:
                        print("X is " + str(checkNumX) + "/" + str(length))

                    if checkNumY == length:
                        print("Y succeeded!!!")
                    else:
                        print("Y is " + str(checkNumY) + "/" + str(length))

                    print("Offset was " + str(offset) + ". Try again with more or less offset by adjusting in the code!")

                    mouse_x_check = []
                    mouse_y_check = []
                    mouse_x_list = []
                    mouse_y_list = []

                if original:
                    original = False
                else:
                    original = True

    if is_mouse_held:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.center = (mouse_x, mouse_y)
        if old_mouse_x != mouse_x or old_mouse_y != mouse_y:
            if original:
                mouse_x_list.append(round(int(mouse_x) / offset) * offset)
                mouse_y_list.append(round(int(mouse_y) / offset) * offset)
            else:
                mouse_x_check.append(round(int(mouse_x) / offset) * offset)
                mouse_y_check.append(round(int(mouse_y) / offset) * offset)
        old_mouse_x, old_mouse_y = pygame.mouse.get_pos()

    pygame.display.update()

pygame.quit()
