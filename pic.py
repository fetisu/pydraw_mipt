from graph import *
from math import sin, cos


def color(r, g, b):
    penColor(r, g, b)
    brushColor(r, g, b)


def move_by(pic, x, y):
    for obj in pic:
        moveObjectBy(obj, x, y)


def turn(points, alpha):
    out_points = []
    for pt in points:
        out_points.append((pt[0] * cos(alpha) + pt[1] * sin(alpha), -pt[0] * sin(alpha) + pt[1] * cos(alpha)))
    return out_points


def reflect_offset(offset, reflect):
    return {False: offset, True: -offset}[reflect]


def scale_reflect(points, k, reflect):
    out_points = []
    for pt in points:
        out_points.append(({False: pt[0] * k, True: 400 - pt[0] * k}[reflect], pt[1] * k))
    return out_points


def poly(points, k, reflect):
    return polygon(scale_reflect(points, k, reflect))


def ellipse(x1, y1, x2, y2, k, reflect):
    base = circle(0, 0, 10)
    if not reflect:
        changeCoords(base, [(x1 * k, y1 * k), (x2 * k, y2 * k)])
    else:
        changeCoords(base, [(400 - x1 * k, y1 * k), (400 - x2 * k, y2 * k)])
    return base


def ln(x1, y1, x2, y2, k, reflect):
    if not reflect:
        return line(x1 * k, y1 * k, x2 * k, y2 * k)
    else:
        return line(400 - x1 * k, y1 * k, 400 - x2 * k, y2 * k)


def foot(scale, reflect):
    return poly(
        [(239, 243), (230, 250), (235, 250), (245, 240), (255, 230), (250, 230), (242, 240), (247, 228), (242, 228),
         (241, 240), (240, 225), (235, 225), (239, 237), (219, 227), (217, 233)], scale, reflect)


def wing(scale, reflect):
    return poly([(50, 100), (40, 90), (40, 40), (10, 0), (30, 0), (100, 60), (105, 70), (100, 80), (60, 100)], scale,
                reflect)


def swan(scale: float = 1., reflect: bool = False) -> [object]:
    penSize(scale)
    penColor('black')
    brushColor('orange')
    sw = [ellipse(380, 110, 418, 120, scale, reflect), ellipse(380, 105, 420, 115, scale, reflect),
          foot(scale, reflect), foot(scale, reflect)]
    moveObjectBy(sw[2], reflect_offset(14 * scale, reflect), 6 * scale)
    moveObjectBy(sw[3], reflect_offset(74 * scale, reflect), 6 * scale)
    brushColor('white')
    sw.extend([wing(scale, reflect), wing(scale, reflect),
               poly([(160, 125), (160, 150), (80, 163), (103, 150), (70, 141), (100, 129), (80, 110)], scale, reflect)])
    moveObjectBy(sw[4], reflect_offset(190 * scale, reflect), 7 * scale)
    moveObjectBy(sw[5], reflect_offset(140 * scale, reflect), 7 * scale)
    penColor('white')
    sw.extend([ellipse(150, 100, 300, 180, scale, reflect), ellipse(280, 110, 340, 140, scale, reflect),
               ellipse(330, 95, 390, 130, scale, reflect)])
    brushColor('black')
    sw.append(ellipse(360, 102, 372, 110, scale, reflect))
    penSize(10 * scale)
    sw.extend([ln(190, 160, 220, 230, scale, reflect), ln(250, 160, 280, 230, scale, reflect),
               ln(220, 230, 240, 240, scale, reflect), ln(280, 230, 300, 240, scale, reflect),
               circle({False: 220 * scale, True: 400 - 220 * scale}[reflect], 230 * scale, 1.5 * scale),
               circle({False: 280 * scale, True: 400 - 280 * scale}[reflect], 230 * scale, 1.5 * scale)])
    return sw


def fish():
    penSize(1)
    penColor('black')
    brushColor('#9c292d')
    fsh = [polygon([(60, 85), (110, 93), (110, 107), (60, 115), (80, 100)]),
           polygon([(140, 100), (135, 70), (162, 74), (188, 68), (205, 76), (200, 100)]),
           polygon([(134, 110), (150, 110), (152, 130), (130, 127)]),
           polygon([(185, 110), (197, 110), (200, 128), (187, 131)])]
    brushColor('#9fbde6')
    penColor(brushColor())
    fsh.extend([polygon([(195, 85), (190, 115), (235, 100)]), ellipse(120, 80, 210, 120, 1, False),
                polygon([(95, 91), (95, 109), (130, 113), (130, 87)])])
    brushColor('green')
    fsh.append(circle(206, 96, 5))
    brushColor('black')
    penColor('black')
    fsh.append(circle(207, 95, 2))
    return fsh


def bird_pts():
    penColor('white')
    penSize(3)
    points = []
    for i in range(30):
        points.append((i - 30, 0.02 * i * (i - 30)))
    for i in range(31):
        points.append((i, 0.02 * i * (i - 30)))
    return points


def bird(scale=1., alpha=0.):
    pts = turn(scale_reflect(bird_pts(), scale, False), alpha)
    lines = []
    for i in range(len(pts) - 1):
        lines.append(line(*pts[i], *pts[i + 1]))
        lines.append(point(*pts[1]))
    return lines


windowSize(600, 900)
canvasSize(600, 900)

# Background
color(20, 20, 180)
rectangle(0, 0, 600, 100)
color(100, 40, 210)
rectangle(0, 100, 600, 180)
color(140, 60, 200)
rectangle(0, 180, 600, 250)
color(170, 100, 170)
rectangle(0, 250, 600, 340)
color(230, 140, 170)
rectangle(0, 340, 600, 410)
color(250, 160, 50)
rectangle(0, 410, 600, 490)
color(40, 120, 150)
rectangle(0, 490, 600, 900)

# Swans
move_by(swan(), -60, 540)
move_by(swan(scale=0.3), 250, 470)
move_by(swan(scale=0.6, reflect=True), 200, 510)

# Fish
move_by(fish(), 10, 750)
move_by(fish(), 240, 680)
move_by(fish(), 330, 620)

# Birds
move_by(bird(scale=2, alpha=0.2), 100, 100)
move_by(bird(scale=1, alpha=-0.2), 530, 130)
move_by(bird(scale=2, alpha=0.1), 260, 170)
move_by(bird(scale=1, alpha=-0.05), 130, 450)
move_by(bird(scale=0.5, alpha=0.04), 410, 200)
move_by(bird(scale=1, alpha=-0.02), 500, 210)
move_by(bird(scale=2, alpha=0.26), 290, 290)
move_by(bird(scale=2.5, alpha=0.3), 490, 390)
move_by(bird(scale=0.3, alpha=-0.1), 50, 190)

run()
