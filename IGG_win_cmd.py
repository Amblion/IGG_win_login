#coding=utf-8
import sys
import threading
import os
import multiprocessing
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import pyperclip
import Fun
import smbclient
uiName="IGG_win"
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 


flag = True
def find_zhanghu2():
    zhanghu_list = []
    with smbclient.open_file(r"\\192.168.6.218\\技术部\\网络\\维京\\IGG通行证.txt") as f:
        line_count = 0    
        for line in f:
            line_count += 1
            line = line.replace("\n","")
            new_line = line.split("----")
            if new_line[2] == '0':
                zhanghu_list.append("%s----%s"%(new_line[0],new_line[1]))
                break
    if len(zhanghu_list) != 0:
        set_zhanghu2(new_line,line_count)
        return zhanghu_list   
    return -1      

def set_zhanghu2(new_line,line_count):
    with smbclient.open_file(r"\\192.168.6.218\技术部\网络\维京\IGG通行证.txt") as f:
        lines = f.readlines()
    lines[line_count-1] = "%s----%s----%s\n"%(new_line[0],new_line[1],1)
    with smbclient.open_file(r"\\192.168.6.218\技术部\网络\维京\IGG通行证.txt", mode='w') as file:
        file.writelines(lines)


def get_zhanghu_num():
    global flag
    line_count = 0 
    if flag:
        flag = False
        with smbclient.open_file(r"\\192.168.6.218\技术部\网络\维京\IGG通行证.txt") as f:
            for line in f:
                line = line.replace("\n","")
                new_line = line.split("----")
                if new_line[2] == '0':
                    line_count += 1
        flag = True
    return line_count
    
zhanghu = ""
zhanghu_index = 0
zhanghu_num = 0
def set_num(uiName):
    global flag
    while True:
        try:
            sss = get_zhanghu_num()
            if sss != 0:
                Fun.SetText(uiName,'Label_2',"剩余账户：%s" %(sss))
            Fun.SetText(uiName,'Label_3',"当前账户数 %s 个"%(zhanghu_index))
        except Exception as Ex:
            flag  = True
        Fun.Sleep(0.5)    

def writeUpgrade(exe_name):
    img_path = 'C:\\updata\\'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    b = open("C:\\updata\\upgrade.bat",'w')
    TempList = "@echo off\n"
    TempList += "if not exist "+r"\\192.168.6.218\\维京崛起\\其它\\工具版本热更新(非专业勿动勿删)\\IGG账户获取\\" + exe_name + " exit \n"  #判断是否有新版本的程序，没有就退出更新。
    TempList += "echo 正在更新至最新版本...\n"
    TempList += "timeout /t 10 /nobreak\n"  #等待10秒
    TempList += "del " + os.path.realpath(exe_name) + "\n" #删除旧程序
    TempList += "copy "+r"\\192.168.6.218\\维京崛起\\其它\\工具版本热更新(非专业勿动勿删)\\IGG账户获取\\" + exe_name + " " + exe_name + '\n' #复制新版本程序
    TempList += "echo 更新完成\n"
    TempList += "timeout /t 3 /nobreak\n"
    TempList += "exit"
    b.write(TempList)
    b.close()
    os.system('start C:\\updata\\upgrade.bat')  #显示cmd窗口
    sys.exit() #退出主程序

version = "2025052201"  
#Form 'Form_1's Load Event :
def Form_1_onLoad(uiName,threadings=0):
    path = os.getcwd()
    if str(path).find("192.168.6.218") != -1:
        Fun.MessageBox("不支持在192.168.6.218共享目录内直接打开","运行错误","error",None)
        sys.exit() #退出主程序
    username = '技术部'  # 用户名
    password = 'Aa123654'  # 密码
    smbclient.reset_connection_cache()
    smbclient.ClientConfig(username=username, password=password)
    try:
        with smbclient.open_file(r"\\192.168.6.218\\技术部\\工具验证设置(非专业勿动勿删)\\IGG账户获取\\version.txt") as f:
            new_version = f.read().split("----")
    except Exception as e:
        Fun.MessageBox("验证异常！联系技术处理","运行错误","error",None)
        print(e)
        sys.exit() #退出主程序
        
    if(int(new_version[0]) > int(version)):
        if int(new_version[1]) == 1:
            Fun.MessageBox("有新版本，需要更新","更新提醒","info",None)
            writeUpgrade("IGG账户获取.exe") 
    run_thread = threading.Thread(target=set_num, args=[uiName])
    run_thread.setDaemon(True)
    run_thread.start()
    
#Button 'Button_1' 's Command Event :
def Button_1_onCommand(uiName,widgetName,threadings=0):
    global flag
    text = Fun.GetText(uiName,'SpinBox_1')
    if int(text) > 15:
        if Fun.AskBox('提示','当前一次输出账户大于15个，是否确定',None) == False:
            return
    for i in range(0,int(text)):
        flag = False
        try:
            data = ["123----123"]
            data = find_zhanghu2()
            
            Fun.AddItemText(uiName,'ListBox_2',data[0],"end") 
            global zhanghu
            zhanghu += data[0]+"\n"
            data = data[0].split("----")    
            value = Fun.DelAllLines(uiName,'ListBox_1')
            Fun.AddItemText(uiName,'ListBox_1',data[0],"end")
            Fun.AddItemText(uiName,'ListBox_1',data[1],"end")
            global zhanghu_index
            zhanghu_index += 1
        except Exception as Ex:
            Fun.MessageBox("账号库可能无数据，请联系管理员","info","info",None)
    flag = True
#ListBox 'ListBox_1's Double-Button-1 Event :
def ListBox_1_onDoubleButton1(event,uiName,widgetName,threadings=0):
    value = Fun.GetCurrentValue(uiName,'ListBox_1')
    if value != -1:
       pyperclip.copy(value)
    pass
#ListBox 'ListBox_2's Double-Button-1 Event :
def ListBox_2_onDoubleButton1(event,uiName,widgetName,threadings=0):
    value = Fun.GetCurrentValue(uiName,'ListBox_2')
    if value != -1:
        pyperclip.copy(value)
        data = value.split("----")    
        value = Fun.DelAllLines(uiName,'ListBox_1')
        Fun.AddItemText(uiName,'ListBox_1',data[0],"end")
        Fun.AddItemText(uiName,'ListBox_1',data[1],"end")
    pass
#Button 'Button_2' 's Command Event :
def Button_2_onCommand(uiName,widgetName,threadings=0):
    global zhanghu
    global zhanghu_index
    try:
        savePath = Fun.SaveFile("保存为文件",[('TXT File','*.txt')], os.path.abspath('.'),'','txt')
        Fun.WriteToFile(savePath,zhanghu,'utf-8',False)
        Fun.MessageBox("保存成功","文件保存","info",None)
        value = Fun.DelAllLines(uiName,'ListBox_2')
        value = Fun.DelAllLines(uiName,'ListBox_1')
        zhanghu =""
        zhanghu_index = 0
        pass
    except:
        Fun.MessageBox("保存失败","文件保存","info",None)
        pass
#ListBox 'ListBox_2's Button-1 Event :
def ListBox_2_onButton1_bak(event,uiName,widgetName,threadings=0):
    value = Fun.GetCurrentValue(uiName,'ListBox_2')
    if value != -1:
        data = value.split("----")    
        value = Fun.DelAllLines(uiName,'ListBox_1')
        Fun.AddItemText(uiName,'ListBox_1',data[0],"end")
        Fun.AddItemText(uiName,'ListBox_1',data[1],"end")
    pass
    
#ListBox 'ListBox_2's ListboxSelect Event :
def ListBox_2_onSelect(event,uiName,widgetName,threadings=0):
    value = Fun.GetCurrentValue(uiName,'ListBox_2')
    if value != -1:
        data = value.split("----")    
        value = Fun.DelAllLines(uiName,'ListBox_1')
        Fun.AddItemText(uiName,'ListBox_1',data[0],"end")
        Fun.AddItemText(uiName,'ListBox_1',data[1],"end")
    pass
#Button 'Button_3' 's Command Event :
def Button_3_onCommand(uiName,widgetName,threadings=0):
    global zhanghu
    global zhanghu_index
    value = Fun.DelAllLines(uiName,'ListBox_2')
    value = Fun.DelAllLines(uiName,'ListBox_1')
    zhanghu =""
    zhanghu_index = 0
    pass
