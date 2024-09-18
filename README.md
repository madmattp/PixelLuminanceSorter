# PixelLuminanceSorter

This Python script processes an image by sorting its pixels based on brightness. The sorting can be done either horizontally or vertically within masked regions of the image, determined by brightness thresholds.
Inspired by Kim Asendorf's [ASDF Pixel Sort](https://github.com/kimasendorf/ASDFPixelSort/tree/master)

<p align="center">
   <img src="https://github.com/user-attachments/assets/bb41e2be-5264-4660-8556-8fce4d7e5205" alt="sorted_image" width="50%">
</p>

### Features!

- Sort pixels by brightness
- Supports vertical and horizontal sorting
- Customizable brightness thresholds


### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/PixelLuminanceSorter.git
   ```
2. Install the required dependencies:
   ```bash
   pip install pillow
   ```

### Usage
1. Adjust the settings inside the script:
    - ```image_name```: Image to be sorted
    - ```min_bright```: Minimum brightness threshold
    - ```max_bright```: Maximum brightness threshold
    - ```opt```: Sorting direction (0 for vertical, 1 for horizontal)
    - ```reverse```: Whether to reverse the sorting order
2. Run the script:
   ```bash
   python PixelLuminanceSorter.py
   ```
3. The sorted image will be saved as ```sorted_image.png```.

### Acknowledgements
This project is inspired by the work of [Kim Asendorf](https://github.com/kimasendorf/ASDFPixelSort/tree/master).


