import tkinter as tk 
from tkinter import messagebox

def crear_interfaz(logica_cola):
    ventana = tk.Tk()
    ventana.title("Ejemplo de una cola sencilla")
    ventana.geometry("400x400")

    #defino la cola
    cola = logica_cola["crear_cola"]()


    def manejar_encolar():
        elemento = entrada_elemento.get()
        if elemento:
            logica_cola["encolar"](cola, elemento)
            actualizar_cola()
            entrada_elemento.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacia", "Porfavor ingresa un elemento")

    def manejar_desencolar():
        try:
            elemento = logica_cola["desencolar"](cola)
            messagebox.showinfo("Desencolar", f"{elemento} elemento desencolado")
            actualizar_cola()
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    
    def manejar_frente():
        try:
            elemento = logica_cola["frente"](cola)
            messagebox.showinfo("Frente", f"Elemento en el frente es: {elemento}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    
    def manejar_tamano():
        tam = logica_cola["tamano"](cola)
        messagebox.showinfo("Tamaño", f"El tmaño de la cola es: {tam}")
    
    def manejar_mostrar(): 
        cola_actual = logica_cola["mostrar_cola"](cola)
        messagebox.showinfo("cola actual", cola_actual)

    def actualizar_cola():
        cola_actual = logica_cola["mostrar_cola"](cola)
        etiqueta_cola.config(text= cola_actual)

    #componentes de la interfaz
    tk.Label(ventana, text= "Manejo de una cola", font=("Arial", 16)).pack(pady=10)

    entrada_elemento = tk.Entry(ventana, width=30)
    entrada_elemento.pack(pady=5)
    tk.Button(ventana, text="Encolar", command=manejar_encolar).pack(pady=5)
    tk.Button(ventana, text="Desencolar", command=manejar_desencolar).pack(pady=5)
    tk.Button(ventana, text="Ver frente", command=manejar_frente).pack(pady=5)
    tk.Button(ventana, text="Ver tamaño", command=manejar_tamano).pack(pady=5)
    tk.Button(ventana, text="Mostrar cola", command=manejar_mostrar).pack(pady=5)

    etiqueta_cola = tk.Label(ventana, text="pila actual:[]", font=("Arial",12))
    etiqueta_cola.pack(pady=20)
    ventana.mainloop()