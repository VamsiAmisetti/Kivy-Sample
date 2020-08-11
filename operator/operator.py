from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import re

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog=''
        self.cgpa=-1
        self.perc=-1
        self.backlogs=-1
        self.f_name=''
    def load_file(self):
        self.f_name=self.ids.file_name.text

    def getData(self):
        #info = self.ids.info
        students_container = self.ids.students
        prog=self.ids.prog_inp.text
        cgpa=self.ids.cgpa_inp.text
        perc=self.ids.perc_inp.text
        backlogs=self.ids.backlogs_inp.text
        if(prog=='' and cgpa=='' and perc=='' and backlogs==''):
            #info.text = '[color=#FF0000]Programme/CGPA/Percentage/No.of Backlogs are required[/color]'
            print('No Data Found')
        else:
            if(len(self.f_name)==0):
                print('Upload file first')
            else:
                cgpa=float(cgpa)
                perc=int(perc)
                backlogs=int(backlogs)
                details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top': 1})
                students_container.add_widget(details)
                

                rn = Label(text='17A81A0501\n17A81A0501',size_hint_x=.2,color=(.06,.45,.45,1))
                nn = Label(text='Vamsi Krishna\nVamsi Krishna',size_hint_x=.4,color=(.06,.45,.45,1))
                dd = Label(text='CSE\nCSE',size_hint_x=.1,color=(.06,.45,.45,1))
                cg = Label(text=str(cgpa)+'\n'+str(cgpa),size_hint_x=.1,color=(.06,.45,.45,1))
                pr = Label(text=str(perc)+'\n'+str(perc),size_hint_x=.1,color=(.06,.45,.45,1))
                bl = Label(text=str(backlogs)+'\n'+str(backlogs),size_hint_x=.1,color=(.06,.45,.45,1))

                details.add_widget(rn)
                details.add_widget(nn)
                details.add_widget(dd)
                details.add_widget(cg)
                details.add_widget(pr)
                details.add_widget(bl)

class OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__=="__main__":
    oa = OperatorApp()
    oa.run()