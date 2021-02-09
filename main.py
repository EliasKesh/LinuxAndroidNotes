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


class YourApp(App):
    def build(self):
        
        # root_folder = self.user_data_dir
        # cache_folder = os.path.join(root_folder, 'cache')

        Logger.critical("DEADBEEF = {}")
        Logger.debug (" ***  DEADBEEF *** ")
        root_widget = BoxLayout(orientation='vertical')

        if platform == 'android':
            Logger.debug ("android")
            # Get path to SD card Android
            theFtSize='18sp'
            FileLocation="AndMyInfoFile.txt"

        if platform == 'linux':
            Logger.debug ("linux")
            FileLocation="/home/Logs/MyInfoFile.txt"
            theFtSize='24sp'

        MyFile= open(FileLocation,"a+")
        now = datetime.datetime.now()
        MyFile.write ("Current date and time : ")
        MyFile.write (now.strftime("%Y-%m-%d %H:%M:%S"))
        MyFile.write ("\n\r")

#        ButtonInfo = namedtuple('Name', 'Color')

        Drinks=[1.0,0.1,0.5,1]
        Food=[0.8,0.1,0.6,1]
        Medicine=[0.4,0.9,0.6,1]
        Watch=[0.5,0.5,0.5,1]
        ButtonInfo = [
                    ('Soda', Drinks),
                    ('Stream', Drinks),
                    ('Coffee', Drinks),
                    ('Sunflower', Food),
                    ('Chips', Food),
                    ('VG', Medicine),
                    ('NicGum', Medicine),
                    ('Probi', Medicine),
                    ('Hydrox', Medicine),
                    ('BM-H', Watch),
                    ('BM-M', Watch),
                    ('BM-S', Watch),
                    ('WorkO', Watch),
                    ('14', [0.0,0.0,0.0,1]),
                    ('15', [0.0,0.0,0.0,1]),
                    ('16', [0.0,0.0,0.0,1]),
                    ('17', [0.0,0.0,0.0,1]),
                    ('18', [0.0,0.0,0.0,1]),
                    ('19', [0.0,0.0,0.0,1]),
                    ('20', [0.0,0.0,0.0,1])
                ] 

        button_grid = GridLayout(cols=2, size_hint_y=2)

        for theButton in ButtonInfo:
            print(theButton[0])
            button_grid.add_widget(Button(text=theButton[0],
                background_color=theButton[1],
                font_size=theFtSize))

        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')

#        checkbox = CheckBox()
#        checkbox.bind(active=on_checkbox_active)


        def print_button_text(instance):
            print("Logger.debug", instance.text)
            now = datetime.datetime.now()
            MyFile.write (now.strftime("%Y-%m-%d %H:%M:%S, "))
            MyFile.write (instance.text)
            MyFile.write ("\n\r")
            MyFile.flush()

        for button in button_grid.children[1:]:  # note use of the
                                              # `children` property
            button.bind(on_press=print_button_text)
 #           print ("button")

        def print_slider_value(instance, value):
            print("Logger.debug", value)


        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height

        root_widget.add_widget(button_grid)

        return root_widget


YourApp().run()
