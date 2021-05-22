# Map generator

Map generator utility for personal project

Goal is to generate random islands with Voronoi.

## Todo
- [ ] Save tilemap
  - [ ] Save terrain as an array of terrain ids (int)
  - [ ] Save objects and entities as a list
    - [ ] Alternatively, use TMX Map Format to save these

### DefaultType Islands
- [x] Create a voronoi diagram
  - [x] Assign Edge cells as water, other cells as land
- [ ] Create Objects
  - [ ] Create a random number of palm trees (20-50)
    - [ ] palms can only generate on land - rerandomize palms that create over water
- [ ] Create Entities
  - [ ] Create a random number of enemy clusters (2-3)
    - [ ] Each cluster has a random number (1-4) of enemies
    - [ ] Each cluster has a coordinate; each individual enemy in a cluster is within deltaX & deltaY of the cluster coordinates
    - [ ] If enemy or enemy cluster is created on water, rerandomize it
