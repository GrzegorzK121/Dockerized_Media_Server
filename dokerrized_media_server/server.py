from flask import Flask, render_template, request, redirect, url_for, session
import os
import sqlite3

app = Flask(__name__, static_folder='static')
app.secret_key = 'supersecretkey'
DB_FILE = "users.db"
FILES_DIR = "files"
ALLOWED_EXTENSIONS = {"jpg", "png", "mp4"}

# Funkcja do inicjalizacji bazy danych i dodania konta admina
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL,
                      role TEXT NOT NULL)''')
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'admin', 'admin')")
    conn.commit()
    conn.close()

# Inicjalizacja bazy przy starcie aplikacji
init_db()

@app.context_processor
def inject_user():
    return dict(user=session.get('user'), role=session.get('role'))

@app.route('/')
def index():
    files = os.listdir(FILES_DIR) if os.path.exists(FILES_DIR) else []
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.split('.')[-1] in ALLOWED_EXTENSIONS:
            file.save(os.path.join(FILES_DIR, file.filename))
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user'] = username
            session['role'] = user[0]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Nieprawidłowe dane logowania")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, 'user'))
            conn.commit()
        except sqlite3.IntegrityError:
            return render_template('register.html', error="Nazwa użytkownika jest już zajęta")
        finally:
            conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs(FILES_DIR, exist_ok=True)
    app.run(host='192.168.88.3', port=5000, debug=True)
