import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

def menu_pantalla(pantalla):
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("icono2.ico")
    image = PhotoImage(file = "seguridad.gif")
    image=image.subsample(2,2)
    label=Label(image = image)
    label.pack()

    Label(text = "Acesso al Sistema", bg = "DODGERBLUE", fg = "white", width = "200", height = "2", font = ("calibri", 15)).pack()
    Label(text = "").pack

    Button(text = "Iniciar Sesión", height = "3", width = "30", command = inicio_sesion).pack()
    Button(text = "Registrar", height = "3", width = "30", command = registrar).pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla_uno
    pantalla_uno = Toplevel(pantalla)
    pantalla_uno.geometry("400x250")
    pantalla_uno.title("Inicio de Sesión")
    pantalla_uno.iconbitmap("icono2.ico")

    Label(pantalla_uno, text = "Porfavor Ingrese su Usuario y Contraseña a continuacion", bg = "DODGERBLUE", fg = "white", width = "200", height = "2", font = ("calibri", 10)).pack()
    Label(pantalla_uno, text = "").pack()

    global nombredeusuario_verify
    global contraseñausuario_verify

    nombredeusuario_verify = StringVar()
    contraseñausuario_verify = StringVar()

    global nombre_usuario_entry
    global contraseña_usuario_entry

    Label(pantalla_uno, text = "Usuario").pack()
    nombre_usuario_entry = Entry(pantalla_uno, textvariable = nombredeusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla_uno).pack()

    Label(pantalla_uno, text = "Contraseña").pack()
    contraseña_usuario_entry = Entry(pantalla_uno, show = "*",textvariable = contraseñausuario_verify)
    contraseña_usuario_entry.pack()
    Label(pantalla_uno).pack()

    Button(pantalla_uno, text = "Iniciar Sesion", command = validacion_datos).pack()

def registrar():
    global pantalla_dos
    pantalla_dos = Toplevel(pantalla)
    pantalla_dos.geometry("400x250")
    pantalla_dos.title("Registro")
    pantalla_dos.iconbitmap("icono2.ico")

    global nombre_de_usuario_entry
    global contraseña_entry

    nombre_usuario_entry = StringVar()
    contraseña_entry = StringVar()

    Label(pantalla_dos, text = "Porfavor ingrese un Usuario y Contraseña, Para el registro del Sistema", bg = "DODGERBLUE", fg = "white", width = "200", height = "2", font = ("calibri", 10)).pack()
    Label(pantalla_dos, text = "").pack()
    Label(pantalla_dos, text = "Registro").pack()

    Label(pantalla_dos, text = "Usuario").pack()
    nombre_de_usuario_entry = Entry(pantalla_dos)
    nombre_de_usuario_entry.pack()
    Label(pantalla_dos).pack()

    Label(pantalla_dos, text="Contraseña").pack()
    contraseña_entry = Entry(pantalla_dos, show="*")
    contraseña_entry.pack()
    Label(pantalla_dos).pack()

    Button(pantalla_dos, text = "Registrar", command = inserta_datos).pack()

def bomba():
    global pantalla_tres
    pantalla_tres = Toplevel(pantalla)
    pantalla_tres.geometry("500x300")
    pantalla_tres.title("Acceso secreto")
    pantalla_tres.iconbitmap("icono2.ico")
    

def inserta_datos():
    bd=pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        db = "bd2",
        )

    fcursor = bd.cursor()

    sql = "INSERT INTO login (user,  password) VALUES('{0}', '{1}')".format(nombre_de_usuario_entry.get(),contraseña_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message = "Registro Exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message = "No Registrado", title = "Aviso")

    bd.close()

def validacion_datos():
    bd = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        db = "bd2",
    )

    fcursor = bd.cursor()

    fcursor.execute("SELECT password FROM login WHERE user ='"+nombredeusuario_verify.get()+"' and password ='"+contraseñausuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo("Inicio de Sesión Correcto!", message = "Usuario y Contraseña Correcta")

    else:
        messagebox.showinfo("Inicio de Sesión incorrecto!", message = "Usuario o Contraseña incorrecta")

    bd.close()

menu_pantalla(pantalla)