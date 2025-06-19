from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'clave_secreta'

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datos_bd"
    )

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conexion = get_db()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        if usuario:
            session['usuario_id'] = usuario['id']
            session['rol_id'] = usuario['rol_id']
            # Redirige según el rol
            if usuario['rol_id'] == 1:
                return redirect(url_for('admin_dashboard'))
            elif usuario['rol_id'] == 2:
                return redirect(url_for('docente_dashboard'))
            elif usuario['rol_id'] == 3:
                return redirect(url_for('estudiante_dashboard'))
            elif usuario['rol_id'] == 4:
                return redirect(url_for('padre_dashboard'))
        else:
            mensaje = "Usuario o contraseña incorrectos."
    return render_template('login.html', mensaje=mensaje)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if session.get('rol_id') != 1:
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

@app.route('/docente/dashboard')
def docente_dashboard():
    if session.get('rol_id') != 2:
        return redirect(url_for('login'))
    return render_template('docente_dashboard.html')

@app.route('/estudiante/dashboard')
def estudiante_dashboard():
    if session.get('rol_id') != 3:
        return redirect(url_for('login'))
    return render_template('estudiante_dashboard.html')

@app.route('/padre/dashboard')
def padre_dashboard():
    if session.get('rol_id') != 4:
        return redirect(url_for('login'))
    return render_template('padre_dashboard.html')

@app.route('/admin/nueva_institucion', methods=['GET', 'POST'])
def nueva_institucion():
    if session.get('rol_id') != 1:
        return redirect(url_for('login'))
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        conexion = get_db()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO instituciones (nombre) VALUES (%s)", (nombre,))
        conexion.commit()
        cursor.close()
        conexion.close()
        mensaje = "Institución registrada correctamente."
    return render_template('nueva_institucion.html', mensaje=mensaje)

@app.route('/admin/nuevo_grupo', methods=['GET', 'POST'])
def nuevo_grupo():
    if session.get('rol_id') != 1:
        return redirect(url_for('login'))
    mensaje = None
    conexion = get_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM instituciones")
    instituciones = cursor.fetchall()
    if request.method == 'POST':
        nombre = request.form['nombre']
        grado = request.form['grado']
        institucion_id = request.form['institucion_id']
        cursor.execute("INSERT INTO grupos (nombre, grado, institucion_id) VALUES (%s, %s, %s)", (nombre, grado, institucion_id))
        conexion.commit()
        mensaje = "Grupo registrado correctamente."
    cursor.close()
    conexion.close()
    return render_template('nuevo_grupo.html', mensaje=mensaje, instituciones=instituciones)

@app.route('/admin/nueva_asignatura', methods=['GET', 'POST'])
def nueva_asignatura():
    if session.get('rol_id') != 1:
        return redirect(url_for('login'))
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        conexion = get_db()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO asignaturas (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conexion.commit()
        cursor.close()
        conexion.close()
        mensaje = "Asignatura registrada correctamente."
    return render_template('nueva_asignatura.html', mensaje=mensaje)

@app.route('/admin/nuevo_usuario', methods=['GET', 'POST'])
def nuevo_usuario():
    if session.get('rol_id') != 1:
        return redirect(url_for('login'))
    mensaje = None
    conexion = get_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM roles_user")
    roles = cursor.fetchall()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rol_id = request.form['rol_id']
        cursor.execute(
            "INSERT INTO users (username, password, email, nombre, apellido, rol_id) VALUES (%s, %s, %s, %s, %s, %s)",
            (username, password, email, nombre, apellido, rol_id)
        )
        conexion.commit()
        mensaje = "Usuario registrado correctamente."
    cursor.close()
    conexion.close()
    return render_template('nuevo_usuario.html', mensaje=mensaje, roles=roles)

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    mensaje = None
    rol_nombre = None
    institucion_nombre = None
    conexion = get_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM roles_user")
    roles = cursor.fetchall()
    cursor.execute("SELECT id, nombre FROM instituciones")
    instituciones = cursor.fetchall()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rol_id = request.form['rol_id']
        institucion_id = request.form['institucion_id']
        try:
            cursor.execute(
                "INSERT INTO users (username, password, email, nombre, apellido, rol_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (username, password, email, nombre, apellido, rol_id)
            )
            user_id = cursor.lastrowid
            # Si quieres asignar a un grupo, aquí puedes hacerlo
            # Busca los nombres para mostrar en el mensaje
            cursor.execute("SELECT nombre FROM roles_user WHERE id=%s", (rol_id,))
            rol_nombre = cursor.fetchone()[0]
            cursor.execute("SELECT nombre FROM instituciones WHERE id=%s", (institucion_id,))
            institucion_nombre = cursor.fetchone()[0]
            mensaje = "¡Registro exitoso!"
        except Exception as e:
            mensaje = "Error: " + str(e)
    cursor.close()
    conexion.close()
    return render_template('registrarse.html', mensaje=mensaje, roles=roles, instituciones=instituciones, rol_nombre=rol_nombre, institucion_nombre=institucion_nombre)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/apoyo')
def apoyo():
    return render_template('apoyo.html')

@app.route('/olvidaste', methods=['GET', 'POST'])
def olvidaste():
    mensaje = None
    if request.method == 'POST':
        email = request.form['email']
        # Aquí podrías buscar el usuario y enviar un correo real
        mensaje = "Si el correo existe en el sistema, recibirás instrucciones para restablecer tu contraseña."
    return render_template('olvidaste.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)