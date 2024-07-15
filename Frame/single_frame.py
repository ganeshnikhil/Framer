import os
from PIL import Image
import json 



def resize(image , IMAGE_WIDTH , IMAGE_HEIGHT):
    output_dir = "resources/en-tr"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    img = Image.open(image)
    new_image = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    name = os.path.basename(image)
    new_path = os.path.join(output_dir, name)
    new_image.save(new_path)
    return new_path


def frame_image(image_path, INTIAL_X = 152 , INTIAL_Y = 771 , BACKGROUND_PATH ="../resources/background.png" , OUTPUT_PATH="output/framed_image.png"):
    # Create a new background image
    new_image = Image.open(BACKGROUND_PATH)
    img = Image.open(image_path)
    x, y = INTIAL_X , INTIAL_Y
    new_image.paste(img, (x, y))
    new_image.save(OUTPUT_PATH)


if __name__ == "__main__":
    ...
    # config_path = "../resources/frame.json"
    # config = json.loads(open(config_path).read())
    # BACKGROUND_PATH = config["Single"]["Background"]
    # OUTPUT_PATH = config["Single"]["Output_path"]
    # FRAME_WIDTH = config["Single"]["Frame_width"]
    # FRAME_HEIGHT = config["Single"]["Frame_height"]
    # PADDING = config["Single"]["Padding"]
    # INTIAL_X = config["Single"]["Intial_x"]
    # INTIAL_Y = config["Single"]["Intial_y"]

    
    # path = "../resources/image/1.jpg"
    # new_path = resize(path , FRAME_WIDTH , FRAME_HEIGHT)
    # frame_image(new_path , INTIAL_X= INTIAL_X , INTIAL_Y= INTIAL_Y , BACKGROUND_PATH=BACKGROUND_PATH , OUTPUT_PATH=OUTPUT_PATH)