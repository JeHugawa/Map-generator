from generator.voronoi import Voronoi


#Main class for map generation
class MapGenerator:
    def create_map(seed):
        tilemap = Voronoi.generate_map(seed, voronoid_points)
        tilemap = parse_map(tilemap)
        return tilemap

    #parses Voronoied map to human readable form
    def parse_map(tilemap):
        #check which tiles are borders
        borders = []
        for i in range(0,256):
            for j in range(0,256):
                if i == 0 or j == 0:
                    if tilemap[i][j] not in borders:
                        borders.append(tilemap[i][j])
        #next we convert all border regions to water and rest to land
        for x in tilemap:
            for y in x:
                if y in borders:
                    y = 1
                else:
                    y = 2

        return tilemap

