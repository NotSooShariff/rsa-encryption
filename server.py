import socket
import rsa

# Generate RSA key pair 
(public_key, private_key) = rsa.newkeys(512)

# Create a socket server just like the CN class shit
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
print("Server listening on port 12345")
client_socket, client_address = server_socket.accept()
print("Accepted connection from", client_address)

# Send the public key to the client & do the reading and shit
public_key_data = public_key.save_pkcs1()
client_socket.send(public_key_data)
encrypted_message = client_socket.recv(1024)
print("Received encrypted message:", encrypted_message)
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
print("Decrypted message:", decrypted_message)

client_socket.close()
server_socket.close()
