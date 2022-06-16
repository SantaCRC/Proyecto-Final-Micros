import Multicolors as Multicolor
import numpy as np
import PySimpleGUI as sg
import programa
import threading

def call_blue():
    red_lower = np.array([0, 136, 0], np.uint8)
    red_upper = np.array([165, 255, 255], np.uint8)
    Multicolor.main(red_lower,red_upper)
    
    

        
    
def menu_programado():
    centro = [[sg.Text(key='texto',text='Seleccione el archivo'),sg.Text(key='ejecutando',text="Ejecutando",visible=False)],[sg.Input(key='_file_'), sg.FileBrowse(key="find",button_text="Buscar"), sg.Button('Correr', key='correr', button_color=('white', 'green'))]]
    window = sg.Window('Programable', layout=centro, modal=True)
    t=threading.Thread(target=programa.leer_archivo, args=('holamundo.txt',))
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "correr":
            t=threading.Thread(target=programa.leer_archivo, args=(values['_file_'],))
            window["correr"].update(visible=False)
            window["texto"].update(visible=False)
            window["find"].update(visible=False)
            window["ejecutando"].update(visible=True)
            window["_file_"].update(visible=False)
            t.start() #Inicia el hilo de ejecucion del modo programado
            window.refresh() #Refresca la ventana
            t.join() #Espera a que el hilo termine
            window["correr"].update(visible=True)
            window["texto"].update(visible=True)
            window["find"].update(visible=True)
            window["ejecutando"].update(visible=False)
            window["_file_"].update(visible=True)
            
    window.close()
        
    

def menu_watchdog():
    centro = [[sg.Text('Seleccione el color')],[sg.Button('Azul', key='blue', button_color=('white', 'blue')), sg.Button('Rojo', key='red', button_color=('white', 'red')), sg.Button('Verde', key='green', button_color=('white', 'green'))]]
    window = sg.Window('Watchdog', layout=centro, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "red":
            call_blue()

        
    window.close()
    
        
sg.theme('Default')   # Add a touch of color
# All the stuff inside your window.
menu_en_centro = [[sg.Text('Seleccione el modo deseado')],[sg.Button('Manual',key='-MANUAL-'), sg.Button('Programable',key='-PROGRAMABLE-'), sg.Button('Watchdog',key='-WATCHDOG-')], [sg.Button('Cerrar',key='salir',button_color=('white','firebrick4'))]]
layout = [[sg.VPush()],[sg.Push(),sg.Column(menu_en_centro),sg.Push()],[sg.VPush()]]
#layout = [  [sg.Text('Seleccione el color a detectar')],
#            [sg.Button("Azul",key="azul"),sg.Button("Verde",key="verde"),sg.Button("Rojo",key="rojo")] ]

# Create the Window
window = sg.Window('Prueba - Proyecto Final', layout, finalize=True)
#window.maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == "-PROGRAMABLE-":
        menu_programado()
    elif event == "-WATCHDOG-":
        menu_watchdog()
window.close()