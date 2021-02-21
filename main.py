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

Loop = 0

class YourApp(App):

    def build(self):
        Loop=0

        CurCount = arr.array('I', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        LabelArr = [0 for x in range(20)]

        Logger.critical("DEADBEEF10 = {}")
        Logger.debug (" ***  DEADBEEF *** ")

        if platform == 'android':
            from android.storage import primary_external_storage_path
            Logger.critical ("android")
            # Get path to SD card Android
            theFtSize='18sp'
            
            AndPath=primary_external_storage_path()
            Logger.critical (AndPath)
#            FileLocation = os.path.join(AndPath, "/AndMyInfoFile.txt")
            FileLocation = AndPath + "/Elias/AndMyInfoFile.txt"
            Logger.critical (FileLocation)

        if platform == 'linux':
            Logger.critical ("linux")
            FileLocation="/home/Logs/MyInfoFile.txt"
            theFtSize='24sp'

        MyFile= open(FileLocation,"a+")
        now = datetime.datetime.now()
        MyFile.write (now.strftime("%Y-%m-%d, "))
        MyFile.write (now.strftime("%H:%M:%S, "))
        MyFile.write ("App Start")
        MyFile.write ("\n\r")
        root_widget = BoxLayout(orientation='vertical')

        button_grid = GridLayout(cols=4, 
            col_default_width=100)

        Loop = 0
        for theButton in ButtonInfo:
            print(theButton[0], Loop)
            LabelArr[Loop] = Label(text=str(CurCount[0]), 
                font_size=theFtSize,
                size_hint_x=None,
                width=90)
            button_grid.add_widget(
                LabelArr[Loop])
            ButtonText=theButton[0]
            button_grid.add_widget(Button(text=ButtonText,
                background_color=theButton[1],
                font_size=theFtSize,
                min_state_time=1,
                size_hint_x=None,
                width=275))
            Loop += 1


        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')

        def IncrementValue(ButtonText):
            global Loop
            Loop = 0
            for theButton in ButtonInfo:
                if ( theButton[0] == ButtonText ):
                    CurCount[Loop] = CurCount[Loop] + 1
                    LabelArr[Loop].text=str(CurCount[Loop])
                Loop += 1

        def print_button_text(instance):
            print("Button Pressed", instance)
            print("Logger.debug", instance)
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


        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height

        root_widget.add_widget(button_grid)

        return root_widget



Drinks=[1.0,0.2,0.2,1]
Food=[0.8,0.1,0.6,1]
Medicine=[0.4,0.9,0.6,1]
Watch=[0.5,0.5,0.5,1]
Blank=[0.0,0.0,0.0,1]
ButtonInfo = [
            ('Soda', Drinks, 0),
            ('Stream', Drinks, 1),
            ('Coffee', Drinks, 2),
            ('Protein', Drinks, 3),
            ('Sunflower', Food, 0),
            ('Chips', Food, 0),
            ('VG', Medicine, 0),
            ('NicGum', Medicine, 0),
            ('Probi', Medicine, 0),
            ('Hydrox', Medicine, 0),
            ('BM-H', Watch, 0),
            ('BM-M', Watch, 0),
            ('BM-S', Watch, 0),
            ('WorkO', Watch, 0),
            ('15', Blank, 0),
            ('16', Blank, 0),
            ('17', Blank, 0),
            ('18', Blank, 0),
            ('19', Blank, 0),
            ('20', Blank, 0)
        ] 
# CurCount = array(20, dtype=int)

YourApp().run()
