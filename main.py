#   Konrad Budukiewicz 172108
#   Wykonałem losowanie 20 punktów zakres (0, 100), punkty maja odwołanie w klasie
#   Zaimplementowanie algorytmu Jarvisa

import matplotlib.pyplot as plt
from collections import namedtuple
import random

Point = namedtuple('Point', 'x y')


class Convex_Hull:
    points = []

    def __init__(self):
        pass

    def add(self, point):
        self.points.append(point)

    def orientation_points(self, pkt1, pkt2, pkt3):  # orientacja punktów
        value = ((pkt2.y - pkt1.y) * (pkt3.x - pkt2.x) - (pkt2.x - pkt1.x) * (pkt3.y - pkt2.y))
        if value == 0:
            return 0
        elif value > 0:
            return 1
        else:
            return 2

    def the_lowest_index_pkt(self):  # znajdowanie najmniejszego elementu
        min_index = 0
        points = self.points
        for i in range(1, len(points[1:])):
            if points[i:] < points[min_index:]:
                min_index = i
            elif points[i:] == points[min_index:]:
                if points[:i] > points[:min_index]:
                    min_index = i
        return min_index

    def calculate_convex_hull(self):  # funkcja licząca punkty i rysująca
        number_pkt = 20
        min_index = self.the_lowest_index_pkt()
        points = self.points
        hull_points = []
        p = min_index

        while True:
            q = 0
            hull_points.append(p)
            q = (p + 1) % number_pkt

            for i in range(number_pkt):
                if self.orientation_points(points[p], points[i], points[q]) == 2:
                    q = i

            p = q

            if p == min_index:
                break

        x_hull = []
        y_hull = []

        print(hull_points)
        for j in hull_points:
            x_hull.append(points[j].x)
            y_hull.append(points[j].y)
        x_hull.append(x_hull[0])
        y_hull.append(y_hull[0])
        x = [pkt.x for pkt in self.points]
        y = [pkt.y for pkt in self.points]

        plt.title('Convex Hull')
        plt.plot(x, y, marker='D', linestyle='None')
        plt.plot(x_hull, y_hull, 'r')
        plt.show()

    def printing(self):  # wypisuje punkty wylosowane
        x1 = [pkt.x for pkt in self.points]
        y1 = [pkt.y for pkt in self.points]
        print(x1, y1)


def main():
    new = Convex_Hull()
    for i in range(0, 20):
        new.add(Point(random.randint(0, 100), random.randint(0, 100)))  # losowanie pkt(0, 100)

    new.printing()
    new.the_lowest_index_pkt()
    new.calculate_convex_hull()


if __name__ == '__main__':
    main()
