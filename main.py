#!/usr/bin/python3
#---------------------------------------------------------------------
#
#	File: 	main
#
#	Contains: 	
#
#
#	Written By: 	Elias Keshishoglou on Mon Feb 1 05:03:36 PM PST 2021
#
#	Copyright : 	2021 Elias Keshishoglou all rights reserved.
#
#
#---------------------------------------------------------------------#
import sys; 
import os 
from kivy.app import App


from kivy.core.window import Window
from kivy.config import Config
# Config.set('graphics', 'fullscreen', '0')
# Config.set('graphics', 'fullscreen', 'false')
# Config.set('graphics', 'window_state', 'maximized')
# Config.set('graphics', 'width', 320)
# Config.set('graphics', 'height', '240')
# Config.set('graphics', 'fullscreen', 'fake')
# Window.fullscreen = 0
# Window.size = (600, 500)

# Config.write()


from kivy.uix.dropdown import DropDown
import array as arr
from kivy.utils import platform
from kivy.logger import Logger
from kivy.uix.button import Button
import datetime
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
# from kivy.uix.recycleview import ScrollView
# from kivy.uix.modelview import ScrollView



# from kivy.uix.screenmanager import ScreenManager, Screen
# sm = ScreenManager()
# for i in range(4):
#     screen = Screen(name='Title %d' % i)
#     sm.add_widget(screen)
# sm.current = 'Title 2'


# debug

# from kivy.lang.builder import Builder
# from kivy.uix.floatlayout import FloatLayout
# from kivymd.app import MDApp
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

# class MainScreen(Screen):
#     pass

# class AnotherScreen(Screen):
#     pass

# class ScreenManagement(ScreenManager):
#     pass

# presentation = Builder.load_file("mainspec.kv")

# class MainApp(App):
#     def build(self):
#         return presentation


# sys.stdout.encoding = None
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# 
# from kivy.graphics import Color
# # If we will not import this module 
# # It will through the error 
# from kivy.uix.slider import Slider 
# from kivy.uix.checkbox import CheckBox

# from kivy.uix.popup import Popup
# import logging
# 
# 
#

Loop = 0
dropdownNumbers = DropDown()
NumbersList = ["1","2","3","4","5"]
NumbersListMax = 5

NonePopup=0
NumberPopup=1

class YourApp(App):

    def build(self):
        # Config.set('graphics', 'fullscreen', 'false')
        # Config.set('graphics', 'window_state', 'maximized')
        # Config.write()

        Loop=0
        LabelArr = [0 for x in range(200)]
#        Logger.critical("DEADBEEF10 = {}")
        Logger.debug (" ***  DEADBEEF *** ")

        if platform == 'android':
            from android.storage import primary_external_storage_path
            
            Logger.critical ("*** android")
            # Get path to SD card Android
            theFtSize='12sp'
            ScreenHeight=2000
            
            AndPath=primary_external_storage_path()
            Logger.critical (AndPath)
#            FileLocation = os.path.join(AndPath, "/AndMyInfoFile.txt")
            FileLocation = AndPath + "/Elias/AndMyInfoFile.txt"
            Logger.critical (FileLocation)

        if platform == 'linux':
            Logger.critical ("In linux")
            FileLocation="/home/Logs/MyInfoFile.txt"
            theFtSize='24sp'
            ScreenHeight=750

#        plyer.notification.notify(title='test',timeout=10, \
#            message="Notification using plyer")

#        def show_selected_value(spinner, text):
        def show_selected_value(instance):
            global LastPressed
            ReturnValue=dropdownNumbers.select(instance)
#            print(ButtonInfo[LastPressed][0]);
#            print('The show_selected_value', instance.text)
            now = datetime.datetime.now()
            MyFile.write (now.strftime("%Y-%m-%d, "))
            MyFile.write (now.strftime("%H:%M:%S, "))
            MyFile.write (ButtonInfo[LastPressed][0])
            Logger.debug ("show_selected_value ", instance.text)

            MyFile.write (", ")
            MyFile.write (instance.text)
            MyFile.write ("\n\r")
            MyFile.flush()

        def numPopup(instance):
            global LastPressed
            ReturnValue=dropdownNumbers.open(instance)
#            print("numPopup ",instance.text)
            theIndex=instance.color[3]-1
            LastPressed=theIndex
            IncrementValue(instance.text)

#            print("numPopup Index", ButtonInfo[theIndex][2])

        for i in range(NumbersListMax): 
            indiv_op = Button(text = NumbersList[i], 
                size_hint_y = None, 
                height = 100,
                font_size=theFtSize,
                background_color=[0,0,0,1],
                color=[1,1,1,1])  
            indiv_op.bind(on_press = show_selected_value) 
            dropdownNumbers.add_widget(indiv_op) 

        # Write the value and date to the file.
        def print_button_text(instance):
            global LastPressed

#            print("Button Pressed", instance.text)
            theIndex=instance.color[3]-1
            LastPressed=theIndex
#            print("Button Pressed", ButtonInfo[theIndex][2])
 #           print("Logger.debug", instance)
            now = datetime.datetime.now()
            MyFile.write (now.strftime("%Y-%m-%d, "))
            MyFile.write (now.strftime("%H:%M:%S, "))
            MyFile.write (instance.text)
            Logger.debug ("print_button_text ", instance.text)
            MyFile.write (", -1, \n\r")
            MyFile.flush()
            IncrementValue(instance.text)

        # Load the values from the same date
        # in case the app closed.
        def ReadFile(FileName):
            now = str(datetime.datetime.now().strftime("%Y-%m-%d, "))

            try:
                MyFile= open(FileName,"r")
            except: 
                return
            
            for line in MyFile:
                if now in line:
                    theIndex=0
                    for Item in ButtonInfo:
                        if (Item[0] in line):
                            CurCount[theIndex]+=1
#                            print("Found ",Item, CurCount[theIndex])
                        theIndex+=1

#            print(CurCount)
            MyFile.close()   
            # CurCount

        # Update the counts
        ReadFile(FileLocation)

        # Open the file for writing and
        # insert the date.
        now = datetime.datetime.now()
        MyFile= open(FileLocation,"a+")
        MyFile.write (now.strftime("%Y-%m-%d, "))
        MyFile.write (now.strftime("%H:%M:%S, "))
        MyFile.write ("App Start")
        MyFile.write ("\n\r")
        
        # Create the grid
        # 2 number column and 2 text.
        button_grid = GridLayout(cols=4, size_hint=(None, None),
            col_default_width=100,height=ScreenHeight)
        button_grid.bind(minimum_height=button_grid.setter('height'))

        # Insert the values into the grid
        Loop = 0
        for theButton in ButtonInfo:
#            print(theButton[0], Loop)
            LabelArr[Loop] = Label(text=str(CurCount[Loop]), 
                font_size=theFtSize,
                size_hint_x=None,
                width=100)
            button_grid.add_widget(
                LabelArr[Loop])
            ButtonText=theButton[0]

            if (theButton[2] == NonePopup):
                myButton = Button(text=ButtonText,
                background_color=theButton[1],
                color=[1,1,1,Loop+1],
                font_size=theFtSize,
                min_state_time=1,
                size_hint_x=None,
                width=400)
                myButton.bind(on_press=print_button_text)

            if (theButton[2] == NumberPopup):
                myButton = Button(text=ButtonText,
                background_color=theButton[1],
                color=[1,1,1,Loop+1],
                font_size=theFtSize,
                min_state_time=1,
                size_hint_x=None,
                width=400, 
                on_press=numPopup)
                myButton.bind(on_press=numPopup)

            button_grid.add_widget(myButton)
            Loop += 1

        # Not used
        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')

        # Given the text up the count 
        def IncrementValue(ButtonText):
            global Loop
            Loop = 0
            for theButton in ButtonInfo:
                if ( theButton[0] == ButtonText ):
                    CurCount[Loop] = CurCount[Loop] + 1
                    LabelArr[Loop].text=str(CurCount[Loop])
                Loop += 1


#        for button in button_grid.children[1:]:
#            button.bind(on_press=print_button_text)


        def print_slider_value(instance, value):
            print("Logger.debug", value)

        # Not used
        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height

        root_widget = ScrollView(size_hint=(1, 1), 
           size=(Window.width, Window.height))
#        root_widget = ModalView(size_hint=(1, 1), 
#            size=(Window.width, Window.height))
#        root_widget.size = (480, 320)

        root_widget.add_widget(button_grid)

        return root_widget

# Color code to help organize
Drinks=[0,1.0,1.75,1]
Food=[0.8,0.1,0.6,1]
MedicineAM=[2.0,2.0,0.0,1]
MedicinePM=[2.0,1.0,0.0,1]
Shared=[1.0,0.0,1.5,1]
Medicine=[0.4,0.8,0.5,1]
Watch=[0.5,0.5,0.5,1]
Workout=[0.2,0.0,1.0,1]
Blank=[0.0,0.0,0.0,1]
LastPressed=0

CurCount = arr.array('I', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
ButtonInfo = [
            ('Coffee',          Drinks,     NonePopup    ),
            ('Kombucha',        Drinks,     NonePopup    ),
            ('Water',           Drinks,     NonePopup    ),
            ('Soda',            Drinks,     NonePopup    ),
            ('Wine',            Drinks,     NonePopup    ),
            ('Beer',            Drinks,     NonePopup    ),
            ('Multi',           MedicineAM, NonePopup    ),
            ('Atorvas_10mg',    MedicineAM, NonePopup    ),
            ('Diltiazem_120mg', MedicineAM, NonePopup    ),
            ('Aspirin_83mg',    MedicineAM, NonePopup    ),
            ('Psyllium',        Shared,     NonePopup    ),
            ('Probi',           Shared,     NonePopup    ),
            ('Losartan_25mg',   MedicinePM, NonePopup    ),
            ('Singular_10mg',   MedicinePM, NonePopup    ),
            ('Transresveratol', MedicinePM, NonePopup    ),
            ('Melatonin_3mg',   Medicine,   NonePopup    ),
            ('Hydrox_10mg',     Medicine,   NonePopup    ),
            ('Calcium',         Medicine,   NonePopup    ),
            ('VG',              Medicine,   NonePopup    ),
            ('BM',              Watch,      NumberPopup  ),
            ('Nuts',            Food,       NonePopup    ),
            ('Tsoureki',        Food,       NonePopup    ),
            ('Chips',           Food,       NonePopup    ),
            ('ChestPress',      Workout,    NonePopup    ),
            ('ChestPull',       Workout,    NonePopup    ),
            ('Lower Back',      Workout,    NonePopup    )
        ] 
# NumberPopup
# CurCount = array(20, dtype=int)

if __name__ == "__main__":
    YourApp().run()
