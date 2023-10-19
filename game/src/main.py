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
    scale = 20

    lab.redact(lab.random_position(), 4)

    screen = pg.display.set_mode((lab.get_size() * scale, lab.get_size() * scale))
    pg.display.set_caption("ЛАБИРИНТ")
    clock = pg.time.Clock()

    player = sk(lab)

    shadows = []
    for i in range(8):
        shadow = sh(lab)
        shadows.append(shadow)

    while True:
        events = pg.event.get()
        if lab.get_condition() == 1:
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

            screen.fill((0, 0, 0))
            if debug:
                dr.debug_draw(lab.get_config(), scale, screen)
            else:
                dr.default_draw(lab.get_config(), scale, screen, player.get_position())
            pg.display.flip()

            clock.tick(60)

        elif lab.get_condition() == 2:
            screen.fill((0, 0, 0))
            screen.blit(pg.font.Font(None, 72).render('Поражение', True, (180, 0, 0)), (280, 350))
            pg.display.flip()
            clock.tick(60)
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
        elif lab.get_condition() == 3:
            screen.fill((0, 0, 0))
            screen.blit(pg.font.Font(None, 72).render('Победа', True, (180, 0, 0)), (285, 350))
            pg.display.flip()
            clock.tick(60)
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()


main()
