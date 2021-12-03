import numpy as np
from PIL import Image, ImageDraw
import random

REPS = 10 #number of times newtons method is applied
cols = ["red", "green", "blue", "yellow", "purple", "pink", "white", "black"]

#ie [2,4,-3,2] will be 2x^3 + 4x^2 - 3x + 2
p = []

print("Enter nums, type done when done: ")
usr_in = input("")
while (not usr_in.endswith("done") and len(p)<9):
    p.append(int(usr_in))
    usr_in = input("")

def f(x): #returns value of polynomial defined by array p at x
    ans = 0
    for a in range(len(p)):
        ans += p[a] * x**(len(p)-a-1)
    return ans

def df(x): #returns gradient of polynomial defined by array p at x
    ans = 0
    for a in range(len(p)-1):
        ans += p[a] * (len(p)-a-1) * x**(len(p)-a-2)
    return ans

def newtons(x, y): #applies newtons method to find roots
    comp = complex(x, y)
    for i in range(REPS):
        comp = comp - f(comp)/df(comp)
    return comp

roots = np.roots(p)
print("Roots: " + str(roots))

def get_col(x): #gets the color of the image drawn based on the root the complex number is closest to
    root_num = 0
    min_dist = 1000
    for n in range(len(roots)):
        d = ((x.real-roots[n].real)**2+(x.imag-roots[n].imag)**2)**0.5
        if (d < min_dist):
            root_num = n
            min_dist = d
    return cols[root_num]


size = int(input("Enter size of output:\n"))
max_coord = int(input("Enter the boundary for the fractal: "))

img = Image.new(mode = "RGB", size = (size, size))
draw = ImageDraw.Draw(img)

print("Generating - this might take a while!")

for x in range(size): #This is where the biz happens
    for y in range(size):
        d=(size/2)/max_coord
        draw.point((x,y), fill=get_col(newtons((x-(size/2))/d+0.00001, (y-(size/2))/d)))

img.show()
img.save("frac_" + str(random.randrange(0,1000000)) + ".png")

print("done!")
