import tkinter as tk
import socket
import rsa

def send_encrypted_message():
    message = entry.get()
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    client_socket.send(encrypted_message)
    entry.delete(0, tk.END)

def quit_application():
    client_socket.close()
    root.quit()

# The socket client shit we did in CN class
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))
print("Connected to server")

# Receive the server's public key (also familiar syntax from CN lab)
public_key_data = client_socket.recv(1024)
public_key = rsa.PublicKey.load_pkcs1(public_key_data)

# Create the GUI (a little diff to understand if you havent ever used tkinter)
root = tk.Tk()
root.title("RSA Encryption Client")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter a message to encrypt and send:")
label.pack()

entry = tk.Entry(frame, width=40)
entry.pack()

send_button = tk.Button(frame, text="Send Encrypted Message", command=send_encrypted_message)
send_button.pack()

quit_button = tk.Button(frame, text="Quit", command=quit_application)
quit_button.pack()

root.mainloop()
