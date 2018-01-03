from kivy.app import App # Required for any Kivy application
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivy.uix.image import AsyncImage

import scraper

class HelloApp(App): # build returns window content, here Label
	def clearSearch(self, argx):
		self.searchField.text = ""

	def submit(self, argx):
		print(self.searchField.text)
		try:
			try:
				self.layout.remove_widget(self.img)
			except Exception as e:
				print(e)
			self.img = AsyncImage(pos_hint = {'x': .35, 'center_y': 0.5}, source = scraper.getImg(self.searchField.text))
			self.layout.add_widget(self.img)
		except Exception as e:
			print(e)

	def close(self, argx):
		App.get_running_app().stop()

	def build(self): # Overriding the built in build method in App
		self.layout = FloatLayout()

		self.searchField = TextInput(pos_hint={'x': 0, 'center_y': 0.08}, size_hint = (.7, .05), multiline = False)
		bProperties = {'Labels' : ['Submit', 'Clear', 'Close'],
					   'Functions' : [self.submit, self.clearSearch, self.close]}

		self.mainButtons = []
		self.mainContent = TextInput(pos_hint={'x': 0, 'center_y': 0.5 }, size_hint = (.7, .5), multiline = True, text = scraper.getWiki(), readonly = True, auto_indent = True, cursor_blink = False)

		for i in range(3):
			self.mainButtons.append(Button(pos_hint = {'x': .70 + (i * 0.1), 'center_y': 0.08}, size_hint=(.1, .05),text= bProperties['Labels'][i]))
			self.mainButtons[i].bind(on_press = bProperties['Functions'][i])
			self.layout.add_widget(self.mainButtons[i])

		self.layout.add_widget(self.searchField)
		self.layout.add_widget(self.mainContent)

		return self.layout



	# def getText(self):
	# 	# TODO: Use this function to get the text from the text entry field. Pass it to get image function in scrapper
	# 	# then return the url and pass it to image widget, redraw image widget each time button is clicked with new
	# 	# image. If empty, don't draw image widget (same applies for big entry).
	# 	pass

if __name__ == "__main__":
	HelloApp().run() # Running an instance of HelloApp
