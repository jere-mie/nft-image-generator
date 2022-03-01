from PIL import Image
import itertools
import json

# getting config details and setting IMAGE_SIZE
with open('config.json', 'r') as f:
    data = json.load(f)
IMAGE_SIZE = (data['image-x'], data['image-y'])

# getting the info on how many layers there are and how many images each layer has
numLayers = int(input("How many layers are there > "))
layers = [1 for i in range(numLayers)]
for i in range(numLayers):
    layers[i] = int(input(f'How many images in layer #{i} > '))

# this lets us traverse all combinations of images
nums = [[i for i in range(j)] for j in layers]
images = list(itertools.product(*nums))

# generating the images
for i in range(len(images)):
    out_image = Image.new("RGBA", IMAGE_SIZE, (255, 255, 255))
    fname = 'out/out'
    for j in range(len(images[i])):
        img = Image.open(f'layers/layer{j}/{images[i][j]}.png').convert('RGBA')
        out_image.paste(img, (0, 0, *IMAGE_SIZE), img)
        img.close()
        fname+= f'-{images[i][j]}'
    out_image.save(fname+'.png', 'PNG')
    out_image.close()