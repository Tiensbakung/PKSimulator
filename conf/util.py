import coord
unit = 3.33                     # 1 speed value = 3.33mm/s


def get_speed(speed):
    if speed:
        l = speed['left'] * unit / coord.bw_ratio
        r = speed['right'] * unit / coord.bw_ratio
        return l, r
    else:
        return 0, 0
