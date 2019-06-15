from PIL import Image
import argparse

class ImageComposite:
	def __init__(self):
		self.output_width = 800
		self.output_height = 800
	def get_argument(self):
		parser = argparse.ArgumentParser();
		parser.add_argument("-p","--path",dest="img_path",help="path of the input image")
		parser.add_argument("-n","--name",dest="output_path",help="name of the output image")
		args = parser.parse_args()
		self.load_image(args.img_path,args.output_path)

	def load_image(self,img_path,output_path):
		self.output_path = output_path
		self.img = Image.open(img_path)
		self.img_width,self.img_height = self.img.size

	def set_background(self):
		self.background = Image.new("RGB",(self.output_width,self.output_height),(255,255,255))

	def get_new_size(self):
		aspect_ratio = float(self.img_width)/float(self.img_height)
		if self.img_height == self.img_width:
			return self.output_width,self.output_height
		elif self.img_height < self.img_width:
			return self.output_width,self.new_height(aspect_ratio)
		elif self.img_height > self.img_width:
			return self.new_width(aspect_ratio),self.output_height

	def new_height(self,aspect_ratio):
		width = float(self.output_width)
		height = width / aspect_ratio
		return int(height)

	def new_width(self,aspect_ratio):
		height = float(self.output_height)
		width = height * aspect_ratio
		return int(width)

	def get_offset(self,):
		_width,_height = self.get_new_size()
		width,height = self.background.size
		return ((width - _width) // 2 , (height - _height) // 2 )

	def save(self):
		self.get_argument()
		self.set_background()
		output_img = self.img.resize(self.get_new_size())
		self.background.paste(output_img,self.get_offset())
		self.background.save(self.output_path + ".jpg")

imgcmp = ImageComposite()
imgcmp.save()