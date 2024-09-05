import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = data_entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

        # Convert the image to a PhotoImage and display it in the window
        qr_image = Image.open("qrcode.png")
        qr_photo = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo

        messagebox.showinfo("Success", "QR Code generated successfully!")
    else:
        messagebox.showwarning("Error", "Please enter some data.")

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("qrcode.png")
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved as {file_path}")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# Label
label = tk.Label(root, text="Enter values or a web link:")
label.pack()

# Entry
data_entry = tk.Entry(root, width=50)
data_entry.pack()

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack()

# Button to save QR code
save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack()

# Run the Tkinter event loop
root.mainloop()
