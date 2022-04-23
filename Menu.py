import Multicolor
import numpy as np
import threading
import PySimpleGUI as sg

def call_blue():
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    Multicolor.main(red_lower,red_upper)
    
sg.theme('Default')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Seleccione el color a detectar')],
            [sg.Button("Azul",key="azul"),sg.Button("Verde",key="verde"),sg.Button("Rojo",key="rojo")] ]

# Create the Window
window = sg.Window('Prueba - Proyecto Final', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "rojo":
        call_blue()

window.close()