from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeThumb(processors.Resize):
    width = 64
    height = 64
    crop = True

class ResizeDisplay(processors.Resize):
    width = 600

class EnhanceThumb(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

class Thumbnail(ImageSpec):
    access_as = 'thumbnail'
    pre_cache = True
    processors = [ResizeThumb, EnhanceThumb]

class Display(ImageSpec):
    increment_count = True
    processors = [ResizeDisplay]

