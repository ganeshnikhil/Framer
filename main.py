from Frame.multi_frame import resizes , frame_images
from Frame.single_frame import resize , frame_image
from Frame.title import place_text 
import json 
import os 
import argparse 
def main():
    
    parser = argparse.ArgumentParser(
        description="Add frames and titles to your screenshots.",
        epilog="Example usage:\n"
                "python main.py -s -c path/to/single/config.json -t path/to/text/config.json\n"
                "python main.py -m -c path/to/multi/config.json -t path/to/text/config.json\n"
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-s', '--single', action='store_true', help="Single image")
    mode_group.add_argument('-m', '--multi', action='store_true', help="Multi image")
    parser.add_argument('-c' , '--config', help="Path to the configuration file (optional)")
    parser.add_argument('-t','--text', help="Path to the text configuration file (optional)")

    args = parser.parse_args()
    
    
    if args.text:
        title_path = args.text 
    
    else:
        title_path = "resources/title.json"
    try:
        # Load title configuration
        config = json.loads(open(title_path).read())
        FRAME_WIDTH = config["Frame_width"]
        FRAME_HEIGHT = config["Frame_height"]
        BACKGROUND_PATH = config["Background"]
        OUTPUT_PATH = config["Output_path"]
        COLOR = config["Color"]
        FONT_PATH = config["Font_path"]
        FONT_SIZE = config["Font_size"]
        SPLIT_WIDTH = config["Split_width"]
        TITLE = config["Title"]
        # Place text if TITLE is provided
        place_text(TITLE, FRAME_WIDTH, FRAME_HEIGHT,  COLOR=COLOR, FONT_PATH=FONT_PATH,BACKGROUND_IMAGE=BACKGROUND_PATH, OUTPUT_PATH=OUTPUT_PATH, FONT_SIZE=FONT_SIZE, SPLIT_WIDTH=SPLIT_WIDTH)

    except FileNotFoundError:
        print(f"Error: Title configuration file '{title_path}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to parse title configuration file '{title_path}'. Check if it's valid JSON.")
        return

    # Determine mode (single or multi)
    mode = 'single' if args.single else 'multi'

    # Determine configuration file path
    config_path = args.config if args.config else "resources/frame.json"
    try:
        with open(config_path) as config_file:
            config = json.load(config_file)
            
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.")
        return 
    except json.JSONDecodeError:
        print(f"Error: Failed to parse configuration file '{config_path}'. Check if it's valid JSON.")
        return 
    
    # setting title 
    if  mode == "single":
        image  = config["Single"]["Image_path"]
        BACKGROUND_PATH = config["Single"]["Background"]
        OUTPUT_PATH = config["Single"]["Output_path"]
        FRAME_WIDTH = config["Single"]["Frame_width"]
        FRAME_HEIGHT = config["Single"]["Frame_height"]
        PADDING = config["Single"]["Padding"]
        INTIAL_X = config["Single"]["Intial_x"]
        INTIAL_Y = config["Single"]["Intial_y"]
        # Resize and frame single image
        new_path = resize(image, FRAME_WIDTH, FRAME_HEIGHT)
        frame_image(new_path, INTIAL_X=INTIAL_X, INTIAL_Y=INTIAL_Y,BACKGROUND_PATH=BACKGROUND_PATH, OUTPUT_PATH=OUTPUT_PATH)
        print(f"[=] SINGLE Framed image is saved in  {OUTPUT_PATH}")
        
        
    elif mode == "multi":
        
        path_of_images = config["Multi"]["Images_path"]
        images = [os.path.join(path_of_images, file) for file in os.listdir(path_of_images) if os.path.isfile(os.path.join(path_of_images, file))]

        BACK_GROUND_PATH = config["Multi"]["Background"]
        FRAME_WIDTH = config["Multi"]["Frame_width"]
        FRAME_HEIGHT = config["Multi"]["Frame_height"]
        PADDING = config["Multi"]["Padding"]
        IMAGES_PER_FRAME = config["Multi"]["Images_per_frame"]
        INTIAL_X = config["Multi"]["Intial_x"]
        INTIAL_Y = config["Multi"]["Intial_y"]
        OUTPUT_PATH = config["Multi"]["Output_path"]
        
        total_images = len(images) // IMAGES_PER_FRAME + len(images) % IMAGES_PER_FRAME
        REQUIRED_HEIGHT = (FRAME_HEIGHT // total_images) - PADDING
        
        # Resize and frame multiple images
        resize_images = resizes(images, FRAME_WIDTH,REQUIRED_HEIGHT, IMAGES_PER_FRAME)
        
        for path in resize_images:
            print(path)

        frame_images(resize_images , PADDING=PADDING ,INTIAL_X=INTIAL_X , INTIAL_Y = INTIAL_Y , BACKGROUND_PATH=BACK_GROUND_PATH , OUTPUT_PATH=OUTPUT_PATH ,IMAGES_PER_FRAME=IMAGES_PER_FRAME )
        print(f"[=] MULTI Framed image is saved in  {OUTPUT_PATH}")
    
    else:
        print("Invalid ..")


if __name__ == "__main__":
    main()
    
    
    

# python main.py -s -c path/to/single/config.json -t path/to/text/config.json
# python main.py -m -c path/to/multi/config.json -t path/to/text/config.json

