#!/usr/bin/env python3

from PIL import Image

# Brightness calculation based on standard luminance coefficients
def calculate_brightness(pixel):
    r, g, b = pixel
    return 0.299 * r + 0.587 * g + 0.114 * b

# Generate a mask based on the image's brightness
def generate_mask(image, min_bright=127, max_bright=223):
    width, height = image.size
    mask = image.copy()

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            pixel_value = calculate_brightness(pixel)

            if ((pixel_value < min_bright) or (pixel_value > max_bright)):
                mask.putpixel((x, y), (0, 0, 0))
            
    #mask.save("mask.png")
    return mask

def sort_line(image, mask, width, height, reverse=False):
    y = height - 1 
    to_be_sorted = []

    range_start = 0
    for x in range(width):
        pixel = mask.getpixel((x, y))
        if (pixel == (0, 0, 0)):
            if((x != range_start) and ((x - 1) != range_start)):
                to_be_sorted.append((range_start, x - 1))
            range_start = x + 1
        
    for start, end in to_be_sorted:
        pixels = [image.getpixel((x, y)) for x in range(start, end + 1)]
        pixels.sort(key=calculate_brightness)
        if reverse:
            pixels.reverse()
        
        i = 0
        for x in range(start, end + 1):
            image.putpixel((x, y), pixels[i])
            i += 1

def sort_col(image, mask, width, height, reverse=False):     
    x = width - 1
    to_be_sorted = []

    range_start = 0
    
    for y in range(height):
        pixel = mask.getpixel((x, y))
        if (pixel == (0, 0, 0)):
            if((y != range_start) and ((y - 1) != range_start)):
                to_be_sorted.append((range_start, y - 1))
            range_start = y + 1
        
    for start, end in to_be_sorted:
        pixels = [image.getpixel((x, y)) for y in range(start, end + 1)]
        pixels.sort(key=calculate_brightness)
        if reverse:
            pixels.reverse()
        
        i = 0
        for y in range(start, end + 1):
            image.putpixel((x, y), pixels[i])
            i += 1


if __name__ == "__main__":
    # Configs
    image_name = 'image.png'
    min_bright = 80
    max_bright = 220
    opt = 1   # 0 = Vertical, 1 = Horizontal
    reverse = False

    try:
        image = Image.open(image_name).convert("RGB")
    except FileNotFoundError:
        print(f"Error: File '{image_name}' not found")
        exit(1)

    width, height = image.size

    mask = generate_mask(image, min_bright, max_bright)

    if opt == 0:  # Vertical
        for y in range(height):
            sort_line(image=image, mask=mask, width=width, height=y, reverse=reverse)
    elif opt == 1: # Horizontal
        for x in range(width):
            sort_col(image=image, mask=mask, width=x, height=height, reverse=reverse)

    frame = image.copy()
    frame.save("sorted_image.png")
    
   
    