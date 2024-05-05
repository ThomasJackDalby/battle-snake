from PIL import Image, ImageDraw
from tools import get_xy, flood_fill

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCALE = 20

def output_flood_fill(width, height, starting_cells):

    def draw_cells(cells, file_path):
        image = Image.new('RGB', (width*SCALE, height*SCALE), (255,255,255))
        draw = ImageDraw.Draw(image)
        for i, cell in enumerate(cells):
            x, y = get_xy(width, i)
            if cell == 0: continue
            if cell == -1: fill = BLACK
            elif cell == 1: fill = RED
            elif cell == 2: fill = BLUE
            elif cell == 3: fill = GREEN
            draw.rectangle((x*SCALE, y*SCALE, (x+1)*SCALE, (y+1)*SCALE), fill)
        return image #.save(file_path)

    images = []
    for i, cells in enumerate(flood_fill(width, height, starting_cells, [(0, 0), (width-1, 0)])):
        images.append(draw_cells(cells, f"images/step.{i}.png"))
    images[0].save('test.gif', save_all=True, append_images=images[1:], optimize=True, duration=10, loop=0)

if __name__ == "__main__":
    import random
    width = 20
    height = 20

    cells = [0] * width * height
    for i in range(200):
        index = random.randint(0, len(cells)-1)
        cells[index] = -1

    output_flood_fill(width, height, cells)