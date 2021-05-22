from voronoi import Voronoi


#Main class for map generation
class Mapgenerator:
    def create_map(seed,voronoi_amount):
        tilemap = Voronoi.generate_map(seed,voronoi_amount)
        tilemap = Mapgenerator.parse_map(tilemap)
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
        ib = 0
        jb = 0
        for x in tilemap:
            for y in x:
                if y in borders:
                    tilemap[ib][jb] = 1
                else:
                    tilemap[ib][jb] = 2
                jb += 1
            ib += 1
            jb = 0
        return tilemap

