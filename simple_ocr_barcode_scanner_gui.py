#Author: Xose
# -*- coding: utf-8 -*-

#You need this packages:
#Pillow
#zbar, use the steps in main directory zbar_install
#Tkinter
#xlrd
#os
#sys
#csv
#openpyxl
#time

import zbar
from PIL import Image
import wincmd
import Tkinter
import tkFileDialog
from openpyxl import Workbook
import openpyxl
import csv
import os
import time
from datetime import datetime
import sys
from Tkinter import *


#FUNCTIONS

def get_qrcode_data_gui(image_name):
    '''??qrcode,????zbar'''
    #import zbar
    from PIL import Image as Img
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    pil = Img.open(image_name).convert('L')
    new_width = 12000
    new_height = 16000
    pil = pil.resize((new_width, new_height), Img.ANTIALIAS)
    width, height = pil.size
    raw = pil.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)
    data = ''
    for symbol in image:
        data += symbol.data+'\n'
    del(image)
    return data

def get_file_path_window():
     root = Tkinter.Tk()
     root.withdraw()
     root.iconbitmap('simple_ocr_barcode_scanner.ico')
     filepath = tkFileDialog.askopenfilename()
     if filepath == '':
         print ("SELECT FILE!")
         get_file_path_window()
     filepath=str(filepath)
     return filepath

#############################################

def get_folder_path_window():
    root = Tkinter.Tk()
    root.withdraw()
    #filepath = tkFileDialog.askopenfilename()
    filepath = tkFileDialog.askdirectory()
    if filepath == '':
        #print ("SELECT FILE!")
        get_folder_path_window()
    filepath = str(filepath)
    return filepath

def ocr_barcode_scanner_folder_gui(path):
    wusername = os.popen('echo %username%').read()
    wusername = wusername.strip()
    name_file= str(datetime.now().strftime('%Y%m%d%H%M'))
    output_file = 'C:/Users/{}/Desktop/{}.txt'.format(wusername, name_file)
    with open(output_file, 'a') as db_temp:
        #in this part will append photos to convert!
        print ("SELECT FOLDER WITH IMAGES FROM YOUR SYSTEM...")
        folder_path=path
        ############
        tstart = datetime.now()
        def test_load(folder_path):
            #folder_path = get_folder_path_window()
            #db_temp.write(get_qrcode_data_new(image_path))
            print("Folder path:")
            print (folder_path)
            print("Reading files...")
            list_folder=os.listdir(folder_path)
            #print (list_folder)
            for element in list_folder:
                #print element
                file_convert=folder_path+'/'+element
                file_convert=file_convert.strip()
                print (file_convert)
                try:
                    print ("Starting image conversion, please wait! ")
                    db_temp.write(get_qrcode_data_gui(file_convert))
                except:
                    print ("This file is not image, it is ignored!")
        test_load(folder_path)
    print("File created in:\n")
    print (output_file)
    tend = datetime.now()
    dur = (tend - tstart)
    dur = str(dur)
    horas = dur.split(':')[0]
    horas = horas + ' hours'
    minutos = dur.split(':')[1]
    minutos = minutos + ' minutes'
    segundos = dur.split(':')[2]
    segundos = segundos.split('.')[0]
    segundos = segundos + ' seconds'
    exec_time = 'FINISHED IN: ' + horas + ' ' + minutos + ' ' + segundos
    print (exec_time)
    ######
    r2.set(output_file)
    ######
    #return (raw_input("WORK DONE!, PRESS ANY KEY TO EXIT"))

def ocr_barcode_scanner_photo_gui(path):
    wusername = os.popen('echo %username%').read()
    wusername = wusername.strip()
    name_file = str(datetime.now().strftime('%Y%m%d%H%M'))
    output_file = 'C:/Users/{}/Desktop/{}.txt'.format(wusername, name_file)
    with open(output_file, 'a') as db_temp:
        #in this part will append photos to convert!
        print ("SELECT IMAGE FROM YOUR SYSTEM...")
        img_path=path
        ############
        tstart = datetime.now()
        def test_load(img_path):
            print("Reading file...")
            file_convert=img_path
            file_convert=file_convert.strip()
            print (file_convert)
            try:
                print ("Starting image conversion, please wait! ")
                db_temp.write(get_qrcode_data_gui(file_convert))
            except:
                print ("This file is not image, it is ignored!")
        test_load(img_path)
    print("File created in:\n")
    print (output_file)
    tend = datetime.now()
    dur = (tend - tstart)
    dur = str(dur)
    horas = dur.split(':')[0]
    horas = horas + ' hours'
    minutos = dur.split(':')[1]
    minutos = minutos + ' minutes'
    segundos = dur.split(':')[2]
    segundos = segundos.split('.')[0]
    segundos = segundos + ' seconds'
    exec_time = 'FINISHED IN: ' + horas + ' ' + minutos + ' ' + segundos
    print (exec_time)
    ######
    r2.set(output_file)
    ######
    #return (raw_input("WORK DONE!, PRESS ANY KEY TO EXIT"))

##################################################################################################
def take_folder_path():
    r.set("")
    r2.set("")
    folder_path = get_folder_path_window()
    r.set(folder_path)
    type_check.set("FOLDER")

def take_image_path():
    r.set("")
    r2.set("")
    image_path = get_file_path_window()
    #comprobar que es una imagen, si no lo es vuelve a lanzarte!
    image_checker = str(image_path)
    image_checker = image_checker.split('.')[1]
    image_checker=image_checker.upper()
    is_image='NO'
    if image_checker == 'JPG':
        is_image = 'YES'
    elif image_checker == 'PNG':
        is_image = 'YES'
    elif image_checker == 'GIF':
        is_image = 'YES'
    elif image_checker == 'JPEG':
        is_image = 'YES'
    elif image_checker == 'BMP':
        is_image = 'YES'
    elif image_checker == 'ICO':
        is_image = 'YES'
    elif image_checker == 'TIFF':
        is_image = 'YES'
    elif image_checker == 'XBM':
        is_image = 'YES'
    elif image_checker == 'WEBP':
        is_image = 'YES'
    else:
        pass
    if is_image == 'YES':
        r.set(image_path)
        type_check.set("IMAGE")
    else:
        take_image_path()

def about_program():
    import Tkinter as tk
    root = tk.Tk()
    root.title("about")  # Titulo de la ventana
    root.iconbitmap('simple_ocr_barcode_scanner.ico')  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=31, height=3, padx=5, pady=5)
    texto.insert(tk.END,"Simple OCR Barcode Scanner v1.0\nAuthor: Xosé Brais Noya García\nhttps://github.com/xoseng\n")
    texto.config(state="disabled")
    root.mainloop()

def license_agreement():
    import Tkinter as tk
    root = tk.Tk()
    root.title("license agreement")  # Titulo de la ventana
    root.iconbitmap('simple_ocr_barcode_scanner.ico')  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=77, height=8, padx=5, pady=5)
    texto.insert(tk.END,"GNU General Public License v3.0\n\n"
                        "Permissions of this strong copyleft license are conditioned\n"
                        "on making available complete source code of licensed works and modifications,\n"
                        "which include larger works using a licensed work, under the same license.\n"
                        "Copyright and license notices must be preserved.\n"
                        "Contributors provide an express grant of patent rights.\n")
    texto.config(state="disabled")
    root.mainloop()

def start_launcher():
        check_value=type_check.get()
        check_value=str(check_value)
        if check_value == 'FOLDER':
            #ejecutar crear archivo de carpetas
            #coger el path y darselo a la funcion
            path=r.get()
            ocr_barcode_scanner_folder_gui(path)
        elif check_value == 'IMAGE':
            path=r.get()
            ocr_barcode_scanner_photo_gui(path)
        else:
            #si no es una imagen o carpeta no hacer nada
            pass

def open_file_launcher():
    fileexists=r2.get()
    fileexists=str(fileexists)
    if fileexists == '':
        pass
    else:
        wincmd.execcmd(fileexists)
###########################################################
# MAIN #############################################

root = Tk()
root.config(bd=30)
root.title("simple ocr barcode scanner")     # Titulo de la ventana
root.iconbitmap('simple_ocr_barcode_scanner.ico')  # Icono de la ventana, en ico o xbm en Linux
root.resizable(0, 0)         # Desactivar redimension de ventana

menubar = Menu(root)
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Info")
helpmenu.add_separator()
helpmenu.add_command(label="License agreement", command=license_agreement)
helpmenu.add_command(label="About", command=about_program)

menubar.add_cascade(label="Info", menu=helpmenu)

imagen = PhotoImage(file="simple_logo.gif")
Label(root, image=imagen).pack(side="top")

##########################GLOBAL TK VARS DECLARATION
r = StringVar()
r2 = StringVar()
type_check = StringVar()
r3 = StringVar()
####################################################

Label(root, text="SELECTED PATH").pack()
Entry(root, justify="center", textvariable=r, state="disabled", width=44).pack()
Label(root, text="FILE FOUND").pack()
Entry(root, justify="center", textvariable=r2, state="disabled", width=44).pack()

Label(root, text="").pack()  # Separador
Button(root, text="LOAD IMAGE", command=take_image_path).pack(side="left", padx=2, pady=2)
Button(root, text="LOAD FOLDER", command=take_folder_path).pack(side="left", padx=2, pady=2)
Button(root, text="OPEN", command=open_file_launcher).pack(side="left", padx=2, pady=2)
Button(root, text="START", command=start_launcher).pack(side="left", padx=2, pady=2)

# Finalmente bucle de la aplicacion
root.mainloop()

