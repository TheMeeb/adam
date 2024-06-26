import threading
import subprocess
import webbrowser

#Websites---------------------------------------------
def Google():
    x=lambda:webbrowser.open_new_tab('http://google.com')
    t=threading.Thread(target=x)
    t.start()
def Instagram():
    x=lambda:webbrowser.open_new_tab('https://www.instagram.com/')
    t=threading.Thread(target=x)
    t.start()
def Facebook():
    x=lambda:webbrowser.open_new_tab('https://www.facebook.com/')
    t=threading.Thread(target=x)
    t.start()
#Applications------------------------------------------
def Calculator():
    x=lambda:subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    t=threading.Thread(target=x)
    t.start()
def Notepad():
    x=lambda:subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    t=threading.Thread(target=x)
    t.start()