import numpy
import Pillow
import cv2

class kanjitotext(object):
	"""description goes here"""

	@staticmethod
	def to_text_one(s: str) -> str:
		""" 
		Takes one character and returns a text art version. 
		"""
		# typical usage:
		img = self._text_to_img(s)
		text_array = self._img_to_text_array(img)
		art = self._text_array_to_text(text_array)
		return art

	def _text_to_img(self, s: str):
		"""
		Takes one character and returns an image of that text.
		"""
		pass

	def _img_to_text_array(self, img):
		"""
		Divide image into grids and create an output array of the same size as grid
		"""
		pass

	def _text_array_to_text(self, text):
		"""
		Turn output array into text
		"""
		pass

if __name__ == '__main__':
	# typical usage:
	art = kanjitotext.to_text_one("字")
	print(art)