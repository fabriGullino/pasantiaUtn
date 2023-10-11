import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import mysql.connector
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gramene"
    )

    cursor = conexion.cursor()

except Exception as e:
    messagebox.showerror("Error", f"Ocurrió un error al conectarse a la base de datos.")

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


def ventanaAcceso():
    def acceso():
        usuario = entry_user.get()
        contraseña = entry_pass.get()
        
        consulta = "SELECT * FROM usuarios WHERE user = %s AND pass = %s"
        valores = (usuario, contraseña)
        cursor.execute(consulta, valores)
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Acceso exitoso", "Inicio de sesión exitoso")
            root.withdraw()
            ventanaInicio()
        elif usuario == "" or contraseña == "":
            messagebox.showerror("Error de acceso", "Uno o mas campos se encuentran vacios.")
        else:
            messagebox.showerror("Error de acceso", "Nombre de usuario o contraseña incorrectos")

    root = tk.Tk()
    root.title("Utn DB Manager")
    root.geometry("300x400")
    root.resizable(False, False)
    root.configure(bg="#12355B")

    centrar_ventana(root)

    icon = os.path.abspath("assets/utnLogotypee.ico")

    root.iconbitmap(icon)

    image = os.path.abspath("assets/utnLogotype.png")

    utnLogo = Image.open(image)

    nuevo_tamano = (100, 100)
    imagen_redimensionada = utnLogo.resize(nuevo_tamano)

    imagen_gif = ImageTk.PhotoImage(imagen_redimensionada)

    fontText = ("Roboto", 12, "bold")

    accessFrame = tk.Frame(root, background="#12355B")
    accessFrame.pack(pady=30)


    userLabel = tk.Label(accessFrame, text="Usuario", font=fontText, background="#12355B", foreground="#fefefe")
    userLabel.pack(pady=10)
    entry_user = tk.Entry(accessFrame, width=28, font=fontText)
    entry_user.pack()


    passLabel = tk.Label(accessFrame, text="Contraseña", font=fontText, background="#12355B", foreground="#fefefe")
    passLabel.pack(pady=10)
    entry_pass = tk.Entry(accessFrame, width=28, font=fontText, show="•")
    entry_pass.pack()


    formSub = tk.Button(accessFrame, text="Ingresar", width=25, height=1, command=acceso, font=fontText, background="#12355B", foreground="#fefefe" )
    formSub.pack(pady=20)

    imageLabel = tk.Label(accessFrame, image=imagen_gif, borderwidth=0)
    imageLabel.pack(pady=15)

    root.mainloop()

def ventanaInicio():

    root = tk.Toplevel()
    root.title("Inicio")
    root.geometry("1024x384")
    root.resizable(False, False)
    root.configure(bg="#12355B")

    centrar_ventana(root)

    icon = os.path.abspath("assets/utnLogotypee.ico")

    root.iconbitmap(icon)

    def abrir_primera_ventana():
        root.withdraw()
        ventanaInicio()
    def abrir_segunda_ventana():
        root.withdraw()
        ventanaAdministracion()
    def abrir_tercera_ventana():
        root.withdraw()
        ventanaUsuarios()

    image = os.path.abspath("assets/utnLogotype.png")

    utnLogo = Image.open(image)

    nuevo_tamano = (200, 200)
    imagen_redimensionada = utnLogo.resize(nuevo_tamano)

    imagen_gif = ImageTk.PhotoImage(imagen_redimensionada)

    nav_frame = tk.Frame(root)
    nav_frame.pack()

    fontText = ("Roboto", 12, "bold")

    button1st = tk.Button(nav_frame, text="Inicio", width=34, height=2, command=abrir_primera_ventana, background="#12355B", foreground="#fefefe", borderwidth=0, font=fontText)
    button2nd = tk.Button(nav_frame, text="Administracion", width=34, height=2, command=abrir_segunda_ventana, background="#12355B", foreground="#fefefe", borderwidth=0, font=fontText)
    button3rd = tk.Button(nav_frame, text="Usuarios", width=34, height=2, command=abrir_tercera_ventana, background="#12355B", foreground="#fefefe", borderwidth=0, font=fontText)

    button1st.pack(side="left", padx=1, pady=1)
    button2nd.pack(side="left", padx=1, pady=1)
    button3rd.pack(side="left", padx=1, pady=1)

    imageFrame = tk.Frame(root, background="#12355B")
    imageFrame.pack(pady=50)

    imageLabel = tk.Label(imageFrame, image=imagen_gif, borderwidth=0)
    imageLabel.pack(pady=15)

    root.mainloop()

def ventanaAdministracion():

    root = tk.Toplevel()
    root.title("Administracion")
    root.geometry("1074x500")
    root.resizable(False, False)
    root.configure(bg="#12355B")

    centrar_ventana(root)

    icon = os.path.abspath("assets/utnLogotypee.ico")

    root.iconbitmap(icon)

    def abrir_primera_ventana():
        root.withdraw()
        ventanaInicio()
    def abrir_segunda_ventana():
        root.withdraw()
        ventanaAdministracion()
    def abrir_tercera_ventana():
        root.withdraw()
        ventanaUsuarios()

    nav_frame = tk.Frame(root)
    nav_frame.pack()

    fontText = ("Roboto", 12, "bold")

    button1st = tk.Button(nav_frame, text="Inicio", width=36, height=2, command=abrir_primera_ventana, background="#12355B", foreground="#fefefe", font=fontText, borderwidth=0)
    button2nd = tk.Button(nav_frame, text="Administracion", width=36, height=2, command=abrir_segunda_ventana, background="#12355B", foreground="#fefefe", font=fontText, borderwidth=0)
    button3rd = tk.Button(nav_frame, text="Usuarios", width=36, height=2, command=abrir_tercera_ventana, background="#12355B", foreground="#fefefe", font=fontText, borderwidth=0)

    button1st.pack(side="left", padx=1, pady=1)
    button2nd.pack(side="left", padx=1, pady=1)
    button3rd.pack(side="left", padx=1, pady=1)


    def actualizar_treeview():

        if tree.get_children():
            tree.delete(*tree.get_children())
        cursor = conexion.cursor()
        select_query = "SELECT * FROM tomate" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)


    def modificarRegistro():
        idValue = id_var.get()
        entryValue = entry_var.get()
        reviewedValue = reviewed_var.get()
        entryNameValue = entry_name_var.get()
        proteinNameValue = protein_name_var.get()
        geneNameValue = gene_name_var.get()
        organismValue = organism_var.get()
        lengthValue = length_var.get()
        

        update_query = "UPDATE tomate SET entry = %s, reviewed = %s, entry_name = %s, protein_names = %s, gene_names = %s, organism = %s, Length = %s WHERE Id = %s"
        valores = (entryValue, reviewedValue, entryNameValue, proteinNameValue, geneNameValue, organismValue, lengthValue, idValue)
        
        if idValue == "" or entryValue == "" or reviewedValue == "" or entryNameValue == "" or proteinNameValue == "" or geneNameValue == "" or organismValue == "" or lengthValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
            if confirmacion:
                cursor.execute(update_query, valores)
                conexion.commit()
                messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                actualizar_treeview()

                textCamp = [id_var, entry_var, reviewed_var, entry_name_var, protein_name_var, gene_name_var, organism_var, length_var]

                for i in range(len(textCamp)):
                    nuevo_valor = ""
                    textCamp[i].set(nuevo_valor)

            else:
                messagebox.showinfo("Cancelacion", "El registro no sera modificado.")


    def cargarRegistro():
        entryValue = entry_var.get()
        reviewedValue = reviewed_var.get()
        entryNameValue = entry_name_var.get()
        proteinNameValue = protein_name_var.get()
        geneNameValue = gene_name_var.get()
        organismValue = organism_var.get()
        lengthValue = length_var.get()
        
        valores = (entryValue, reviewedValue, entryNameValue, proteinNameValue, geneNameValue, organismValue, lengthValue)

        insert_query = "INSERT INTO tomate (entry, reviewed, entry_name, protein_names, gene_names, organism, Length) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        if entryValue == "" or reviewedValue == "" or entryNameValue == "" or proteinNameValue == "" or geneNameValue == "" or organismValue == "" or lengthValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor.execute(insert_query, valores)
            messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
            conexion.commit()
            actualizar_treeview()

            textCamp = [id_var, entry_var, reviewed_var, entry_name_var, protein_name_var, gene_name_var, organism_var, length_var]

            for i in range(len(textCamp)):
                nuevo_valor = "" 
                textCamp[i].set(nuevo_valor)




    def eliminarRegistro():
        id_to_delete = id_var.get()
        valores = (id_to_delete,)
        delete_query = "DELETE FROM tomate WHERE Id = %s"
        confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
        if confirmacion:
            cursor.execute(delete_query, valores)
            conexion.commit()
            messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
            actualizar_treeview()

            textCamp = [id_var, entry_var, reviewed_var, entry_name_var, protein_name_var, gene_name_var, organism_var, length_var]

            for i in range(len(textCamp)):
                nuevo_valor = "" 
                textCamp[i].set(nuevo_valor)

        else:
            messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")


    def volcarTodo():
        consulta = "SELECT * FROM tomate"
        cursor.execute(consulta)
            

        registros = cursor.fetchall()
            

        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values") 


        for b, value in enumerate(values):
            textboxes[b].delete(0, tk.END)
            textboxes[b].insert(0, value)


    def columnSearch():
        comboValue = comboSearch.get()
        searchValue = search.get()
        valor = (searchValue,)

        if comboValue == "" or searchValue == "":

            messagebox.showinfo("Campo Vacio", "Uno o varios campos se encuentran vacios.")

        if comboValue == "Entry":
            consulta = "SELECT * FROM tomate WHERE entry = %s"
        elif comboValue == "Entry Name":
            consulta = "SELECT * FROM tomate WHERE entry_name = %s"
        elif comboValue == "Protein Name":
            consulta = "SELECT * FROM tomate WHERE protein_names = %s"
        elif comboValue == "Gene Name":
            consulta = "SELECT * FROM tomate WHERE gene_names = %s"
        elif comboValue == "Length":
            consulta = "SELECT * FROM tomate WHERE Length = %s"
        else:
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")
            return

        cursor.execute(consulta, valor)

        registros = cursor.fetchall()
            

        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)


    searchFrame = tk.Frame(root, background="#12355B")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Entry", "Entry Name", "Protein Name", "Gene Name", "Length"], width=30)
    comboSearch.pack(side="left", padx=30)


    search = tk.Entry(searchFrame, width=30, font=fontText)
    search.pack(side="left", padx=30)


    searchButton = tk.Button(searchFrame, text="Buscar", width=30, command=columnSearch, font=fontText, background="#12355B", foreground="#fefefe")
    searchButton.pack(side="left", padx=30)


    tree_frame = tk.Frame(root, background="#12355B")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("ID", "Entry", "Reviewed", "Entry Name", "Protein Name", "Gene Name", "Organism", "Length"))

    for c in range(1,8):
        tree.column(f"#{c}", width=127, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#8", width=127, anchor="center")

    headings = ["Id", "Entry", "Reviewed", "Entry Name", "Protein Name", "Gene Name", "Organism", "Length"]

    for e in range(8):
        headNum = [1,2,3,4,5,6,7,8]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)


    textbox_frame = tk.Frame(root, background="#12355B")
    textbox_frame.pack(pady=10)

    labels = ["Id", "Entry", "Reviewed", "Entry Name", "Protein Name", "Gene Name", "Organism", "Length"]

    for i in range(8):
        label = tk.Label(textbox_frame, text=f"{labels[i]}", font=fontText, background="#12355B", foreground="#fefefe")
        label.grid(row=1, column=i, padx=5, pady=5)
        labels.append(label)

    textboxes = []
    text_vars = [] 

    for x in range(8):
        text_var = tk.StringVar() 
        text_vars.append(text_var) 

        textbox = tk.Entry(textbox_frame, textvariable=text_var, width=20, borderwidth=0)
        textbox.grid(row=2, column=x, padx=5, pady=5)
        textboxes.append(textbox)  

    id_var, entry_var, reviewed_var, entry_name_var, protein_name_var, gene_name_var, organism_var, length_var = text_vars

    btn_frame = tk.Frame(root, background="#12355B")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, font=fontText, background="#12355B", foreground="#fefefe")
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, font=fontText, background="#12355B", foreground="#fefefe")
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, font=fontText, background="#12355B", foreground="#fefefe")
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, font=fontText, background="#12355B", foreground="#fefefe")

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)

    root.mainloop()

def ventanaUsuarios():
    root = tk.Toplevel()
    root.title("Usuarios")
    root.geometry("820x500")
    root.resizable(False, False)
    root.configure(bg="#12355B")

    centrar_ventana(root)

    icon = os.path.abspath("assets/utnLogotypee.ico")

    root.iconbitmap(icon)

    def abrir_primera_ventana():
        root.withdraw()
        ventanaInicio()
    def abrir_segunda_ventana():
        root.withdraw()
        ventanaAdministracion()
    def abrir_tercera_ventana():
        root.withdraw()
        ventanaUsuarios()

    fontText = ("Roboto", 12, "bold")

    nav_frame = tk.Frame(root)
    nav_frame.pack()

    button1st = tk.Button(nav_frame, text="Inicio", width=27, height=2, command=abrir_primera_ventana, font=fontText, background="#12355B", foreground="#fefefe", borderwidth=0)
    button2nd = tk.Button(nav_frame, text="Administracion", width=27, height=2, command=abrir_segunda_ventana, font=fontText, background="#12355B", foreground="#fefefe", borderwidth=0)
    button3rd = tk.Button(nav_frame, text="Usuarios", width=27, height=2, command=abrir_tercera_ventana, font=fontText, background="#12355B", foreground="#fefefe", borderwidth=0)

    button1st.pack(side="left", padx=1, pady=1)
    button2nd.pack(side="left", padx=1, pady=1)
    button3rd.pack(side="left", padx=1, pady=1)

    def actualizar_treeview():
        # Verificar si hay elementos en el Treeview antes de intentar eliminarlos
        if tree.get_children():
            tree.delete(*tree.get_children())  # Eliminar todas las filas excepto la raíz
        cursor = conexion.cursor()
        select_query = "SELECT * FROM usuarios" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)


    def modificarRegistro():
        codUserValue = cod_user_var.get()
        userValue = user_var.get()
        passValue = pass_var.get()

        
        # Actualizar los registros en la base de datos
        update_query = "UPDATE usuarios SET user = %s, pass = %s WHERE cod_user = %s"
        valores = (userValue, passValue, codUserValue)
        
        if codUserValue == "" or userValue == "" or passValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
            if confirmacion:
                cursor.execute(update_query, valores)
                conexion.commit()
                messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                actualizar_treeview()

                textCamp = [cod_user_var, user_var, pass_var]

                for i in range(len(textCamp)):
                    nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                    textCamp[i].set(nuevo_valor)

            else:
                messagebox.showinfo("Cancelacion", "El registro no sera modificado.")


    def cargarRegistro():
        userValue = user_var.get()
        passValue = pass_var.get()
        
        valores = (userValue, passValue)

        insert_query = "INSERT INTO usuarios (user, pass) VALUES (%s, %s)"
        
        if userValue == "" or passValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor.execute(insert_query, valores)
            messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
            conexion.commit()
            actualizar_treeview()

            textCamp = [cod_user_var, user_var, pass_var]

            for i in range(len(textCamp)):
                nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                textCamp[i].set(nuevo_valor)



    # Función para eliminar un registro de la base de datos
    def eliminarRegistro():
        id_to_delete = cod_user_var.get()
        valores = (id_to_delete,)
        delete_query = "DELETE FROM usuarios WHERE cod_user = %s"
        confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
        if confirmacion:
            cursor.execute(delete_query, valores)
            conexion.commit()
            messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
            actualizar_treeview()

            textCamp = [cod_user_var, user_var, pass_var]

            for i in range(len(textCamp)):
                nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                textCamp[i].set(nuevo_valor)

        else:
            messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")

    # Función para volcar datos desde la base de datos al Treeview
    def volcarTodo():
        consulta = "SELECT * FROM usuarios"
        cursor.execute(consulta)
            
            # Obtener todos los registros
        registros = cursor.fetchall()
            
            # Limpiar el Treeview
        for a in tree.get_children():
            tree.delete(a)
            
            # Llenar el Treeview con los datos
        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]  # Obtiene el primer elemento seleccionado
        values = tree.item(item, "values")  # Obtiene los valores de la fila seleccionada

        # Asigna los valores a los Textboxes
        for b, value in enumerate(values):
            textboxes[b].delete(0, tk.END)
            textboxes[b].insert(0, value)


    def columnSearch():
        comboValue = comboSearch.get()
        searchValue = search.get()
        valor = (searchValue,)

        if comboValue == "" or searchValue == "":

            messagebox.showinfo("Campo Vacio", "Uno o varios campos se encuentran vacios.")

        if comboValue == "Usuario":
            consulta = "SELECT * FROM usuarios WHERE user = %s"
        elif comboValue == "Contraseña":
            consulta = "SELECT * FROM usuarios WHERE pass = %s"
        else:
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")
            return

        cursor.execute(consulta, valor)

        registros = cursor.fetchall()
            
        # Limpiar el Treeview
        for a in tree.get_children():
            tree.delete(a)
            
        # Llenar el Treeview con los datos
        for registro in registros:
            tree.insert("", "end", values=registro)


    searchFrame = tk.Frame(root, background="#12355B")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Usuario", "Contraseña"], width=30)
    comboSearch.pack(side="left", padx=17)

    # TextBox para mostrar los resultados
    search = tk.Entry(searchFrame, width=30, font=fontText)
    search.pack(side="left", padx=17)

    # Botón para realizar la búsqueda
    searchButton = tk.Button(searchFrame, text="Buscar", width=30, height=1, command=columnSearch, font=fontText, background="#12355B", foreground="#fefefe")
    searchButton.pack(side="left", padx=17)

    # Treeview
    tree_frame = tk.Frame(root, background="#12355B")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Usuario", "Usuario", "Contraseña"))

    for c in range(1,3):
        tree.column(f"#{c}", width=250, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#3", width=250, anchor="center")

    headings = ["Cod Usuario", "Usuario", "Contraseña"]

    for e in range(3):
        headNum = [1,2,3]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # Colocar el Treeview usando grid
    tree.grid(row=0, column=0, sticky="nsew")

    # Colocar el scrollbar junto al Treeview usando grid
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configurar el peso de las filas y columnas para que el Treeview se expanda correctamente
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    # Etiquetas y TextBox
    textbox_frame = tk.Frame(root, background="#12355B")
    textbox_frame.pack(pady=10)

    labels = ["Cod de Usuario", "Usuario", "Contraseña"]

    for i in range(len(labels)):
        label = tk.Label(textbox_frame, text=labels[i], background="#12355B", foreground="#fefefe", font=fontText)
        label.grid(row=1, column=i, padx=10, pady=5)
        labels.append(label)

    textboxes = []
    text_vars = []  # Lista para almacenar las variables StringVar

    for x in range(3):
        text_var = tk.StringVar()  # Crea una nueva variable StringVar
        text_vars.append(text_var)  # Agrega la variable a la lista

        textbox = tk.Entry(textbox_frame, textvariable=text_var, width=20)
        textbox.grid(row=2, column=x, padx=10, pady=5)
        textboxes.append(textbox)  # Agrega la caja de entrada a la lista

    # Asigna nombres a las variables StringVar
    cod_user_var, user_var, pass_var = text_vars

    btn_frame = tk.Frame(root, background="#12355B")
    btn_frame.pack(pady=10, padx=2)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=15, height=1, background="#12355B", foreground="#fefefe", font=fontText)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=15, height=1, background="#12355B", foreground="#fefefe", font=fontText)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=15, height=1, background="#12355B", foreground="#fefefe", font=fontText)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=15, height=1, background="#12355B", foreground="#fefefe", font=fontText)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    ventanaAcceso()


try:
    cursor.close()
    conexion.close()

except Exception as e:
    messagebox.showerror("Error", f"Ocurrió un error al cerrar la conexion a la base de datos.")

