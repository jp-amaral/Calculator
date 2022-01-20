# import kivy module
import kivy
import random 
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
 
# declaring the colours you can use directly also
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue =  [0, 0, 1, 1]
purple = [1, 0, 1, 1]
Window.size= (600,800)
# class in which we are creating the button
class Calculator(App):
    def build(self):
        superBox = BoxLayout(orientation ='vertical')
        HB = BoxLayout(orientation ='horizontal')
        self.screen = Label(text ="",font_size=90)
        HB.add_widget(self.screen)
        VB = GridLayout()
        VB.cols = 4
        butoes = []
        values = ["1","2","3","+","4","5","6","-","7","8","9","/","C","0","=","*"]
        for i in range(len(values)):
            color = '#00FFCE'
            if values[i] == "*" or values[i] == "/" or values[i] == "+" or values[i] == "-":
                color = '#0000CE'
            elif values[i] == "C":
                color = '#FF0000'
            elif values[i] == "=":
                color = '#00FF11'
            butoes.append(Button(text=values[i],size_hint = (0.2,0.2),bold = True,background_color = color))
            butoes[i].bind(on_press=self.callback)
            VB.add_widget(butoes[i])
 
        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        return superBox
    def callback(self,instance):
        if 'C' == instance.text:
            self.screen.text  = ""
        else:
            self.screen.text += instance.text
            if '=' in self.screen.text:
                self.screen.text += "result (?)"

root = Calculator()
root.run()