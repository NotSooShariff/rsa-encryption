from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
import rsa
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

user_credentials = {
    'user1@example.com': 'password1',
    'user2@example.com': 'password2',
    'user3@example.com': 'password3',
    # Add more email-password pairs as needed
}

# Dictionary to store chat rooms and their creators
chat_rooms = {}

# Function to generate a random chat code
def generate_chat_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/')
def home():
    if 'logged_in' not in session:
        session['logged_in'] = False

    chat_rooms_data = None

    # Provide chat_rooms in the context if the user is logged in
    if session['logged_in']:
        chat_rooms_data = chat_rooms

    return render_template('home.html', chat_rooms=chat_rooms_data)


@app.route('/create', methods=['POST'])
def create_chat():
    chat_code = generate_chat_code()
    creator_email = session.get('email')  # Get the email of the logged-in user
    chat_rooms[chat_code] = {
        'creator_email': creator_email,
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

@app.route('/chat/<chat_code>')
def chat(chat_code):
    if chat_code not in chat_rooms:
        return "Chat room not found."

    return render_template('chat.html', chat_code=chat_code, messages=chat_rooms[chat_code]['messages'])

@socketio.on('send_message')
def handle_message(data):
    chat_code = data['chat_code']
    message = data['message']
    encrypted_message = rsa.encrypt(message.encode(), chat_rooms[chat_code]['public_key'])
    chat_rooms[chat_code]['messages'].append({
        'sender': 'You',
        'message': message,
        'encrypted_message': encrypted_message,
    })
    emit('update_messages', chat_rooms[chat_code]['messages'], broadcast=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email exists in the user_credentials dictionary and the password is correct
        if email in user_credentials and user_credentials[email] == password:
            session['logged_in'] = True
            session['email'] = email  # Store the email in the session
            return redirect(url_for('home'))
        else:
            return "Invalid email or password."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove the 'logged_in' session variable
    return redirect(url_for('login'))

if __name__ == '__main__':
    socketio.run(app, debug=True)