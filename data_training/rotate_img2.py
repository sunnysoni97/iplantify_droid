from PIL import Image
import os

im_list = os.listdir()

for x in im_list:
	if(x.endswith(".py")):
		continue
	img = Image.open(x)
	img2 = Image.open(x)
	R = img.rotate(90, expand=True)
	L = img2.rotate(270, expand=True)

	if x.endswith(".jpg"):
		L.save(str(x+"L"+".jpg"))
		R.save(str(x+"R"+".jpg"))

	elif x.endswith(".jpeg"):
			L.save(str(x+"L"+".jpeg"))
			R.save(str(x+"R"+".jpeg"))

print("Conversion completed")