import board
import neopixel
import time
import random

pixel = neopixel.NeoPixel(board.GP23, 1, brightness=0.5)

new_R = 0
new_G = 0
new_B = 0
new_A = 0

while True:
    R = new_R
    G = new_G
    B = new_B
    A = new_A
    new_R = random.randint(0, 255)
    new_G = random.randint(0, 255)
    new_B = random.randint(0, 255)
    new_A = random.randint(0, 100)
    T = round(random.random() / 5, 2)
    #print(f'{T} - sleep time for ({new_R, new_G, new_B} with brightness {new_A})')
    
    while ((R != new_R) or (G != new_G) or (B != new_B) or (A != new_A)):
        if R != new_R:
            if R < new_R:
                R = R + 1
            else:
                R = R - 1
        if G != new_G:
            if G < new_G:
                G = G + 1
            else:
                G = G - 1
        if B != new_B:
            if B < new_B:
                B = B + 1
            else:
                B = B - 1
        if A != new_A:
            if A < new_A:
                A = A + 1
            else:
                A = A - 1
                
        pixel.brightness = A / 100
        pixel.fill((R, G, B))
        time.sleep(T)

    time.sleep(T * 10)
 
