import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GitApp(GridLayout):
    def __init__(self, **kwargs):
        super(GitApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Employee Name'))
        self.e_name = TextInput()
        self.add_widget(self.e_name)
        
        self.add_widget(Label(text='Employee Role'))
        self.e_role = TextInput()
        self.add_widget(self.e_role)
        
        self.add_widget(Label(text='Employee Gender'))
        self.e_gender = TextInput()
        self.add_widget(self.e_gender)
        
        self.press = Button(text='Click Here')
        self.press.bind(on_press=self.click_here)
        self.add_widget(self.press)
        
    def click_here(self, instance):
        print("Name of Employee is "+self.e_name.text)
        print("Role of Employee is "+self.e_role.text)
        print("Gender of Employee is "+self.e_gender.text)
        print("")
        
        
       
class  parentApp(App):
    def build(self):
        return GitApp()
    
if __name__ == "__main__":
    parentApp().run()