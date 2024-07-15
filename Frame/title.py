import textwrap 
from PIL import Image, ImageFont, ImageDraw
import json 





def text_balance(text , width ):
    wrapper = textwrap.TextWrapper(width=width)
    return wrapper.wrap(text = text)
    

def fit_in(formatted_text , font):
    #font = ImageFont.truetype(FONT_PATH, FONT_SIZE, encoding='utf-8')
    #formatted_text = text_balance(text , width)
    max_width = max(font.getbbox(line)[2] for line in formatted_text)
    total_height = sum(font.getbbox(line)[3]  for line in formatted_text)
    return max_width , total_height


def place_text(TITLE,FRAME_WIDTH , FRAME_HEIGHT, COLOR='blue', FONT_PATH = "../resources/font.ttf" , BACKGROUND_IMAGE="resources/background.png", OUTPUT_PATH="output/framed_image.png" , FONT_SIZE = 60 , SPLIT_WIDTH = 12):
    
    if TITLE:
        counter = 1
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE, encoding='utf-8')
        formatted_text = text_balance(TITLE , SPLIT_WIDTH)
        max_width , total_height = fit_in(formatted_text , font)
        font_size = FONT_SIZE
        
        while  max_width >= FRAME_WIDTH:
            counter += 1 
            width = font_size // counter
            formatted_text = text_balance(TITLE, width)
            if width < FRAME_WIDTH:
                fit_in(formatted_text , font)
            else:
                print("Text width out of bounds")
                quit()
                
        while total_height >= FRAME_HEIGHT:
            font_size-= 2 
            font = ImageFont.truetype(FONT_PATH,font_size, encoding='utf-8')
            formatted_text = text_balance(TITLE, SPLIT_WIDTH)
            if font_size - 2 > 0:
                max_width, total_height = fit_in(formatted_text, font)
            else:
                print("Text height out of bounds.......")
                quit()
                
        image = Image.open(BACKGROUND_IMAGE)
        draw = ImageDraw.Draw(image)
        x = 0
        # print(frame_height , total_height)
        y = (FRAME_HEIGHT - total_height) // 2
        for line in formatted_text:
            #print(left , top , right , bottom)
            bbox = font.getbbox(line)
            text_width = bbox[2] 
            text_height = bbox[3]
            x = (FRAME_WIDTH - text_width) // 2
            draw.text((x, y), line, fill=COLOR, font=font)
            y += text_height
            # y += font.getbbox(line)[3]
        image.save(OUTPUT_PATH)
    else:
        image = Image.open(BACKGROUND_IMAGE)
        image.save(OUTPUT_PATH)
        print("[=] No text is given.....")
    return 
        

if __name__ == "__main__":
    ...
    # config_path = "../resources/title.json"
    # config = json.loads(open(config_path).read())
    
    # FRAME_WIDTH = config["Frame_width"]
    # FRAME_HEIGHT = config["Frame_height"]
    # BACKGROUND_PATH = config["Background"]
    # OUTPUT_PATH = config["Output_path"]
    # COLOR = config["Color"]
    # FONT_PATH = config["Font_path"]
    # FONT_SIZE = config["Font_size"]
    # SPLIT_WIDTH = config["Split_width"]
    # TITLE = config["Title"]
    
    # place_text(TITLE, FRAME_WIDTH, FRAME_HEIGHT , COLOR=COLOR, FONT_PATH=FONT_PATH,
    #            BACKGROUND_IMAGE=BACKGROUND_PATH, OUTPUT_PATH=OUTPUT_PATH, FONT_SIZE=FONT_SIZE, SPLIT_WIDTH=SPLIT_WIDTH)

