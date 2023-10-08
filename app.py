from flask import Flask, render_template, request, redirect, url_for, session
import rsa
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dictionary to store chat rooms and messages
chat_rooms = {}

# Function to generate a random chat code
def generate_chat_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create', methods=['POST'])
def create_chat():
    chat_code = generate_chat_code()
    chat_rooms[chat_code] = {
        'messages': [],
        'public_key': rsa.newkeys(512)[0]  # Generate RSA public key for this chat
    }
    return redirect(url_for('chat', chat_code=chat_code))

@app.route('/enter', methods=['POST'])
def enter_chat():
    chat_code = request.form['chat_code']
    if chat_code in chat_rooms:
        return redirect(url_for('chat', chat_code=chat_code))
    else:
        return "Chat room not found."

@app.route('/chat/<chat_code>', methods=['GET', 'POST'])
def chat(chat_code):
    if chat_code not in chat_rooms:
        return "Chat room not found."

    if request.method == 'POST':
        message = request.form['message']
        encrypted_message = rsa.encrypt(message.encode(), chat_rooms[chat_code]['public_key'])
        chat_rooms[chat_code]['messages'].append({
            'sender': 'You',
            'message': message,
            'encrypted_message': encrypted_message,
        })

    return render_template('chat.html', chat_code=chat_code, messages=chat_rooms[chat_code]['messages'])

if __name__ == '__main__':
    app.run(debug=True)
