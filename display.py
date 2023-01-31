import pygame as pg
import sudokuSolve as s

br = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

WHITE = (255,255,255)
BLACK = (0,0,0)

pg.init()

font1 = pg.font.SysFont('chalkduster.ttf', 18)


canvas = pg.display.set_mode((900,900))

pg.display.set_caption("Sudoku Solver")
exit = False

while not exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True

        if event.type == pg.MOUSEBUTTONUP:
            mousePOS = pg.mouse.get_pos()
            x = mousePOS[0] // 100
            y = mousePOS[1] // 100
            print(f"X: {x}, Y: {y}, Value: {br[y][x]}")
    
    canvas.fill(WHITE)
    for x in range(9):
        if x % 3 != 0:
            pg.draw.line(canvas,BLACK, ((x*100),0),((x*100),900))
            pg.draw.line(canvas,BLACK, (0,(x*100)),(900,(x*100)))
        else:
            pg.draw.line(canvas,BLACK, ((x*100),0),((x*100),900),3)
            pg.draw.line(canvas,BLACK, (0,(x*100)),(900,(x*100)),3)
    
    for y in range(9):
        for x in range(9):
            if br[y][x] != 0:
                num = font1.render(str(br[y][x]), True, BLACK)
                canvas.blit(num,((x*100)+45,(y*100+45)))

    #br = s.solve(br)
    
    
    pg.display.update()