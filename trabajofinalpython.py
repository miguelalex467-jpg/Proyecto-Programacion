# este codigo se hizo de manera educativa entre tres amigos, miguel, esau y alex

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

class Libro:
    def __init__(self, isbn, titulo, autor, anio, editorial, categoria, estado):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.editorial = editorial
        self.categoria = categoria
        self.estado = estado

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_anio(self):
        return self.anio

    def set_anio(self, anio):
        self.anio = anio

    def get_editorial(self):
        return self.editorial

    def set_editorial(self, editorial):
        self.editorial = editorial

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def a_diccionario(self):
        dic = {}
        dic["isbn"] = self.isbn
        dic["titulo"] = self.titulo
        dic["autor"] = self.autor
        dic["anio"] = self.anio
        dic["editorial"] = self.editorial
        dic["categoria"] = self.categoria
        dic["estado"] = self.estado
        return dic

    def desde_diccionario(self, dic):
        self.isbn = dic["isbn"]
        self.titulo = dic["titulo"]
        self.autor = dic["autor"]
        self.anio = dic["anio"]
        self.editorial = dic["editorial"]
        self.categoria = dic["categoria"]
        self.estado = dic["estado"]


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.archivo = "biblioteca.json"
        self.cargar()

    def agregar(self, libro):
        self.libros.append(libro)
        self.guardar()

    def buscar(self, isbn):
        for libro in self.libros:
            if libro.get_isbn() == isbn:
                return libro
        return None

    def modificar(self, isbn, nuevo_libro):
        for i in range(len(self.libros)):
            if self.libros[i].get_isbn() == isbn:
                self.libros[i] = nuevo_libro
                self.guardar()
                return True
        return False

    def eliminar(self, isbn):
        for i in range(len(self.libros)):
            if self.libros[i].get_isbn() == isbn:
                del self.libros[i]
                self.guardar()
                return True
        return False

    def listar(self):
        return self.libros

    def guardar(self):
        try:
            lista = []
            for libro in self.libros:
                lista.append(libro.a_diccionario())
            with open(self.archivo, "w") as f:
                json.dump(lista, f, indent=4)
        except Exception as e:
            print("Error al guardar:", e)
        else:
            print("Guardado ok")
        finally:
            print("Fin de guardar")

    def cargar(self):
        try:
            if not os.path.exists(self.archivo):
                with open(self.archivo, "w") as f:
                    json.dump([], f)
            with open(self.archivo, "r") as f:
                datos = json.load(f)
            self.libros = []
            for d in datos:
                libro = Libro(d["isbn"], d["titulo"], d["autor"], d["anio"], d["editorial"], d["categoria"], d["estado"])
                self.libros.append(libro)
        except Exception as e:
            print("Error al cargar:", e)
            self.libros = []
        else:
            print("Cargado ok")
        finally:
            print("Fin de cargar")


class VentanaAgregar:
    def __init__(self, parent, biblioteca):
        self.biblioteca = biblioteca
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Agregar Libro")
        self.ventana.geometry("300x350")
        self.ventana.grab_set()

        tk.Label(self.ventana, text="ISBN").pack()
        self.entry_isbn = tk.Entry(self.ventana)
        self.entry_isbn.pack()

        tk.Label(self.ventana, text="Titulo").pack()
        self.entry_titulo = tk.Entry(self.ventana)
        self.entry_titulo.pack()

        tk.Label(self.ventana, text="Autor").pack()
        self.entry_autor = tk.Entry(self.ventana)
        self.entry_autor.pack()

        tk.Label(self.ventana, text="Anio").pack()
        self.entry_anio = tk.Entry(self.ventana)
        self.entry_anio.pack()

        tk.Label(self.ventana, text="Editorial").pack()
        self.entry_editorial = tk.Entry(self.ventana)
        self.entry_editorial.pack()

        tk.Label(self.ventana, text="Categoria").pack()
        self.entry_categoria = tk.Entry(self.ventana)
        self.entry_categoria.pack()

        tk.Label(self.ventana, text="Estado").pack()
        self.entry_estado = tk.Entry(self.ventana)
        self.entry_estado.pack()
        self.entry_estado.insert(0, "Disponible")

        tk.Button(self.ventana, text="Guardar", command=self.guardar).pack(pady=5)
        tk.Button(self.ventana, text="Cancelar", command=self.ventana.destroy).pack()

    def guardar(self):
        try:
            isbn = self.entry_isbn.get()
            titulo = self.entry_titulo.get()
            autor = self.entry_autor.get()
            anio = int(self.entry_anio.get())
            editorial = self.entry_editorial.get()
            categoria = self.entry_categoria.get()
            estado = self.entry_estado.get()
            if isbn == "" or titulo == "":
                messagebox.showerror("Error", "ISBN y Titulo son obligatorios")
                return
            libro = Libro(isbn, titulo, autor, anio, editorial, categoria, estado)
            self.biblioteca.agregar(libro)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Ok", "Libro agregado")
            self.ventana.destroy()
        finally:
            print("Fin agregar")


class VentanaConsultar:
    def __init__(self, parent, biblioteca):
        self.biblioteca = biblioteca
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Consultar Libros")
        self.ventana.geometry("700x400")
        self.ventana.grab_set()

        frame_buscar = tk.Frame(self.ventana)
        frame_buscar.pack(pady=5)
        tk.Label(frame_buscar, text="Buscar ISBN:").pack(side=tk.LEFT)
        self.entry_buscar = tk.Entry(frame_buscar)
        self.entry_buscar.pack(side=tk.LEFT)
        tk.Button(frame_buscar, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buscar, text="Actualizar listado", command=self.actualizar).pack(side=tk.LEFT)

        columnas = ("isbn", "titulo", "autor", "anio", "editorial", "categoria", "estado")
        self.tree = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        tk.Button(self.ventana, text="Cerrar", command=self.ventana.destroy).pack(pady=5)

        self.actualizar()

    def actualizar(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for libro in self.biblioteca.listar():
            self.tree.insert("", tk.END, values=(libro.get_isbn(), libro.get_titulo(), libro.get_autor(), libro.get_anio(), libro.get_editorial(), libro.get_categoria(), libro.get_estado()))

    def buscar(self):
        isbn = self.entry_buscar.get()
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)
            libro = self.biblioteca.buscar(isbn)
            if libro:
                self.tree.insert("", tk.END, values=(libro.get_isbn(), libro.get_titulo(), libro.get_autor(), libro.get_anio(), libro.get_editorial(), libro.get_categoria(), libro.get_estado()))
            else:
                messagebox.showinfo("Info", "No encontrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            print("Busqueda ok")
        finally:
            print("Fin buscar")


class VentanaModificar:
    def __init__(self, parent, biblioteca):
        self.biblioteca = biblioteca
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Modificar Libro")
        self.ventana.geometry("300x400")
        self.ventana.grab_set()

        tk.Label(self.ventana, text="ISBN a buscar").pack()
        self.entry_isbn_buscar = tk.Entry(self.ventana)
        self.entry_isbn_buscar.pack()
        tk.Button(self.ventana, text="Buscar", command=self.buscar).pack(pady=5)

        tk.Label(self.ventana, text="ISBN").pack()
        self.entry_isbn = tk.Entry(self.ventana)
        self.entry_isbn.pack()

        tk.Label(self.ventana, text="Titulo").pack()
        self.entry_titulo = tk.Entry(self.ventana)
        self.entry_titulo.pack()

        tk.Label(self.ventana, text="Autor").pack()
        self.entry_autor = tk.Entry(self.ventana)
        self.entry_autor.pack()

        tk.Label(self.ventana, text="Año").pack()
        self.entry_anio = tk.Entry(self.ventana)
        self.entry_anio.pack()

        tk.Label(self.ventana, text="Editorial").pack()
        self.entry_editorial = tk.Entry(self.ventana)
        self.entry_editorial.pack()

        tk.Label(self.ventana, text="Categoria").pack()
        self.entry_categoria = tk.Entry(self.ventana)
        self.entry_categoria.pack()

        tk.Label(self.ventana, text="Estado").pack()
        self.entry_estado = tk.Entry(self.ventana)
        self.entry_estado.pack()

        tk.Button(self.ventana, text="Guardar cambios", command=self.guardar).pack(pady=5)
        tk.Button(self.ventana, text="Cancelar", command=self.ventana.destroy).pack()

    def buscar(self):
        try:
            isbn = self.entry_isbn_buscar.get()
            libro = self.biblioteca.buscar(isbn)
            if libro:
                self.entry_isbn.delete(0, tk.END)
                self.entry_isbn.insert(0, libro.get_isbn())
                self.entry_titulo.delete(0, tk.END)
                self.entry_titulo.insert(0, libro.get_titulo())
                self.entry_autor.delete(0, tk.END)
                self.entry_autor.insert(0, libro.get_autor())
                self.entry_anio.delete(0, tk.END)
                self.entry_anio.insert(0, str(libro.get_año()))
                self.entry_editorial.delete(0, tk.END)
                self.entry_editorial.insert(0, libro.get_editorial())
                self.entry_categoria.delete(0, tk.END)
                self.entry_categoria.insert(0, libro.get_categoria())
                self.entry_estado.delete(0, tk.END)
                self.entry_estado.insert(0, libro.get_estado())
            else:
                messagebox.showinfo("Info", "No encontrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            print("Busqueda ok")
        finally:
            print("Fin buscar modificar")

    def guardar(self):
        try:
            isbn_viejo = self.entry_isbn_buscar.get()
            isbn = self.entry_isbn.get()
            titulo = self.entry_titulo.get()
            autor = self.entry_autor.get()
            año = int(self.entry_año.get())
            editorial = self.entry_editorial.get()
            categoria = self.entry_categoria.get()
            estado = self.entry_estado.get()
            nuevo = Libro(isbn, titulo, autor, año, editorial, categoria, estado)
            ok = self.biblioteca.modificar(isbn_viejo, nuevo)
            if ok:
                messagebox.showinfo("Ok", "Modificado")
                self.ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo modificar")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            print("Guardar ok")
        finally:
            print("Fin guardar modificar")


class VentanaEliminar:
    def __init__(self, parent, biblioteca):
        self.biblioteca = biblioteca
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Eliminar Libro")
        self.ventana.geometry("250x150")
        self.ventana.grab_set()

        tk.Label(self.ventana, text="ISBN a eliminar").pack(pady=10)
        self.entry_isbn = tk.Entry(self.ventana)
        self.entry_isbn.pack()

        tk.Button(self.ventana, text="Eliminar", command=self.eliminar).pack(pady=10)
        tk.Button(self.ventana, text="Cancelar", command=self.ventana.destroy).pack()

    def eliminar(self):
        try:
            isbn = self.entry_isbn.get()
            if isbn == "":
                messagebox.showerror("Error", "Pon un ISBN")
                return
            respuesta = messagebox.askyesno("Confirmar", "Seguro que quieres eliminar?")
            if respuesta:
                ok = self.biblioteca.eliminar(isbn)
                if ok:
                    messagebox.showinfo("Ok", "Eliminado")
                    self.ventana.destroy()
                else:
                    messagebox.showinfo("Info", "No encontrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            print("Eliminar ok")
        finally:
            print("Fin eliminar")


class VentanaAcerca:
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Acerca de")
        self.ventana.geometry("300x250")
        self.ventana.grab_set()

        tk.Label(self.ventana, text="Sistema de Gestion de Biblioteca ").pack(pady=5)
        tk.Label(self.ventana, text="Integrantes: Miguel, Esau, Alex").pack(pady=5)
        tk.Label(self.ventana, text="Grupo: 1").pack(pady=5)
        tk.Label(self.ventana, text="Materia:Lenguaje de Programacion 3").pack(pady=5)
        tk.Label(self.ventana, text="Fecha: 2026").pack(pady=5)
  
        tk.Button(self.ventana, text="Cerrar", command=self.ventana.destroy).pack(pady=10)


class PrincipalApp:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.ventana = tk.Tk()
        self.ventana.title("Sistema Biblioteca")
        self.ventana.geometry("400x300")
        self.crear_menu()
        self.ventana.mainloop()

    def crear_menu(self):
        menu_bar = tk.Menu(self.ventana)
        self.ventana.config(menu=menu_bar)

        menu_archivo = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo)
        menu_archivo.add_command(label="Guardar", command=self.guardar)
        menu_archivo.add_command(label="Salir", command=self.ventana.quit)

        menu_libros = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Libros", menu=menu_libros)
        menu_libros.add_command(label="Agregar libro", command=self.abrir_agregar)
        menu_libros.add_command(label="Consultar libros", command=self.abrir_consultar)
        menu_libros.add_command(label="Buscar libro", command=self.abrir_buscar)
        menu_libros.add_command(label="Modificar libro", command=self.abrir_modificar)
        menu_libros.add_command(label="Eliminar libro", command=self.abrir_eliminar)

        menu_ayuda = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.abrir_acerca)
        menu_ayuda.add_command(label="Creador del codigo base:", command=self.abrir_creador)

    def nuevo(self):
        self.biblioteca.libros = []
        self.biblioteca.guardar()
        messagebox.showinfo("Nuevo", "Biblioteca limpia")

    def guardar(self):
        self.biblioteca.guardar()
        messagebox.showinfo("Guardar", "Guardado")

    def abrir_agregar(self):
        VentanaAgregar(self.ventana, self.biblioteca)

    def abrir_consultar(self):
        VentanaConsultar(self.ventana, self.biblioteca)

    def abrir_buscar(self):
        VentanaConsultar(self.ventana, self.biblioteca)

    def abrir_modificar(self):
        VentanaModificar(self.ventana, self.biblioteca)

    def abrir_eliminar(self):
        VentanaEliminar(self.ventana, self.biblioteca)

    def abrir_acerca(self):
        VentanaAcerca(self.ventana)

    def abrir_creador(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Creador")
        ventana.geometry("200x100")
        tk.Label(ventana, text="Programador:N054").pack(pady=20)
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack()


if __name__ == "__main__":
    app = PrincipalApp()
