import PySimpleGUI as sg


sg.popup_no_buttons('Hello World')         # the single line

# single line using a real window
sg.Window('Hello world', [[sg.Text('Hello World')]]).read()

# This is a "Traditional" PySimpleGUI window code. First make a layout, then a window, the read it
layout = [[sg.Text('Hello World')]]
window = sg.Window('Hello world', layout)
event, values = window.read()

window.close()
