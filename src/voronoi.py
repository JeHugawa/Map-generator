import random
import math


class Voronoi:
    def generate_map(seed,voronoi_amount):
        #seed should stay the same as long as the program is running
        random.seed(seed)
        tilemap = []
        for x in range(0, 256):
            a = []
            for y in range(0, 256):
                a.append(0)
            tilemap.append(a)

        tilemap = Voronoi.voronoid(tilemap,voronoi_amount)

        return tilemap


    #extremely simple bruteforce Voronoid algorithm
    def voronoid(tilemap,amount):
        points = Voronoi.generate_voronoi_points(amount)

        for i in range(0,len(tilemap)):
            for j in range(0, len(tilemap)):
                closest_distance = len(tilemap) * len(tilemap[0])
                for k in range(0, len(points)):
                    distance = math.sqrt(((points[k][0] - i)**2) + ((points[k][1] - j)**2))
                    if distance < closest_distance:
                        closest_point = k
                        closest_distance = distance
                tilemap[i][j] = closest_point 

        return tilemap
        

    def generate_voronoi_points(amount):
        points = []
        for i in range(0, amount):
            a = []
            a.append(random.randint(0,256))
            a.append(random.randint(0,256))
            points.append(a)
        return points


