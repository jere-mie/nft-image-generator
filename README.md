# nft-image-generator

A simple image generator for creating collections of images, similar to those used in NFTs

## Dependencies

- Python3
- Pillow (`pip3 install Pillow`)

## Getting Started

- All images must be the same size.
- Edit `config.json` to set the width and height (x and y) values of the images (in pixels).
- Make sure you have Python3 installed.
- Run `pip3 install pillow` to install pillow.
- Place all of your "layer" folders in the layer folder (i.e., the folder should contain `layers/layer0`, `layers/layer1`, etc. Each `layers/layerx/` folder should have `0.png`, `1.png`, etc.).
  - Look under `examples/layers` to see what the folder should look like.
- Run `python3 main.py` to run the program, and answer the prompts to generate your images!

## Optional - Create PDF of all images

- `pip3 install img2pdf`
- `python3 pdf-out.py`
- Check out `out/generated_images.pdf`!

## Optional - Rename your generated images numerically

- This feature allows all files to be renamed to 1.png, 2.png, ..., etc.
- Simply run `python3 number-out-images.py`
