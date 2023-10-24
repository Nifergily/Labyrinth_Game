import pygame as pg
import Draw as dr
import sys
from Shadow import Shadow as sh
from Seeker import Seeker as sk
from Labyrinth import Labyrinth as lb


def main():
    pg.init()
    lab = lb()

    debug = False
    shadows = None
    player = None
    turns = None
    menu_vertical = 1
    difficulty = 8
    scale = 20

    screen = pg.display.set_mode((lab.get_size() * scale, lab.get_size() * scale))
    pg.display.set_caption("ЛАБИРИНТ")
    clock = pg.time.Clock()

    while True:
        events = pg.event.get()
        screen.fill((0, 0, 0))
        match lab.get_condition():
            case 0:
                for event in events:
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    elif event.type == pg.KEYDOWN:
                        match event.key:
                            case pg.K_w:
                                if menu_vertical > 1:
                                    menu_vertical -= 1
                            case pg.K_s:
                                if menu_vertical < 3:
                                    menu_vertical += 1
                            case pg.K_a:
                                if menu_vertical == 2 and (4 < difficulty):
                                    difficulty -= 1
                            case pg.K_d:
                                if menu_vertical == 2 and (difficulty < 20):
                                    difficulty += 1
                            case pg.K_RETURN:
                                if menu_vertical == 1:
                                    debug = False

                                    lab = lb()
                                    lab.set_condition(1)
                                    lab.redact(lab.random_position(), 4)

                                    turns = 0

                                    for i in range(8):
                                        lab.redact(lab.random_position(), 5)

                                    player = sk(lab)
                                    shadows = []
                                    for i in range(difficulty):
                                        shadow = sh(lab)
                                        shadows.append(shadow)
                                elif menu_vertical == 3:
                                    pg.quit()
                                    sys.exit()
                dr.draw_menu(screen, menu_vertical, difficulty)

            case 1:
                for event in events:
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        for shadow in shadows:
                            shadow.think(lab.get_config(), player.get_position())
                        match event.key:
                            case pg.K_w:
                                player.move(lab, "Up")
                            case pg.K_s:
                                player.move(lab, "Down")
                            case pg.K_a:
                                player.move(lab, "Left")
                            case pg.K_d:
                                player.move(lab, "Right")
                            case pg.K_p:
                                debug = not debug
                        for shadow in shadows:
                            shadow.think(lab.get_config(), player.get_position())
                            shadow.move(lab)
                        turns += 1
                        if turns % (48 - 16 * (difficulty // 8)) == 0:
                            lab.rebuild()

                if debug:
                    dr.debug_draw(lab.get_config(), scale, screen)
                else:
                    dr.default_draw(lab.get_config(), scale, screen, player.get_position())

            case _:
                if lab.get_condition() == 2:
                    screen.blit(pg.font.Font(None, 64).render('Поражение! Ходов сделано: ' + str(turns), True, (180, 0, 0)), (60, 350))
                else:
                    screen.blit(pg.font.Font(None, 64).render('Победа! Ходов сделано: ' + str(turns), True, (180, 0, 0)), (60, 350))

                for event in events:
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    elif event.type == pg.KEYDOWN:
                        lab.set_condition(0)
        pg.display.flip()
        clock.tick(60)


main()
