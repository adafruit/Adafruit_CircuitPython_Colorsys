

import colorsys

hls = (0.2, 0.7, 0.5)
rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
print("HLS {} == RGB {}".format(hls, rgb))

hsv = (0.8, 0.5, 0.5)
rgb = colorsys.hls_to_rgb(hsv[0], hsv[1], hsv[2])
print("HSV {} == RGB {}".format(hsv, rgb))