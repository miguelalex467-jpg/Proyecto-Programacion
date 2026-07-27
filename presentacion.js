const pptxgen = require("pptxgenjs");

let pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Miguel, Esau, Alex - N054";
pres.title = "Sistema de Gestión de Biblioteca Universitaria";
pres.subject = "Presentación del proyecto";

// Colores
const AZUL_OSCURO = "1a365d";
const AZUL = "2b6cb0";
const AZUL_CLARO = "ebf8ff";
const GRIS = "4a5568";
const BLANCO = "FFFFFF";
const VERDE = "276749";

// ========== SLIDE 1: Portada ==========
let s1 = pres.addSlide();
s1.background = { color: AZUL_OSCURO };
s1.addText("Sistema de Gestión de\nBiblioteca Universitaria", {
  x: 0.5, y: 1.5, w: 9, h: 1.8,
  fontSize: 32, fontFace: "Arial", bold: true, color: BLANCO, align: "center"
});
s1.addText("Proyecto colaborativo de Programación Orientada a Objetos\ncon Tkinter y JSON", {
  x: 0.5, y: 3.5, w: 9, h: 0.8,
  fontSize: 16, fontFace: "Arial", color: "A0AEC0", align: "center"
});
s1.addText("Miguel  •  Esau  •  Alex\nGrupo N054  |  2026", {
  x: 0.5, y: 4.6, w: 9, h: 0.6,
  fontSize: 14, fontFace: "Arial", color: BLANCO, align: "center"
});

// ========== SLIDE 2: Objetivo ==========
let s2 = pres.addSlide();
s2.background = { color: BLANCO };
s2.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.15, fill: { color: AZUL_OSCURO } });
s2.addText("Objetivo del proyecto", {
  x: 0.5, y: 0.4, w: 9, h: 0.5,
  fontSize: 26, fontFace: "Arial", bold: true, color: AZUL_OSCURO
});
s2.addText("Desarrollar una aplicación de escritorio en Python que permita administrar una pequeña biblioteca universitaria, aplicando:", {
  x: 0.5, y: 1.1, w: 9, h: 0.7,
  fontSize: 15, fontFace: "Arial", color: GRIS
});
s2.addText([
  { text: "Programación Orientada a Objetos (clases Libro, Biblioteca y PrincipalApp)", options: { bullet: true, breakLine: true } },
  { text: "Interfaz gráfica con Tkinter y ventanas modales (Toplevel)", options: { bullet: true, breakLine: true } },
  { text: "Persistencia de datos en archivo JSON", options: { bullet: true, breakLine: true } },
  { text: "Trabajo colaborativo y código modular", options: { bullet: true } }
], { x: 0.7, y: 2.0, w: 8.5, h: 2.5, fontSize: 16, fontFace: "Arial", color: GRIS });

// ========== SLIDE 3: Funcionalidades ==========
let s3 = pres.addSlide();
s3.background = { color: BLANCO };
s3.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.15, fill: { color: AZUL_OSCURO } });
s3.addText("Funcionalidades del sistema", {
  x: 0.5, y: 0.4, w: 9, h: 0.5,
  fontSize: 26, fontFace: "Arial", bold: true, color: AZUL_OSCURO
});

const funcs = [
  { titulo: "Agregar", desc: "Registrar libros nuevos" },
  { titulo: "Consultar", desc: "Ver listado completo (Treeview)" },
  { titulo: "Buscar", desc: "Localizar por ISBN" },
  { titulo: "Modificar", desc: "Editar datos de un libro" },
  { titulo: "Eliminar", desc: "Borrar con confirmación" },
  { titulo: "JSON", desc: "Guardado y carga automática" }
];

funcs.forEach((f, i) => {
  const col = i % 3;
  const row = Math.floor(i / 3);
  const x = 0.5 + col * 3.1;
  const y = 1.2 + row * 1.8;
  s3.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: x, y: y, w: 2.9, h: 1.5,
    fill: { color: AZUL_CLARO }, rectRadius: 0.1
  });
  s3.addText(f.titulo, {
    x: x, y: y + 0.3, w: 2.9, h: 0.4,
    fontSize: 16, fontFace: "Arial", bold: true, color: AZUL, align: "center"
  });
  s3.addText(f.desc, {
    x: x + 0.1, y: y + 0.8, w: 2.7, h: 0.4,
    fontSize: 13, fontFace: "Arial", color: GRIS, align: "center"
  });
});

// ========== SLIDE 4: Arquitectura ==========
let s4 = pres.addSlide();
s4.background = { color: BLANCO };
s4.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.15, fill: { color: AZUL_OSCURO } });
s4.addText("Arquitectura del código", {
  x: 0.5, y: 0.4, w: 9, h: 0.5,
  fontSize: 26, fontFace: "Arial", bold: true, color: AZUL_OSCURO
});
s4.addText("Todo el sistema está contenido en un solo archivo: codigo final.py", {
  x: 0.5, y: 1.0, w: 9, h: 0.4,
  fontSize: 14, fontFace: "Arial", color: GRIS
});

const clases = [
  { nombre: "Libro", items: "ISBN, Título, Autor,\nAño, Editorial,\nCategoría, Estado\n+ getters/setters\n+ a_diccionario()" },
  { nombre: "Biblioteca", items: "Agregar, Buscar,\nModificar, Eliminar,\nListar, Guardar JSON,\nCargar JSON" },
  { nombre: "PrincipalApp", items: "Ventana principal,\nMenús, Abrir ventanas\nmodales, Coordinar\noperaciones" }
];

clases.forEach((c, i) => {
  const x = 0.5 + i * 3.15;
  s4.addShape(pres.shapes.RECTANGLE, {
    x: x, y: 1.6, w: 3.0, h: 0.5,
    fill: { color: AZUL }
  });
  s4.addText(c.nombre, {
    x: x, y: 1.65, w: 3.0, h: 0.4,
    fontSize: 15, fontFace: "Arial", bold: true, color: BLANCO, align: "center"
  });
  s4.addShape(pres.shapes.RECTANGLE, {
    x: x, y: 2.1, w: 3.0, h: 2.6,
    fill: { color: AZUL_CLARO }
  });
  s4.addText(c.items, {
    x: x + 0.15, y: 2.3, w: 2.7, h: 2.3,
    fontSize: 13, fontFace: "Arial", color: GRIS, align: "center"
  });
});

// ========== SLIDE 5: Interfaz ==========
let s5 = pres.addSlide();
s5.background = { color: BLANCO };
s5.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.15, fill: { color: AZUL_OSCURO } });
s5.addText("Interfaz gráfica (Tkinter)", {
  x: 0.5, y: 0.4, w: 9, h: 0.5,
  fontSize: 26, fontFace: "Arial", bold: true, color: AZUL_OSCURO
});
s5.addText([
  { text: "Ventana principal", options: { bold: true, breakLine: true } },
  { text: "Solo menú superior. No contiene formularios. Controla todo el sistema.", options: { breakLine: true } },
  { text: "", options: { breakLine: true } },
  { text: "Ventanas modales (Toplevel)", options: { bold: true, breakLine: true } },
  { text: "• Agregar libro  →  formulario con todos los campos + Guardar / Cancelar", options: { breakLine: true } },
  { text: "• Consultar / Buscar  →  Treeview + botones Buscar, Actualizar y Cerrar", options: { breakLine: true } },
  { text: "• Modificar  →  buscar por ISBN, mostrar datos, editar y guardar", options: { breakLine: true } },
  { text: "• Eliminar  →  pedir ISBN + confirmación antes de borrar", options: { breakLine: true } },
  { text: "• Acerca de  →  nombre del proyecto, integrantes, grupo, materia, fecha", options: { breakLine: true } },
  { text: "• Creador  →  ventana que muestra \"N054\"", options: { breakLine: true } }
], { x: 0.5, y: 1.1, w: 9, h: 4, fontSize: 14, fontFace: "Arial", color: GRIS });

// ========== SLIDE 6: Persistencia ==========
let s6 = pres.addSlide();
s6.background = { color: BLANCO };
s6.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.15, fill: { color: AZUL_OSCURO } });
s6.addText("Persistencia con JSON", {
  x: 0.5, y: 0.4, w: 9, h: 0.5,
  fontSize: 26, fontFace: "Arial", bold: true, color: AZUL_OSCURO
});
s6.addText("Archivo: biblioteca.json", {
  x: 0.5, y: 1.0, w: 9, h: 0.4,
  fontSize: 16, fontFace: "Arial", bold: true, color: AZUL
});
s6.addText([
  { text: "Al iniciar el programa se carga automáticamente el archivo.", options: { bullet: true, breakLine: true } },
  { text: "Si el archivo no existe, se crea vacío.", options: { bullet: true, breakLine: true } },
  { text: "Cada vez que se agrega, modifica o elimina un libro, se guarda automáticamente.", options: { bullet: true, breakLine: true } },
  { text: "Se usa try / except / else / finally para manejar errores de lectura y escritura.", options: { bullet: true } }
], { x: 0.5, y: 1.6, w: 9, h: 2.2, fontSize: 15, fontFace: "Arial", color: GRIS });

s6.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 0.5, y: 4.0, w: 9, h: 1.2,
  fill: { color: "F7FAFC" }, rectRadius: 0.08
});
s6.addText('Ejemplo:  [{"isbn":"978123456", "titulo":"Python Basico", "autor":"Juan Perez", ...}]', {
  x: 0.7, y: 4.3, w: 8.6, h: 0.6,
  fontSize: 13, fontFace: "Consolas", color: GRIS, align: "center"
});

// ========== SLIDE 7: Trabajo colaborativo ==========
let s7 = pres.addSlide();
s7.background = { color: BLANCO };
s7.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.15, fill: { color: AZUL_OSCURO } });
s7.addText("Trabajo colaborativo", {
  x: 0.5, y: 0.4, w: 9, h: 0.5,
  fontSize: 26, fontFace: "Arial", bold: true, color: AZUL_OSCURO
});

s7.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 0.5, y: 1.2, w: 4.3, h: 3.5,
  fill: { color: AZUL_CLARO }, rectRadius: 0.1
});
s7.addText("Integrante A (Modelo)", {
  x: 0.7, y: 1.4, w: 3.9, h: 0.4,
  fontSize: 16, fontFace: "Arial", bold: true, color: AZUL
});
s7.addText([
  { text: "Clase Libro", options: { bullet: true, breakLine: true } },
  { text: "Clase Biblioteca", options: { bullet: true, breakLine: true } },
  { text: "Lectura y escritura JSON", options: { bullet: true, breakLine: true } },
  { text: "Validaciones de datos", options: { bullet: true } }
], { x: 0.8, y: 2.0, w: 3.7, h: 2.2, fontSize: 14, fontFace: "Arial", color: GRIS });

s7.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 5.2, y: 1.2, w: 4.3, h: 3.5,
  fill: { color: AZUL_CLARO }, rectRadius: 0.1
});
s7.addText("Integrante B (Vista)", {
  x: 5.4, y: 1.4, w: 3.9, h: 0.4,
  fontSize: 16, fontFace: "Arial", bold: true, color: AZUL
});
s7.addText([
  { text: "Ventana principal y menús", options: { bullet: true, breakLine: true } },
  { text: "Ventanas modales", options: { bullet: true, breakLine: true } },
  { text: "Treeview", options: { bullet: true, breakLine: true } },
  { text: "Mensajes y validaciones visuales", options: { bullet: true } }
], { x: 5.5, y: 2.0, w: 3.7, h: 2.2, fontSize: 14, fontFace: "Arial", color: GRIS });

// ========== SLIDE 8: Conclusión ==========
let s8 = pres.addSlide();
s8.background = { color: AZUL_OSCURO };
s8.addText("Conclusión", {
  x: 0.5, y: 1.3, w: 9, h: 0.6,
  fontSize: 28, fontFace: "Arial", bold: true, color: BLANCO, align: "center"
});
s8.addText("Se logró un sistema funcional, simple y educativo que cumple con todos los requisitos:\nPOO, interfaz gráfica con Tkinter, ventanas modales y persistencia en JSON.", {
  x: 1, y: 2.2, w: 8, h: 1.5,
  fontSize: 16, fontFace: "Arial", color: "A0AEC0", align: "center"
});
s8.addText("Miguel  •  Esau  •  Alex\nGrupo N054", {
  x: 0.5, y: 4.2, w: 9, h: 0.7,
  fontSize: 15, fontFace: "Arial", color: BLANCO, align: "center"
});

pres.writeFile({ fileName: "/home/workdir/artifacts/Presentacion_Proyecto.pptx" })
  .then(() => console.log("Presentacion_Proyecto.pptx creada correctamente"))
  .catch(err => console.error(err));
