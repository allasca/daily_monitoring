# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: /home/allasca/buildozer/.buildozer/android/app/utils.py
# Compiled at: 2020-06-10 15:51:30
# Size of source mod 2**32: 385 bytes
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tab import MDTabsBase

class TabDash(ScrollView, MDTabsBase):
    pass


class TabForm(ScrollView, MDTabsBase):
    pass


class TabAbout(ScrollView, MDTabsBase):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass