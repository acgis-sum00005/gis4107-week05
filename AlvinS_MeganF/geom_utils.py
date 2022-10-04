def is_point_in_box(x, y, xmin, ymin, xmax, ymax):
    if x > xmin and x < xmax:
        return True
    elif y > ymin and y < ymax:
         return True
    elif x == xmin or x == xmax or y == ymin or y == ymax:
         return False
    else:
        return False




