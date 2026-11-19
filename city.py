from ursina import *
import random

app = Ursina()
random.seed(42)

GRID_SIZE = 8        # blocks per side
BLOCK_SIZE = 12      # spacing between roads
ROAD_WIDTH = 3
CITY_SIZE = GRID_SIZE * BLOCK_SIZE

# 1. Ground
Entity(model='plane',
       scale=(CITY_SIZE + 10, 1, CITY_SIZE + 10),
       color=color.rgb32(75, 105, 75),
       position=(CITY_SIZE / 2, 0, CITY_SIZE / 2))

# 2. Roads: one across + one down per step
for i in range(GRID_SIZE + 1):
    p = i * BLOCK_SIZE
    Entity(model='cube', color=color.dark_gray,
           position=(CITY_SIZE / 2, 0.05, p),
           scale=(CITY_SIZE, 0.1, ROAD_WIDTH))
    Entity(model='cube', color=color.dark_gray,
           position=(p, 0.05, CITY_SIZE / 2),
           scale=(ROAD_WIDTH, 0.1, CITY_SIZE))

# 3. One plot in the middle of every block
for x in range(GRID_SIZE):
    for z in range(GRID_SIZE):
        center_x = x * BLOCK_SIZE + BLOCK_SIZE / 2
        center_z = z * BLOCK_SIZE + BLOCK_SIZE / 2

        # 4. A building with a random size
        height = random.randint(3, 18)
        width = random.uniform(3, 7)
        depth = random.uniform(3, 7)
        Entity(model='cube',
               position=(center_x, height / 2, center_z),
               scale=(width, height, depth),
               color=color.rgb32(random.randint(100, 210),
                                 random.randint(100, 210),
                                 random.randint(100, 210)))

# 5. Light, sky, camera - and run
DirectionalLight(rotation=(45, -45, 45))
Sky()
EditorCamera()
app.run()
