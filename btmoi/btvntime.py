import pyglet
import datetime as dt
tday = dt.datetime.today().hour
n= dt.datetime.today().minute
x=int(input("gio can bao thuc la"))
y=int(input("phut can bao thuc la"))
while True:
    while tday!=x or n!=y:        
        tday = dt.datetime.today().hour
        n= dt.datetime.today().minute
        if tday==x and n>y:
            break
    while tday==x and n==y:
        music = pyglet.resource.media('sample.wav')
        music.play()
        pyglet.app.run()
        tday = dt.datetime.today().hour
        n= dt.datetime.today().minute
        if tday==x and n>y:
            break
    if n>y:
        break
