import glob
from PIL import ImageFile, Image
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True


def find_min_dimensions():
  min_width, min_height = float('inf'), float('inf')
  for folder in list(range(11)) + ["resnet_training_negatives"]:
    curr_path = "./data/" + str(folder) + "/*.jpg"
    print(curr_path)
    for img_path in glob.glob(curr_path):
      im = Image.open(img_path)
      width, height = im.size
      min_width = min(min_width, width)
      min_height = min(min_height, height)

  print("min widht", min_width)
  print("min height", min_height)
  return (min_width, min_height)

def resize_images(width, height):
  os.mkdir('./data-resized')
  for folder in list(range(11)):
    curr_path = "./data/" + str(folder)
    if folder == 10:
      curr_path += "/*.png"
    else:
      curr_path += "/*.jpg"
    new_dest = "./data-resized/" + str(folder) + "-resized/"
    os.mkdir(new_dest)
    print(curr_path)
    for img_path in glob.glob(curr_path):
      im = Image.open(img_path)
      new_img = im.resize((width, height))
      new_img.save(new_dest + img_path[9:], im.format)
  
  os.mkdir("./data-resized/resnet_training_negatives_resized/")
  for idx in range(5):
    curr_path = "./data/" + "resnet_training_negatives/set"
    dest = './data-resized/resnet_training_negatives_resized/set' + str(idx)
    os.mkdir(dest)
    for img_path in glob.glob(curr_path + str(idx) + "/*.png"):
      im = Image.open(img_path)
      new_img = im.resize((width, height))
      new_img.save(dest + img_path[38:], im.format)

# min_width, min_height = find_min_dimensions()
resize_images(256, 256)