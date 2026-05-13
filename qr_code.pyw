
from tkinter import messagebox
import customtkinter as ctk 
import qrcode 
from PIL import Image 
import os
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppQR(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Generator")
        self.geometry("400x550")

        icon_base = os.path.dirname(__file__)
        icon_ruta = os.path.join(icon_base, "icono_qr.ico")
        self.iconbitmap(icon_ruta)

        self.label_titulo = ctk.CTkLabel(self, text="Generador de QR", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        self.entry_link = ctk.CTkEntry(self, placeholder_text="Pega tu link aquí", width=300)
        self.entry_link.pack(pady=10)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre del archivo (sin .png)", width=300)
        self.entry_nombre.pack(pady=10)

        self.boton_generar = ctk.CTkButton(self, text="Generar y Guardar", command=self.generar_qr)
        self.boton_generar.pack(pady=20)

        self.label_imagen = ctk.CTkLabel(self, text="") 
        self.label_imagen.pack(pady=10)

    def generar_qr(self):
        link = self.entry_link.get()
        nombre = self.entry_nombre.get()

        if not link or not nombre:
            messagebox.showerror("Error", "Por favor rellena ambos campos.")
            return

        nombre_archivo = f"{nombre}.png"

        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nombre_archivo)

        # --- Mostrar la imagen en la ventana ---
        img_qr = Image.open(nombre_archivo)
        img_ctk = ctk.CTkImage(light_image=img_qr, dark_image=img_qr, size=(200, 200))
        
        self.label_imagen.configure(image=img_ctk)
        self.label_imagen.image = img_ctk 

        # --- VENTANA EMERGENTE ---
        messagebox.showinfo("¡Logrado!", f"Tu QR ha sido guardado con éxito como:\n{nombre_archivo}")

        
        self.entry_link.delete(0, 'end')
        self.entry_nombre.delete(0, 'end')
            

if __name__ == "__main__":
    app = AppQR()
    app.mainloop()
