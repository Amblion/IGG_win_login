#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}
import IGG_win_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  IGG_win:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.configure_event = None
        self.isTKroot = isTKroot
        self.firstRun = True
        self.rootZoomed = False
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.Register(uiName,'root',root)
        style = IGG_win_sty.SetupStyle(isTKroot)
        self.UIJsonString ='{"Version": "1.0.0", "UIName": "IGG_win", "Description": "", "WindowSize": [423, 435], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": false, "WindowTitle": "IGG账户获取 v2025052201", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": false, "MinSize": [0, 0], "ResolutionScaling": true, "PopupDebugDialog": false, "TransparentColor": null, "RootTransparency": 255, "ICOFile": "Resources/ico.ico", "ICOMode": "File", "WinState": 1, "WinTopMost": true, "BGColor": "#EFEFEF", "GroupList": {"Group_1": "1"}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#EFEFEF", "Size": [423, 435], "PlaceInfo": null, "EventList": {"Load": "Form_1_onLoad"}}, {"Type": "Button", "Index": 8, "AliasName": "Button_1", "ParentName": "Form_1", "Layer": "lift", "PlaceInfo": [226, 29, 94, 43, "nw", true, false], "Visible": true, "Size": [100, 46], "BGColor": "#EFEFEF", "Text": "获取账户", "FGColor": "#000000", "Relief": "raised", "EventList": {"Command": "Button_1_onCommand"}}, {"Type": "Button", "Index": 11, "AliasName": "Button_2", "ParentName": "Form_1", "PlaceInfo": [277, 372, 113, 29, "nw", true, false], "Visible": true, "Size": [120, 31], "BGColor": "#EFEFEF", "Text": "保存", "FGColor": "#000000", "Relief": "raised", "EventList": {"Command": "Button_2_onCommand"}}, {"Type": "Button", "Index": 21, "AliasName": "Button_3", "ParentName": "Form_1", "PlaceInfo": [211, 373, 55, 29, "nw", true, false], "Visible": true, "Size": [59, 31], "BGColor": "#EFEFEF", "Text": "清空", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_3_onCommand"}}, {"Type": "ListBox", "Index": 9, "AliasName": "ListBox_1", "ParentName": "Form_1", "PlaceInfo": [12, 12, 189, 60, "nw", true, false], "Visible": true, "Size": [200, 64], "ExportSelection": 1, "BGColor": "#FFFFFF", "SelectMode": "BROWSE", "EventList": {"Double-Button-1": "ListBox_1_onDoubleButton1"}}, {"Type": "ListBox", "Index": 10, "AliasName": "ListBox_2", "ParentName": "Form_1", "PlaceInfo": [9, 104, 381, 262, "nw", true, false], "Visible": true, "Size": [403, 278], "ExportSelection": 1, "BGColor": "#FFFFFF", "SelectMode": "EXTENDED", "EventList": {"Double-Button-1": "ListBox_2_onDoubleButton1", "ListboxSelect": "ListBox_2_onSelect"}, "ScrollBarList": [false, true]}, {"Type": "Label", "Index": 3, "AliasName": "Label_1", "ParentName": "Form_1", "Layer": "lower", "PlaceInfo": [-30, 82, 477, 22, "nw", true, false], "Visible": true, "Size": [505, 24], "BGColor": "#EFEFEF", "Text": "----------------------------------------历史账户-------------------------------------------", "FGColor": "#000000"}, {"Type": "Label", "Index": 16, "AliasName": "Label_2", "ParentName": "Form_1", "Layer": "lower", "PlaceInfo": [226, -4, 146, 45, "nw", true, false], "Visible": true, "Size": [155, 48], "BGColor": "#EFEFEF", "Text": "剩余账户：", "FGColor": "#000000", "Anchor": "w", "EventList": {}}, {"Type": "Label", "Index": 17, "AliasName": "Label_3", "ParentName": "Form_1", "PlaceInfo": [12, 372, 137, 28, "nw", true, false], "Visible": true, "Size": [145, 30], "BGColor": "#EFEFEF", "Text": "当前账号数 0 个", "FGColor": "#000000", "Anchor": "w", "Font": ["Microsoft YaHei UI", 9, "normal", "roman", 0, 0]}, {"Type": "Label", "Index": 20, "AliasName": "Label_4", "ParentName": "Form_1", "Layer": "lower", "PlaceInfo": [2, 0, 395, 105, "nw", true, false], "Visible": true, "Size": [418, 112], "BGColor": "#EFEFEF", "Text": "", "FGColor": "#000000"}, {"Type": "SpinBox", "Index": 22, "AliasName": "SpinBox_1", "ParentName": "Form_1", "PlaceInfo": [330, 29, 56, 45, "nw", true, false], "Visible": true, "Size": [60, 48], "BGColor": "#FFFFFF", "From": 1.0, "To": 99999.0, "Increment": 1.0, "Wrap": 0, "Value": "1", "EventList": {}}]}'
        Form_1 = Fun.CreateUIFormJson(uiName,root,isTKroot,style,self.UIJsonString,False)
        #Inital all element's Data 
        Fun.LoadCanvasRecord(uiName,0.9456264775413712)
        #Call Form_1's OnLoad Function
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Configure>', self.Configure)
            if self.rootZoomed == True and isinstance(self.root,tkinter.Tk) == True:
                self.root.state("zoomed")
                Fun.SetUIState(uiName,"zoomed")
                self.rootZoomed = False
            
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName,0,'')

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget and (self.configure_event is None or self.configure_event[2]!= event.width or self.configure_event[3]!= event.height):
            uiName = self.uiName
            self.configure_event = [event.x,event.y,event.width,event.height]
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            pass
    def ExecuteCode(self,CodeText):
        exec(CodeText)
