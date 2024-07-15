from PIL import Image
import os
import json 


def resizes(images, FRAME_WIDTH, REQUIRED_HEIGHT, IMAGES_PER_FRAME = 2, bias=8):
    new_paths = []
    output_dir = "resources/en-tr"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    
    for path in images:
        img = Image.open(path)
        _ , img_height = img.size 
        if img_height != REQUIRED_HEIGHT:
            REQUIRED_WIDTH = (FRAME_WIDTH // IMAGES_PER_FRAME) - bias
            new_image = img.resize((REQUIRED_WIDTH , REQUIRED_HEIGHT))
            
        name = os.path.basename(path)
        new_path = os.path.join(output_dir, name)
        new_image.save(new_path)
        new_paths.append(new_path)
        
    return new_paths



def frame_images(resize_images, PADDING = 10 , INTIAL_X= 152 , INTIAL_Y = 771 ,  BACKGROUND_PATH="../resources/background.png", OUTPUT_PATH="output/framed_image.png", IMAGES_PER_FRAME=2):
    # Create a new background image
    new_image = Image.open(BACKGROUND_PATH)

    x, y = INTIAL_X , INTIAL_Y
    counter = 0
    for path in resize_images:
        img = Image.open(path)
        width, height = img.size
        
        new_image.paste(img, (x, y))
        
        # Check if image fits horizontally, otherwise move to next row 
        counter += 1
        if counter % IMAGES_PER_FRAME == 0:
            x = INTIAL_X  # Reset x to initial value for the new row
            y += height + PADDING  # Move y to next row
        else:
            x += width + PADDING  # Update x coordinate for the next image

    new_image.save(OUTPUT_PATH) # save new image to given path 

if __name__ == "__main__":
    ...
    # images = [
    #     "../resources/image/1.jpg",
    #     "../resources/image/3.jpg",
    #     "../resources/image/2.jpg",
    #     "../resources/image/4.jpg",
    #     "../resources/image/5.jpg",
    #     "../resources/image/6.jpg",
    #     "../resources/image/7.jpg"]
    
    # config_path = "../resources/frame.json"
    # config = json.loads(open(config_path).read())
    # BACK_GROUND_PATH = config["Multi"]["Background"]
    # FRAME_WIDTH = config["Multi"]["Frame_width"]
    # FRAME_HEIGHT = config["Multi"]["Frame_height"]
    # PADDING = config["Multi"]["Padding"]
    # IMAGES_PER_FRAME = config["Multi"]["Images_per_frame"]
    # INTIAL_X = config["Multi"]["Intial_x"]
    # INTIAL_Y = config["Multi"]["Intial_y"]
    
    
    # total_images = len(images) // IMAGES_PER_FRAME + len(images) % IMAGES_PER_FRAME
    # REQUIRED_HEIGHT = (FRAME_HEIGHT // total_images) - PADDING
    
    # resize_images = resizes(images, FRAME_WIDTH , REQUIRED_HEIGHT , IMAGES_PER_FRAME)
    # for path in resize_images:
    #     print(path)
        
    frame_images(resize_images)