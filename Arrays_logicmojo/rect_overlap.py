"""
Given two rectangles with top left and bottom right endpoints, Check if rectangles
overlap or not
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_overlap_rectange(s1, s2, p1, p2):
    if s1.x >= p2.x or s2.x >= p1.x:
        return False
    if s1.y <= p2.y or s2.y <= p1.y:
        return False
    return True


if __name__ == '__main__':
    s1 = Point(0, 10)
    p1 = Point(10, 0)
    s2 = Point(5, 5)
    p2 = Point(15, 0)

    if check_overlap_rectange(s1, s2, p1, p2):
        print("rectangles overlap")
    else:
        print("rectangles don't overlap")
