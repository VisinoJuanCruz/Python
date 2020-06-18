import PySimpleGUI as sg

layout = [sg.B("Win1"), sg.B("Win2")]
window = sg.Window("Menu", layout)
while True:
    event, values = window.read(timeout=200)
    if not event:
        exit(0)
    elif event == "Win1":
        win1()
    elif event == "Win2":
        win2()

def win1():
    layout = [sg.T("Win1")]
    window = sg.Window("Win1", layout)
    while True:
        event, values = window.read(timeout=200)
        if not event:
            break

def win2():
    layout = [sg.T("Win2")]
    window = sg.Window("Win2", layout)
    while True:
        event, values = window.read(timeout=200)
        if not event:
            break