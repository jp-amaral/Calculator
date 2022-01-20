import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size= (400,600)
class Calculator(App):
    def build(self):
        self.notnumber = 0
        superBox = BoxLayout(orientation ='vertical')
        HB = BoxLayout(orientation ='horizontal')
        self.array = []
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
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        return superBox
    def callback(self,instance):
        if 'C' == instance.text:
            self.screen.text  = ""
        elif '=' == instance.text:
            self.CalcMath()
        else:
            self.array.append(instance.text)
            print(self.array)
            try:
                int(instance.text)
                #print("number")
                if self.notnumber == 1:
                    self.screen.text = ""
                    self.notnumber = 0
                self.screen.text += instance.text
            except:
                self.screen.text = instance.text
                #print("not number")
                self.notnumber = 1
                
    def CalcMath(self):
        pass

root = Calculator()
root.run()