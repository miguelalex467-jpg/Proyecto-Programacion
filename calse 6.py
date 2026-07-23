import tkinter as tk
from tkinter import ttk, messagebox

class AppGestionLibros(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Libros")
        self.geometry("800x500")
        self.minsize(600, 400)

        # Configuración de peso para diseño responsivo
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self._crear_menu()
        self._crear_interfaz_principal()

    # 1. Ventana principal y Menús
    def _crear_menu(self):
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Nuevo Libro", command=self.abrir_modal_agregar)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.destroy)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Gestor de Libros v1.0"))
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    def _crear_interfaz_principal(self):
        # Contenedor principal responsivo
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Barra de herramientas superior
        toolbar = ttk.Frame(main_frame)
        toolbar.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        btn_agregar = ttk.Button(toolbar, text="➕ Agregar Libro", command=self.abrir_modal_agregar)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        btn_eliminar = ttk.Button(toolbar, text="🗑️ Eliminar Seleccionado", command=self.eliminar_libro)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # 3. Treeview y Componentes (Tabla de libros)
        columnas = ("id", "titulo", "autor", "precio")
        self.tree = ttk.Treeview(main_frame, columns=columnas, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("precio", text="Precio ($)")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("titulo", width=250)
        self.tree.column("autor", width=200)
        self.tree.column("precio", width=80, anchor="e")

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

    # 2. Ventanas modales (Formularios flotantes)
    def abrir_modal_agregar(self):
        ModalLibro(self)

    # 4. Mensajes de confirmación y Validaciones
    def eliminar_libro(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, selecciona un libro de la lista.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este libro?")
        if confirmar:
            for item in seleccion:
                self.tree.delete(item)
            messagebox.showinfo("Éxito", "Libro eliminado correctamente.")


class ModalLibro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Agregar Nuevo Libro")
        self.geometry("350x250")
        self.resizable(False, False)
        self.transient(parent)  # Mantener sobre la ventana principal
        self.grab_set()         # Modal (bloquea la ventana principal hasta cerrar)

        self.parent = parent
        self._crear_formulario()

    def _crear_formulario(self):
        frame = ttk.Frame(self, padding="15")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Título:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_titulo = ttk.Entry(frame, width=30)
        self.entry_titulo.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Autor:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_autor = ttk.Entry(frame, width=30)
        self.entry_autor.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Precio:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_precio = ttk.Entry(frame, width=30)
        self.entry_precio.grid(row=2, column=1, pady=5)

        btn_guardar = ttk.Button(frame, text="Guardar", command=self.guardar)
        btn_guardar.grid(row=3, column=0, columnspan=2, pady=20)

    # Validaciones visuales y de datos
    def guardar(self):
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        precio_str = self.entry_precio.get().strip()

        if not titulo or not autor or not precio_str:
            messagebox.showerror("Error de validación", "Todos los campos son obligatorios.", parent=self)
            return

        try:
            precio = float(precio_str)
        except ValueError:
            messagebox.showerror("Error de validación", "El precio debe ser un número válido.", parent=self)
            return

        # Insertar en el Treeview principal (simulación de guardado)
        nuevo_id = len(self.parent.tree.get_children()) + 1
        self.parent.tree.insert("", tk.END, values=(nuevo_id, titulo, autor, f"{precio:.2f}"))
        
        messagebox.showinfo("Éxito", "Libro registrado exitosamente.", parent=self)
        self.destroy()

if __name__ == "__main__":
    app = AppGestionLibros()
    app.mainloop()