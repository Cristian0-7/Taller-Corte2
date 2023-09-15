import pyodbc
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


connection_string = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:C:C:\Users\CUC\Documents\TasksDB.accdb;"
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

@app.route('/')
def index():
    return 

@app.route('/Tareas')
def Tareas():
    cursor.execute("SELECT * FROM Tareas")
    Tareas = cursor.fetchall()
    return render_template('Tareas.html', add_Tareas=Tareas)

@app.route('/add_Tareas', methods=['POST'])
def add_Tareas():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cursor.execute("INSERT INTO tareas (title, description, done) VALUES (?, ?, ?)", (title, description, False))
        conn.commit()
    return redirect('/tareas')

@app.route('/complete_tareas/<int:id>')
def complete_Tareas(id):
    cursor.execute("UPDATE Tareas SET done = True WHERE id = ?", (id,))
    conn.commit()
    return redirect('/Tareas')

@app.route('/delete_Tareas/<int:id>')
def delete_Tareas(id):
    cursor.execute("DELETE FROM Tareas WHERE id = ?", (id,))
    conn.commit()
    return redirect('/tareas')

if __name__ == '__main__':
    app.run(debug=True)
