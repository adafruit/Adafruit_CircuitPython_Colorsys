#This implements a chopped down relevant version of the colorsys library
#to add HLS and HSV to RGB support.  Script altered to return RGB[0-255]

__all__ = ["hls_to_rgb","hsv_to_rgb"]

# Some floating point constants

ONE_THIRD = 1.0/3.0
ONE_SIXTH = 1.0/6.0
TWO_THIRD = 2.0/3.0

# HLS: Hue, Luminance, Saturation
# H: position in the spectrum
# L: color lightness
# S: color saturation

def hls_to_rgb(h, l, s):
    if s == 0.0:
        return l, l, l
    if l <= 0.5:
        m2 = l * (1.0+s)
    else:
        m2 = l+s-(l*s)
    m1 = 2.0*l - m2
    return (int(_v(m1, m2, h+ONE_THIRD)*255), int(_v(m1, m2, h)*255), int(_v(m1, m2, h-ONE_THIRD)*255))

def _v(m1, m2, hue):
    hue = hue % 1.0
    if hue < ONE_SIXTH:
        return m1 + (m2-m1)*hue*6.0
    if hue < 0.5:
        return m2
    if hue < TWO_THIRD:
        return m1 + (m2-m1)*(TWO_THIRD-hue)*6.0
    return m1


# HSV: Hue, Saturation, Value
# H: position in the spectrum
# S: color saturation ("purity")
# V: color brightness

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return int(v * 255), int(t *255), int(p * 255)
    if i == 1:
        return int(q * 255), int(v *255), int(p * 255)
    if i == 2:
        return int(p * 255), int(v *255), int(t * 255)
    if i == 3:
        return int(p * 255), int(q *255), int(v * 255)
    if i == 4:
        return int(t * 255), int(p *255), int(v * 255)
    if i == 5:
        return int(v * 255), int(p *255), int(q * 255)
    # Cannot get here
