"""Write a function that takes 2 colors as arguments and returns the average color.
* The parameters will be two 6-digit hexadecimal strings. This does not need to be validated.
* The return value should be a 6-digit hexadecimal string.
* The hexadecimal strings represent colors in RGB, much like in CSS.
* The average color is to be determined by taking the arithmetic mean for each component: red, green and blue
"""

def avg_hex_color(color1, color2):
    
    # convert hex to rgb
    rgb_color1 = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
    rgb_color2 = tuple(int(color2[i:i+2], 16) for i in (0, 2, 4))
    
    # calculate avg of two colors for each red, green, blue value
    rgb_avg_color = tuple( int((i[0]+i[1])/2) for i in zip(rgb_color1, rgb_color2) )
    
    # convert rgb to hex
    hex_rgb_color = '%02x%02x%02x' % rgb_avg_color
    
    return hex_rgb_color.upper()

avg_hex_color('39a459', '52eb80')
