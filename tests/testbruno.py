# import kivy module
import kivy
import random 
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
 
# declaring the colours you can use directly also
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue =  [0, 0, 1, 1]
purple = [1, 0, 1, 1]
   
# class in which we are creating the button
class BoxLayoutApp(App):
       
    def build(self):
 
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets 
        superBox = BoxLayout(orientation ='vertical')
 
        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation ='horizontal')
 
        colors = [red, green, blue, purple]
         
        # styling the button boxlayout
        screen = Label(text ="Screen")
 
        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(screen)
 
        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = GridLayout()
        VB.cols = 4
        butoes = []
        values = ["1","2","3","4","5","6","7","8","9","0","=","/","*","+","-"]
        for i in range(15):
            butoes.append(Button(text=values[i],size_hint = (0.2,0.2),bold = True,background_color = '#00FFCE'))
            VB.add_widget(butoes[i])
 
        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)
 
        return superBox
 
# creating the object root for BoxLayoutApp() class 
root = BoxLayoutApp()
   
# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()