import tkinter as tk
from tkinter import messagebox
import json
import os


class AplicacionPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto General - Menú y Ventanas Modales")
        self.root.geometry("500x400")

        # Listas para almacenar datos
        self.datos_usuario = []
        self.datos_calculadora = []
        if os.path.exists("datos.json"):
            with open("datos.json","r",encoding="utf-8") as archivo:
                datos=json.load(archivo)
                self.datos_usuario=datos.get("datos_usuario",[])
                self.datos_calculadora=datos.get("datos_calculadora",[])

        # Barra de menú
        self.menu_barra = tk.Menu(self.root)
        self.root.config(menu=self.menu_barra)

        # Menú Operaciones
        self.menu_operaciones = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Operaciones", menu=self.menu_operaciones)
        self.menu_operaciones.add_command(label="Ingresar Dato", command=self.abrir_ventana_modal)
        self.menu_operaciones.add_command(label="Ver Datos", command=self.abrir_ventana_datos)
        self.menu_operaciones.add_command(label="Guardar JSON", command=self.guardar_json)

        # Menú Ayuda
        self.menu_ayuda = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_ayuda.add_command(label="Acerca de", command=self.mostrar_ayuda)

        # Menú Ventanas
        self.menu_ventanas = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label="Ventanas", menu=self.menu_ventanas)
        self.menu_ventanas.add_command(label="Calculadora", command=self.abrir_ventana_modal2)

    def abrir_ventana_modal(self):
        modal = tk.Toplevel(self.root)
        modal.title("Ingresar Información")
        modal.geometry("300x150")

        modal.transient(self.root)
        modal.grab_set()

        tk.Label(modal, text="Escribe un nuevo dato:").pack(pady=15)

        entrada = tk.Entry(modal)
        entrada.pack(pady=5)

        def guardar():
            valor = entrada.get()

            if valor:
                self.datos_usuario.append(valor)
                messagebox.showinfo(
                    "Éxito",
                    f"'{valor}' guardado correctamente.",
                    parent=modal
                )
                modal.destroy()
            else:
                messagebox.showwarning(
                    "Advertencia",
                    "El campo está vacío.",
                    parent=modal
                )

        tk.Button(modal, text="Guardar", command=guardar).pack(pady=15)

    # -----------------------------------------------------
    def abrir_ventana_datos(self):

        modal = tk.Toplevel(self.root)
        modal.title("Datos almacenados")
        modal.geometry("350x250")

        modal.transient(self.root)
        modal.grab_set()

        listbox = tk.Listbox(modal, width=40)
        listbox.pack(fill="both", expand=True, padx=10, pady=10)

        listbox.insert(tk.END, "DATOS INGRESADOS")
        listbox.insert(tk.END, "------------------------")

        if self.datos_usuario:
            for dato in self.datos_usuario:
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "Sin datos.")

        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "OPERACIONES")
        listbox.insert(tk.END, "------------------------")

        if self.datos_calculadora:
            for dato in self.datos_calculadora:
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "Sin operaciones.")

        tk.Button(modal, text="Cerrar", command=modal.destroy).pack(pady=10)


    def guardar_json(self):
        with open("datos.json","w",encoding="utf-8") as archivo:
            json.dump({"datos_usuario":self.datos_usuario,"datos_calculadora":self.datos_calculadora},archivo,indent=4,ensure_ascii=False)
        messagebox.showinfo("Guardar","Datos guardados correctamente.")

    def mostrar_ayuda(self):
        messagebox.showinfo(
            "Acerca de",
            "Proyecto realizado con Python y Tkinter."
        )


    def abrir_ventana_modal2(self):

        modal = tk.Toplevel(self.root)
        modal.title("Sumar números reales")
        modal.geometry("300x250")

        modal.transient(self.root)
        modal.grab_set()

        tk.Label(modal, text="Número 1").pack(pady=5)

        caja1 = tk.Entry(modal)
        caja1.pack()

        tk.Label(modal, text="Número 2").pack(pady=5)

        caja2 = tk.Entry(modal)
        caja2.pack()

        etiqueta = tk.Label(modal, text="Resultado")
        etiqueta.pack(pady=10)

        def calculos():

            try:
                n1 = float(caja1.get())
                n2 = float(caja2.get())

                suma = n1 + n2

                etiqueta.config(
                    text=f"Resultado: {suma}"
                )

                self.datos_calculadora.append(
                    f"{n1} + {n2} = {suma}"
                )

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Debes escribir solamente números."
                )

        tk.Button(
            modal,
            text="CALCULAR SUMA",
            command=calculos
        ).pack(pady=10)

        tk.Button(
            modal,
            text="Cerrar",
            command=modal.destroy
        ).pack()


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AplicacionPrincipal(ventana_principal)
    ventana_principal.mainloop()