# RSA Encryption and Chat Application (PoC Test)

This is a simple Flask application that I wrote which demonstrates the use of RSA encryption for secure communication just to play around with python libraries. However, please note that this is not meant to be a secure implementation or a suitable foundation for a production chat application. It lacks proper user authentication and user management. User emails and passwords are hard-coded for demonstration purposes only.

## ⚒️ Installation and Setup

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

3. Clone this repository:

   ```
   git clone https://github.com/NotSooShariff/RSA-Encryption.git
   ```
   
2. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

4. Change to the project directory:

   ```
   cd RSA-Encryption
   ```

## ▶️ Running the Application

You can run the application by executing the following command in your terminal:

```
python app.py
```


## 📦 Usage

- Access the application in your web browser at `http://localhost:5000`.
- The application allows you to create chat rooms and join existing ones.
- You can send messages within chat rooms, and they will be encrypted using a combination of Caesar Cipher and RSA encryption.
- When sending a message, the system uses your hard-coded user email and password to identify you.

## 📄 Code Structure

- `app.py`: The main Flask application that defines routes and handles WebSocket communication.
- `templates/`: Contains HTML templates for the web pages.
- `myenv/`: Contains the python virtual environment
- `requirements.txt`: Contains all the packages and versions needed to run this tool

## 📌 Important Note

This application is only for educational purposes and should not be used in a real-world scenario. It lacks essential security features and user authentication mechanisms, making it unsuitable for a secure chat application. The user credentials are hard-coded, and encryption is rudimentary. Do not use this code as a basis for any production system.

Feel free to explore and experiment with RSA encryption, but be aware of its limitations and the need for comprehensive security measures in real-world applications.
