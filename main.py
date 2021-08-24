#!/usr/bin/python
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

# sys.stdout.encoding = None
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color
# If we will not import this module 
# It will through the error 
from kivy.uix.slider import Slider 
from kivy.uix.checkbox import CheckBox

from kivy.utils import platform
from kivy.uix.popup import Popup
import logging
from kivy.logger import Logger
import datetime
import array as arr
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Loop = 0

class YourApp(App):

    def build(self):

        Loop=0

        LabelArr = [0 for x in range(30)]

#        Logger.critical("DEADBEEF10 = {}")
#        Logger.debug (" ***  DEADBEEF *** ")

        if platform == 'android':
            from android.storage import primary_external_storage_path
            Logger.critical ("android")
            # Get path to SD card Android
            theFtSize='14sp'
            ScreenHeight=1400
            
            AndPath=primary_external_storage_path()
            Logger.critical (AndPath)
#            FileLocation = os.path.join(AndPath, "/AndMyInfoFile.txt")
            FileLocation = AndPath + "/Elias/AndMyInfoFile.txt"
            Logger.critical (FileLocation)

        if platform == 'linux':
            Logger.critical ("linux")
            FileLocation="/home/Logs/MyInfoFile.txt"
            theFtSize='24sp'
            ScreenHeight=750

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
#            col_default_width=100,height=750)
        button_grid.bind(minimum_height=button_grid.setter('height'))

        # Insert the values into the grid
        Loop = 0
        for theButton in ButtonInfo:
#            print(theButton[0], Loop)
            LabelArr[Loop] = Label(text=str(CurCount[Loop]), 
                font_size=theFtSize,
                size_hint_x=None,
                width=50)
            button_grid.add_widget(
                LabelArr[Loop])
            ButtonText=theButton[0]
            button_grid.add_widget(Button(text=ButtonText,
                background_color=theButton[1],
                font_size=theFtSize,
                min_state_time=1,
                size_hint_x=None,
                width=245))
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

        # Write the value and date to the file.
        def print_button_text(instance):
 #           print("Button Pressed", instance)
 #           print("Logger.debug", instance)
            now = datetime.datetime.now()
            MyFile.write (now.strftime("%Y-%m-%d, "))
            MyFile.write (now.strftime("%H:%M:%S, "))
            MyFile.write (instance.text)
            MyFile.write ("\n\r")
            MyFile.flush()
            IncrementValue(instance.text)

        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)

        def print_slider_value(instance, value):
            print("Logger.debug", value)

        # Not used
        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height

        root_widget = ScrollView(size_hint=(1, 1), 
            size=(Window.width, Window.height))
#        root_widget.size = (480, 320)

        root_widget.add_widget(button_grid)

        return root_widget



# Color code to help organize
Drinks=[0,1.0,1.75,1]
Food=[0.8,0.1,0.6,1]
MedicineAM=[2.0,2.0,0.0,1]
MedicinePM=[0.0,0.0,1.5,1]
Medicine=[0.4,0.8,0.5,1]
Watch=[0.5,0.5,0.5,1]
Blank=[0.0,0.0,0.0,1]


CurCount = arr.array('I', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
ButtonInfo = [
            ('ACV', Drinks),
            ('Coffee', Drinks),
            ('Protein', Drinks),
            ('Psyllium', Drinks),
            ('Multi', MedicineAM),
            ('Atorvas', MedicineAM),
            ('Diltiazem', MedicineAM),
            ('Aspirin', MedicineAM),
            ('Calcium', MedicineAM),
            ('Singular', MedicinePM),
            ('Potass', MedicinePM),
            ('Resvera', MedicinePM),
            ('Melatonin', Medicine),
            ('Probi', Medicine),
            ('Hydrox', Medicine),
            ('VG', Medicine),
            ('Sunflower', Food),
            ('B-H', Watch),
            ('B-S', Watch),
            ('WorkO', Watch),
            # ('21', Blank),
            # ('22', Blank),
            # ('23', Blank),
            # ('24', Blank),
            # ('25', Blank),
            # ('26', Blank),
            # ('27', Blank),
            # ('28', Blank),
            ('29', Blank),
            ('30', Blank)
        ] 
# CurCount = array(20, dtype=int)

YourApp().run()
