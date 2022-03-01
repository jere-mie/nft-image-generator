import img2pdf
import glob
with open("./out/generated_images.pdf","wb") as f:
    f.write(img2pdf.convert(glob.glob("./out/*.png")))