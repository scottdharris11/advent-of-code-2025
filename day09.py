"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 9", "Part 1")
def solve_part1(lines: list) -> int:
    """part 1 solving function"""
    tiles = parse_tiles(lines)
    max_area = 0
    for i, a in enumerate(tiles):
        for b in tiles[i+1:]:
            t = area(a,b)
            max_area = max(max_area, t)
    return max_area

@runner("Day 9", "Part 2")
def solve_part2(lines: list) -> int:
    """part 2 solving function"""
    tiles = parse_tiles(lines)
    floor = Floor(tiles)
    max_area = 0
    for i, a in enumerate(tiles):
        for b in tiles[i+1:]:
            t = area(a,b)
            if t > max_area:
                if red_green_area(a,b,floor):
                    print(f"found valid area between {a} and {b} of area {t}")
                    max_area = t
    return max_area

class Floor:
    """defines structure of floor"""
    def __init__(self, tiles: list[tuple[int,int]]):
        """capture the horizontal and vertical edges"""
        self.max_x = None
        self.min_x = None
        self.max_y = None
        self.min_y = None
        self.horizontal = {}
        self.vertical = {}
        tiles.append(tiles[0])
        idx = 1
        while idx < len(tiles):
            sx,sy = tiles[idx-1]
            ex,ey = tiles[idx]
            miny, maxy = (min(sy,ey),max(sy,ey))
            minx, maxx = (min(sx,ex),max(sx,ex))
            if sx == ex:
                cedges = self.vertical.get(sx, [])
                cedges.append((miny,maxy))
                self.vertical[sx] = cedges
            else:
                cedges = self.horizontal.get(sy, [])
                cedges.append((minx,maxx))
                self.horizontal[sy] = cedges
            if self.max_x is None or maxx > self.max_x:
                self.max_x = maxx
            if self.min_x is None or minx < self.min_x:
                self.min_x = minx
            if self.max_y is None or maxy > self.max_y:
                self.max_y = maxy
            if self.min_y is None or miny < self.min_y:
                self.min_y = miny
            idx += 1
        tiles.pop()

    def is_vertical(self, x: int, a: int, b: int) -> bool:
        """determine if points a and b are the end points of vertical line at x"""
        if x in self.vertical:
            for vert in self.vertical.get(x,[]):
                if (vert[0] == a and vert[1] == b) or (vert[0] == b and vert[1] == a):
                    return True
        return False

    def is_horizontal(self, y: int, a: int, b: int) -> bool:
        """determine if points a and b are the end points of horizontal line at x"""
        if y in self.horizontal:
            for horz in self.horizontal.get(y,[]):
                if (horz[0] == a and horz[1] == b) or (horz[0] == b and horz[1] == a):
                    return True
        return False

    def crosses_vert_edge(self, a: tuple[int,int], b: tuple[int,int]) -> bool:
        """determine if the supplied horizontal line crosses a vertical edge"""
        y = a[1]
        xa, xb = (a[0]+1,b[0]-1)
        for x, verts in self.vertical.items():
            if xa <= x <= xb:
                for vert in verts:
                    if vert[0] < y < vert[1]:
                        return True
        return False

    def crosses_horz_edge(self, a: tuple[int,int], b: tuple[int,int]) -> bool:
        """determine if the supplied vertical line crosses a horizontal edge"""
        x = a[0]
        ya, yb = (a[1]+1,b[1]-1)
        for y, horzs in self.horizontal.items():
            if ya <= y <= yb:
                for horz in horzs:
                    if horz[0] < x < horz[1]:
                        return True
        return False

    def inside_area(self, tl: tuple, tr: tuple, bl: tuple, _: tuple) -> bool:
        """determine if the four corners represent a rectangle inside all edges"""
        midpoint = (((tr[0]-tl[0])//2)+tl[0],((bl[1]-tl[1])//2)+tl[1])
        if not self.inside_horizonal(midpoint[0], self.min_y, midpoint[1]-1):
            return False
        if not self.inside_horizonal(midpoint[0], midpoint[1]+1, self.max_y):
            return False
        if not self.inside_vertical(midpoint[1], self.min_x, midpoint[0]-1):
            return False
        if not self.inside_vertical(midpoint[1], midpoint[0]+1, self.max_x):
            return False
        return True

    def inside_horizonal(self, x: int, start_y: int, end_y: int) -> bool:
        """determine inside in horiztonal space"""
        cross = 0
        edge = 0
        for y, horzs in self.horizontal.items():
            if start_y <= y <= end_y:
                for horz in horzs:
                    if horz[0] <= x <= horz[1]:
                        if horz[0] == x or horz[1] == x:
                            edge += 1
                        else:
                            cross += 1
        cross += edge // 2
        if cross == 0 or cross % 2 == 0:
            return False
        return True

    def inside_vertical(self, y: int, start_x: int, end_x: int) -> bool:
        """determine inside in horiztonal space"""
        cross = 0
        edge = 0
        for x, verts in self.vertical.items():
            if start_x <= x <= end_x:
                for vert in verts:
                    if vert[0] <= y <= vert[1]:
                        if vert[0] == y or vert[1] == y:
                            edge += 1
                        else:
                            cross += 1
        cross += edge // 2
        if cross == 0 or cross % 2 == 0:
            return False
        return True

def red_green_area(a: tuple[int,int], b: tuple[int,int], floor: Floor) -> bool:
    """determine if supplied corners form a rectangle within red/green area"""
    if a[0] == b[0]:
        return floor.is_vertical(a[0],a[1],b[1])
    if a[1] == b[1]:
        return floor.is_horizontal(a[1],a[0],b[0])
    tl, tr, bl, br = rect_corners(a,b)
    if floor.crosses_vert_edge(tl,tr) or floor.crosses_vert_edge(bl,br):
        return False
    if floor.crosses_horz_edge(tl,bl) or floor.crosses_horz_edge(tr,br):
        return False
    return floor.inside_area(tl,tr,bl,br)

def rect_corners(a: tuple[int,int], b: tuple[int,int]) -> tuple[tuple,tuple,tuple,tuple]:
    """calculate the 4 corners of rectangle"""
    ax, ay = a
    bx, by = b
    miny, maxy = (min(ay,by),max(ay,by))
    minx, maxx = (min(ax,bx),max(ax,bx))
    top_left = (minx,miny)
    top_right = (maxx,miny)
    bottom_left = (minx,maxy)
    bottom_right = (maxx,maxy)
    return top_left, top_right, bottom_left, bottom_right

def area(a: tuple[int,int], b: tuple[int,int]) -> int:
    """calculate the area between the two tiles when recentangle formed"""
    ax, ay = a
    bx, by = b
    return (abs(ax-bx)+1) * (abs(ay-by)+1)

def parse_tiles(lines: list[str]) -> list[tuple[int,int]]:
    """parse junction boxes from input"""
    tiles = []
    for line in lines:
        x,y = line.split(",")
        tiles.append(((int(x),int(y))))
    return tiles

# Data
data = read_lines("input/day09/input.txt")
sample = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()

# Part 1
assert solve_part1(sample) == 50
assert solve_part1(data) == 4729332959

# Part 2
assert solve_part2(sample) == 24
assert solve_part2(data) < 2437724873 # answer too high
