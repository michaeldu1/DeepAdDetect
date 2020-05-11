from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True

import glob

min_width, min_height = float('inf'), float('inf')

ct = 0
for img_path in glob.glob("./data/0/*.jpg"):
  # print(ct)
  ct += 1
  im = Image.open(img_path)
  new_img = im.resize((257, 257))
  new_img.save('./data-resized/0-resized/' + img_path[9:], im.format)
  # width, height = im.size
  # min_width = min(min_width, width)
  # min_height = min(min_height, height)

print("min widht", min_width)
print("min height", min_height)