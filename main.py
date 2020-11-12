from functools import partial
from tkinter import *
from tkinter import messagebox
import sqlite3

menu = Tk()


def nueva_pantalla_menu():
    menu.geometry("300x380")
    menu.title("Bienvenidos")
    menu.iconbitmap("icono2.ico")

    image = PhotoImage(file="seguridad.gif")
    image = image.subsample(2, 2)
    label = Label(image=image)
    label.pack()

    Label(text="Acesso al Sistema", bg="DODGERBLUE", fg="white", width="200", height="2", font=("calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3", width="30", command=nueva_pantalla_inicio_sesion).pack()
    Button(text="Registrar", height="3", width="30", command=nueva_pantalla_registrar).pack()

    return menu


def nueva_pantalla_inicio_sesion():
    pantalla_login = Toplevel(menu)
    pantalla_login.geometry("400x250")
    pantalla_login.title("Inicio de Sesión")
    pantalla_login.iconbitmap("icono2.ico")

    Label(pantalla_login, text="Porfavor Ingrese su Usuario y Contraseña a continuacion", bg="DODGERBLUE", fg="white",
          width="200", height="2", font=("calibri", 10)).pack()
    Label(pantalla_login, text="").pack()

    user_verify = StringVar()
    pass_verify = StringVar()

    Label(pantalla_login, text="Usuario").pack()
    user_entry = Entry(pantalla_login, textvariable=user_verify)
    user_entry.pack()
    Label(pantalla_login).pack()

    Label(pantalla_login, text="Contraseña").pack()
    pass_entry = Entry(pantalla_login, show="*", textvariable=pass_verify)
    pass_entry.pack()
    Label(pantalla_login).pack()

    login_partial = partial(login, user_entry, pass_entry)
    Button(pantalla_login, text="Iniciar Sesion", command=login_partial).pack()


def nueva_pantalla_registrar():
    pantalla_registrar = Toplevel(menu)
    pantalla_registrar.geometry("400x250")
    pantalla_registrar.title("Registro")
    pantalla_registrar.iconbitmap("icono2.ico")

    Label(pantalla_registrar, text="Porfavor ingrese un Usuario y Contraseña, Para el registro del Sistema",
          bg="DODGERBLUE",
          fg="white", width="200", height="2", font=("calibri", 10)).pack()
    Label(pantalla_registrar, text="").pack()
    Label(pantalla_registrar, text="Registro").pack()

    Label(pantalla_registrar, text="Usuario").pack()
    user_entry = Entry(pantalla_registrar)
    user_entry.pack()
    Label(pantalla_registrar).pack()

    Label(pantalla_registrar, text="Contraseña").pack()
    pass_entry = Entry(pantalla_registrar, show="*")
    pass_entry.pack()
    Label(pantalla_registrar).pack()

    register_partial = partial(inserta_datos, user_entry, pass_entry)
    Button(pantalla_registrar, text="Registrar", command=register_partial).pack()


def nueva_pantalla_bomba():
    pantalla_bomba = Toplevel(menu)
    pantalla_bomba.geometry("500x300")
    pantalla_bomba.title("Acceso secreto")
    pantalla_bomba.iconbitmap("icono2.ico")


def inserta_datos(user, password):
    bd = sqlite3.connect("login.db")

    fcursor = bd.cursor()

    sql = "INSERT INTO login (user,  password) VALUES('{0}', '{1}')".format(user.get(), password.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="Error de registro", title="Aviso")

    bd.close()


def login(user, password):
    bd = sqlite3.connect("login.db")

    fcursor = bd.cursor()

    fcursor.execute("""SELECT password FROM login WHERE user = %(user)s and password = %(password)s""",
                    {"user": user.get(), "password": password.get()})

    if fcursor.fetchall():
        messagebox.showinfo("Inicio de Sesión Correcto!", message="Usuario y Contraseña Correcta")

    else:
        messagebox.showinfo("Inicio de Sesión incorrecto!", message="Usuario o Contraseña incorrecta")

    bd.close()


if __name__ == '__main__':
    menu = nueva_pantalla_menu()
    menu.mainloop()
