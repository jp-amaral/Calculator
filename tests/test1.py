from tkinter import Button
from turtle import position
from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

 
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', False)
 
# fix the width of the window
Config.set('graphics', 'width', '500')
 
# fix the height of the window
Config.set('graphics', 'height', '600')
# import kivy module
import kivy
 
# this restrict the kivy version i.e
# below this kivy version you cannot use the app
kivy.require("1.9.1")
 
# defining the App class
class Calculator(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 4
        self.window.cols_minimum = {0: 100, 1: 100, 2: 100, 3: 100, 4: 100}
        #self.label = Label(text ="Calculator",font_size ='20sp', markup = True,pos_hint={'center_x':0.5,'center_y':0.95})
        self.btn0 = Button(text="1",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE')
        self.btn1 = Button(text="2",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE')
        self.btn2 = Button(text="3",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn10 = Button(text="9",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn3 = Button(text="/",size_hint = (0.2,0.2),bold = True,background_color = '#00FF00') 
        self.btn4 = Button(text="4",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn5 = Button(text="5",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn6 = Button(text="6",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn8 = Button(text="7",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn9 = Button(text="8",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE') 
        self.btn7 = Button(text="+",size_hint = (0.2,0.2),bold = True,background_color = '#00FF00') 
        self.btn11 = Button(text="-",size_hint = (0.2,0.2),bold = True,background_color = '#00FF00') 
        self.btn15 = Button(text="/",size_hint = (0.2,0.2),bold = True,background_color = '#00FF00') 
        self.btn13 = Button(text="0",size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE')
        self.btn14 = Button(text="=",size_hint = (0.2,0.2),bold = True,background_color = '#00BBCE') 
        self.btn12 = Button(text="C",size_hint = (0.2,0.2),bold = True,background_color = '#FF0000') 


        #self.window.add_widget(self.label)
        self.window.add_widget(self.btn0)
        self.window.add_widget(self.btn1)
        self.window.add_widget(self.btn2)
        self.window.add_widget(self.btn3)
        self.window.add_widget(self.btn4)
        self.window.add_widget(self.btn5)
        self.window.add_widget(self.btn6)
        self.window.add_widget(self.btn7)
        self.window.add_widget(self.btn8)
        self.window.add_widget(self.btn9)
        self.window.add_widget(self.btn10)
        self.window.add_widget(self.btn11)
        self.window.add_widget(self.btn12)
        self.window.add_widget(self.btn13)
        self.window.add_widget(self.btn14)
        self.window.add_widget(self.btn15)

        return self.window
# creating the object
window = Calculator()
 
if __name__ == "__main__":
    Calculator().run()