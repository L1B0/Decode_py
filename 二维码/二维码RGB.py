from PIL import Image
x = 1640
y = 1920
im = Image.new("RGB", (x, y))
file = open('flag.bmp').read()
for i in range(0, x):
    for j in range(0, y):
        if file[i*x+y] == 0xff:
			rgb = [255,255,255]
		else:
			rgb = [0,0,0]
        im.putpixel((i, j), (int(rgb[0]), int(rgb[1]), int(rgb[2])))
im.show()
