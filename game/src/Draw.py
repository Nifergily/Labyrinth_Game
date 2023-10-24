import pygame as pg


wall_colour = (178, 34, 34)       # Огнеупорно-кирпичный (Что блядь)
floor_colour = (255, 127, 80)     # Кораловый
light_colour = (255, 255, 255)    # Белый
shadow_colour = (0, 0, 0)         # Чёрный
seeker_colour = (128, 128, 0)     # Оливковый
portal_colour = (153, 102, 204)   # Аметистовый


def draw(lab, scale, screen, i, j):
    pg.draw.rect(screen, floor_colour, (scale * j, scale * i, scale, scale))
    match lab[i][j]:
        case 1:
            pg.draw.rect(screen, wall_colour, (scale * j, scale * i, scale, scale))
        case 2:
            pg.draw.rect(screen, shadow_colour, (scale * j + (scale / 2) - 4, scale * i + (scale / 2) - 4, 8, 8))
        case 3:
            pg.draw.rect(screen, seeker_colour, (scale * j + (scale / 2) - 4, scale * i + (scale / 2) - 4, 8, 8))
        case 4:
            pg.draw.rect(screen, light_colour, (scale * j + (scale / 2) - 4, scale * i + (scale / 2) - 4, 8, 8))
        case 5:
            pg.draw.rect(screen, portal_colour, (scale * j + (scale / 2) - 4, scale * i + (scale / 2) - 4, 8, 8))


def debug_draw(lab, scale, screen):
    for i in range(len(lab)):
        for j in range(len(lab)):
            draw(lab, scale, screen, i, j)


def default_draw(lab, scale, screen, position):
    try:
        if lab[position[0] - 1][position[1]] != 1:
            draw(lab, scale, screen, position[0] - 2, position[1])
            draw(lab, scale, screen, position[0] - 2, position[1] - 1)
            draw(lab, scale, screen, position[0] - 2, position[1] + 1)
            try:
                if lab[position[0] - 2][position[1]] != 1:
                    draw(lab, scale, screen, position[0] - 3, position[1])
                    draw(lab, scale, screen, position[0] - 3, position[1] - 1)
                    draw(lab, scale, screen, position[0] - 3, position[1] + 1)
            except Exception:
                pass
    except Exception:
        pass
    try:
        if lab[position[0] + 1][position[1]] != 1:
            draw(lab, scale, screen, position[0] + 2, position[1])
            draw(lab, scale, screen, position[0] + 2, position[1] - 1)
            draw(lab, scale, screen, position[0] + 2, position[1] + 1)
            try:
                if lab[position[0] + 2][position[1]] != 1:
                    draw(lab, scale, screen, position[0] + 3, position[1])
                    draw(lab, scale, screen, position[0] + 3, position[1] - 1)
                    draw(lab, scale, screen, position[0] + 3, position[1] + 1)
            except Exception:
                pass
    except Exception:
        pass
    try:
        if lab[position[0]][position[1] - 1] != 1:
            draw(lab, scale, screen, position[0], position[1] - 2)
            draw(lab, scale, screen, position[0] - 1, position[1] - 2)
            draw(lab, scale, screen, position[0] + 1, position[1] - 2)
            try:
                if lab[position[0]][position[1] - 2] != 1:
                    draw(lab, scale, screen, position[0], position[1] - 3)
                    draw(lab, scale, screen, position[0] - 1, position[1] - 3)
                    draw(lab, scale, screen, position[0] + 1, position[1] - 3)
            except Exception:
                pass
    except Exception:
        pass
    try:
        if lab[position[0]][position[1] + 1] != 1:
            draw(lab, scale, screen, position[0], position[1] + 2)
            draw(lab, scale, screen, position[0] - 1, position[1] + 2)
            draw(lab, scale, screen, position[0] + 1, position[1] + 2)
            try:
                if lab[position[0]][position[1] + 2] != 1:
                    draw(lab, scale, screen, position[0], position[1] + 3)
                    draw(lab, scale, screen, position[0] + 1, position[1] + 3)
                    draw(lab, scale, screen, position[0] - 1, position[1] + 3)
            except Exception:
                pass
    except Exception:
        pass
    draw(lab, scale, screen, position[0], position[1])
    draw(lab, scale, screen, position[0], position[1] + 1)
    draw(lab, scale, screen, position[0] + 1, position[1] + 1)
    draw(lab, scale, screen, position[0] + 1, position[1])
    draw(lab, scale, screen, position[0] + 1, position[1] - 1)
    draw(lab, scale, screen, position[0], position[1] - 1)
    draw(lab, scale, screen, position[0] - 1, position[1] - 1)
    draw(lab, scale, screen, position[0] - 1, position[1])
    draw(lab, scale, screen, position[0] - 1, position[1] + 1)


def draw_menu(screen, menu_vertical, difficulty):
    screen.blit(pg.font.Font(None, 72).render('Играть', True, (180, 0, 0)), (280, 350))
    screen.blit(pg.font.Font(None, 72).render('Сложность:', True, (180, 0, 0)), (280, 450))
    screen.blit(pg.font.Font(None, 72).render(str(difficulty), True, (180, 0, 0)), (580, 450))
    screen.blit(pg.font.Font(None, 72).render('Выйти', True, (180, 0, 0)), (280, 550))
    pg.draw.line(screen, floor_colour, (280, 304 + 100 * menu_vertical), (630 - 190 * (menu_vertical % 2), 304 + 100 * menu_vertical), 6)
