# import kivy module
import re
from cv2 import exp
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

Window.size = (600, 800)

# class in which we are creating the button
class Calculator(App):
       
    def build(self):
 
        self.numbers = [1,2,3,4,5,6,7,8,9,0]
        self.operators = ['/', '*', '+', '-']
        self.regexPattern = '|'.join(map(re.escape, self.operators))
        self.input = []
        self.result = 0
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets 
        superBox = BoxLayout(orientation ='vertical')
 
        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation ='horizontal')
        
 
        colors = [red, green, blue, purple]
         
        # styling the button boxlayout
        self.screen = Label(text ="", color="#00FFCE", font_size=90)
 
        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(self.screen)
 
        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = GridLayout()
        VB.cols = 4
        butoes = []
        values = ["1","2","3","+","4","5","6","-","7","8","9","/","C","0","=","*"]
        color = '#8a8a8a'
        for i in range(len(values)):
            butoes.append(Button(text=values[i],size_hint = (0.2,0.2),bold = True,background_color = color))
            butoes[i].bind(on_press=self.callback)
            VB.add_widget(butoes[i])
 
        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)
 
        return superBox
        
    def callback(self,instance):
        if instance.text != '=':
            self.input.append(instance.text)
        print(self.input)
        try:
            int(instance.text)
            if self.input[-2] in self.operators:
                self.screen.text = ""
            self.screen.text += instance.text
        except:
            self.screen.text = instance.text
        if instance.text == 'C':
            self.input = []
            self.screen.text = ""
        if instance.text == '=':
            expr = ''.join([str(elem) for elem in self.input])
            self.result = self.calcResult(expr)
            self.input = []
            self.input.append(self.result)
            self.fresh_result = 1
            self.screen.text = str(self.result)
        
        return instance.text

    def calcResult(self, expr):
        print(expr)
        operators = []
        for char in expr:
            if char in self.operators:
                operators.append(char)
        tokens = re.split(self.regexPattern, expr)
        print(tokens)
        print(operators)

        while(len(tokens) != 1):
            
            for i in range(len(operators)):
                if operators[i] == '/' or operators[i] == '*':
                    print("mult or div")
                    op = operators[i]
                    operators.pop(i)
                    a = int(tokens.pop(i))
                    b = int(tokens.pop(i))
                    if op == '/':result = a // b
                    if op == '*':result = a*b
                    tokens.insert(i, str(result))
                    break
            print(tokens)
            print(operators)
            if ('/' not in operators and '*' not in operators) and len(operators)>0:
                print("add or sub")
                for i in range(len(operators)):
                    if operators[i] == '+' or operators[i] == '-':
                        op = operators.pop(i)
                        a = int(tokens.pop(i))
                        b = int(tokens.pop(i))
                        if op == '+':result = a + b
                        if op == '-':result = a-b
                        tokens.insert(i, str(result))
                        break
        
        return tokens[0]

# creating the object root for BoxLayoutApp() class 
root = Calculator()
   
# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()