import threading
import subprocess
import webbrowser

x=lambda:webbrowser.open_new_tab('http://google.com')
t=threading.Thread(target=x)
t.start()
x=lambda:webbrowser.open_new_tab('https://www.instagram.com/')
t=threading.Thread(target=x)
t.start()
x=lambda:webbrowser.open_new_tab('https://www.facebook.com/')
t=threading.Thread(target=x)
t.start()