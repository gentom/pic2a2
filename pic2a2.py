#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import numpy

class Pic2AA:
    def __init__(self, image):
        self.ASCII_CHARs = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
        self.image = image
    
    def pic2aa(self, new_width=100):
        image = self._scaler(self.image)
        image = self._pic2grayscale(image)
        pixels_to_chars = self._mapper(image)
        len_pixels_to_chars = len(pixels_to_chars)
        image_ascii = [pixels_to_chars[index: index + new_width] for index in range(0, len_pixels_to_chars, new_width)]
        return "\n".join(image_ascii)
    
    # Maps each pixel to an ascii char based on the range in which it lies. 0-255 is divided into 11 ranges of 25 pixels each.
    def _mapper(self, image, range_width=25):
        pixels_in_image = list(image.getdata())
        pixels_to_chars = [self.ASCII_CHARs[int(value/range_width)] for value in pixels_in_image]
        return "".join(pixels_to_chars)

    # convert to grayscale
    def _pic2grayscale(self, image):
        return image.convert('L')

    # Resizes an image preserving the aspect ratio.
    def _scaler(self, new_width=100):
        (original_width, original_height) = self.image.size
        aspect_ratio = original_height / float(original_width)
        new_width = 100
        new_height = int(aspect_ratio * new_width)
        new_image = self.image.resize((new_width, new_height))
        return new_image

class Pic2A2_IO:
    @staticmethod
    def io(img_filepath):
        try:
            image = Image.open(img_filepath)
        except OSError:
            print('Cannot open', img_filepath)
            return
        ascii_art = Pic2AA(image)
        print(ascii_art.pic2aa())
