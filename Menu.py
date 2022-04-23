import Multicolor
import numpy as np
import threading

red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
Multicolor.main(red_lower,red_upper)