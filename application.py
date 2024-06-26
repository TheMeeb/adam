import threading
import subprocess
import webbrowser

#Websites---------------------------------------------
x=lambda:webbrowser.open_new_tab('http://google.com')
t=threading.Thread(target=x)
t.start()
x=lambda:webbrowser.open_new_tab('https://www.instagram.com/')
t=threading.Thread(target=x)
t.start()
x=lambda:webbrowser.open_new_tab('https://www.facebook.com/')
t=threading.Thread(target=x)
t.start()
#Applications------------------------------------------
x=lambda:subprocess.Popen('C:\\Windows\\System32\\calc.exe')
t=threading.Thread(target=x)
t.start()
x=lambda:subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
t=threading.Thread(target=x)
t.start()