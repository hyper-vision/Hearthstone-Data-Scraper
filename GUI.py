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
	def build(self): # Overriding the built in build method in App
		self.layout = FloatLayout()

		self.searchField = TextInput(pos_hint={'x': 0, 'center_y': 0.08}, size_hint = (.7, .05), multiline = False)
		bLabels = ['Submit', 'Clear', 'Close']
		self.mainButtons = []
		self.mainContent = TextInput(pos_hint={'x': 0, 'center_y': 0.5 }, size_hint = (.7, .5), multiline = True, text = scraper.getWiki(), readonly = True, auto_indent = True, cursor_blink = False)
		self.img = AsyncImage(pos_hint = {'x': .35, 'center_y': 0.5}, source = scraper.getImg())

		for i in range(3):
			self.mainButtons.append(Button(pos_hint = {'x': .70 + (i * 0.1), 'center_y': 0.08}, size_hint=(.1, .05),text= bLabels[i]))
			self.layout.add_widget(self.mainButtons[i])

		self.layout.add_widget(self.searchField)
		self.layout.add_widget(self.mainContent)
		self.layout.add_widget(self.img)
		return self.layout

	def getText(self):
		# TODO: Use this function to get the text from the text entry field. Pass it to get image function in scrapper
		# then return the url and pass it to image widget, redraw image widget each time button is clicked with new
		# image. If empty, don't draw image widget (same applies for big entry).


if __name__ == "__main__":
	HelloApp().run() # Running an instance of HelloApp
