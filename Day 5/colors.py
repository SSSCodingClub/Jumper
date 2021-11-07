COLOR_BLACK        = (  0,   0,   0)
COLOR_WHITE        = (255, 255, 255)
COLOR_RED          = (255,   0,   0)
COLOR_YELLOW       = (255, 255,   0)
COLOR_LIGHT_PINK   = (255, 209, 223)
COLOR_LIGHT_BLUE   = (213, 209, 255)
COLOR_LIGHT_YELLOW = (255, 250, 209)
COLOR_ORANGE       = (255, 173,  51)
COLOR_OFF_RED      = (255,  69,  69)
COLOR_PURPLE       = (202,  69, 255)
COLOR_DARK_BLUE    = ( 57,  26, 135)

def interpolate_color(color_start, color_end, alpha):
    r = color_start[0] * (1 - alpha) + color_end[0] * alpha
    g = color_start[1] * (1 - alpha) + color_end[1] * alpha
    b = color_start[2] * (1 - alpha) + color_end[2] * alpha
    return r, g, b

def get_color_brightness(color):
    r, g, b = color
    return (r + g + b) / 3

class ColorPalette:

    interpolation_duration = 500
    brightness_threshold = 100
    
    def __init__(self, primary_color, accent_color, previous_palette = None):
        self.alpha = 0
        self.previous_palette = previous_palette
        self.primary_color = primary_color
        self.accent_color = accent_color
        if get_color_brightness(self.primary_color) > self.brightness_threshold:
            self.text_color = COLOR_BLACK
        else:
            self.text_color = COLOR_WHITE
   
    def update(self, delta_time):
        self.alpha = min(1, self.alpha + delta_time / self.interpolation_duration)
    
    def get_primary_color(self):
        if self.previous_palette is not None:
            return interpolate_color(self.previous_palette.primary_color, 
                                     self.primary_color, 
                                     self.alpha)
        else:
            return self.primary_color
    
    def get_accent_color(self):
        if self.previous_palette is not None:
            return interpolate_color(self.previous_palette.accent_color, 
                                     self.accent_color, 
                                     self.alpha)
        else:
            return self.accent_color
    
    def get_text_color(self):
        if self.previous_palette is not None:
            return interpolate_color(self.previous_palette.text_color, 
                                     self.text_color, 
                                     self.alpha)
        else:
            return self.text_color

