-- Tablas

CREATE TABLE alertas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  estudiante_id INTEGER NOT NULL,
  docente_id INTEGER NOT NULL,
  grupo_id INTEGER NOT NULL,
  mensaje TEXT NOT NULL,
  fecha TEXT NOT NULL
);

CREATE TABLE asignaturas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  descripcion TEXT
);

CREATE TABLE asistencias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  estudiante_id INTEGER NOT NULL,
  fecha TEXT NOT NULL,
  presente INTEGER NOT NULL
);

CREATE TABLE calificaciones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  estudiante_id INTEGER NOT NULL,
  asignatura_id INTEGER NOT NULL,
  calificacion REAL NOT NULL,
  fecha TEXT NOT NULL
);

CREATE TABLE grupos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  grado INTEGER NOT NULL,
  institucion_id INTEGER NOT NULL
);

CREATE TABLE grupo_usuario (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  grupo_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL
);

CREATE TABLE instituciones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL
);

CREATE TABLE padre_estudiante (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  padre_id INTEGER NOT NULL,
  estudiante_id INTEGER NOT NULL
);

CREATE TABLE roles_user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  nombre TEXT,
  apellido TEXT,
  rol_id INTEGER NOT NULL,
  institucion_id INTEGER NOT NULL
);

-- Datos de ejemplo

INSERT INTO asignaturas (id, nombre, descripcion) VALUES
(1, 'Matemáticas', 'Fomenta el razonamiento lógico, la resolución de problemas y el uso de herramientas matemáticas para situaciones cotidianas y académicas.'),
(2, 'Comunicación', 'Desarrolla habilidades de lectura, escritura, expresión oral y comprensión de textos, promoviendo el pensamiento crítico y la capacidad de argumentar.'),
(3, 'Ciencias Sociales', 'Estudia la sociedad, la historia, la geografía, la economía y la política, ayudando a comprender el entorno social y fomentar una ciudadanía responsable.'),
(4, 'Inglés', 'Enseña el uso del idioma inglés en sus formas oral y escrita, para comunicarse de forma efectiva en contextos personales, académicos y profesionales.'),
(5, 'Arte y Cultura', 'Promueve la expresión creativa a través de diversas formas artísticas, apreciando la diversidad cultural y desarrollando la sensibilidad estética.'),
(6, 'Arte y Cultura', 'Promueve la expresión creativa a través de diversas formas artísticas, apreciando la diversidad cultural y desarrollando la sensibilidad estética.');

INSERT INTO grupos (id, nombre, grado, institucion_id) VALUES
(1, '1°A', 1, 1),
(2, '2°A', 2, 1),
(3, '3°A', 3, 1),
(4, '4°A', 4, 1),
(5, '5°A', 5, 1),
(6, '1°B', 1, 2),
(7, '2°B', 2, 2),
(8, '3°B', 3, 2),
(9, '4°B', 4, 2),
(10, '5°B', 5, 2),
(11, '1° secundaria "A"', 1, 1),
(12, 'Sección A', 1, 1),
(13, 'Sección A', 1, 1),
(14, 'Sección A', 1, 1);

INSERT INTO instituciones (id, nombre) VALUES
(1, 'Colegio Nacional San Martín'),
(2, 'Moderno América'),
(3, 'Monitor Huascar'),
(4, 'Santo Domingo');

INSERT INTO roles_user (id, nombre) VALUES
(1, 'Administrador'),
(2, 'Docente'),
(3, 'Padre');

INSERT INTO users (id, username, password, email, nombre, apellido, rol_id, institucion_id) VALUES
(1, 'Joyce S.A', 'nininini', '2023024207@unfv.edu.pe', 'Joyce', 'Santamaria Abanto', 2, 1),
(5, 'karla', 'blancus', 'karla_ros_1788@hotmail.com', 'karla', 'Giraldo Montero', 1, 1),
(6, 'Jonatan', 'picado', '2023023923@unfv.edu.pe', 'Jonatan', 'Larico Alarcon ', 3, 1),
(7, 'Denis', '1', 'denisvila@hotmail.com', 'Denis', 'Vila Tommy', 3, 1),
(8, 'Isabella', '08874521', 'risabela_1987@hotmail.com', 'Isabella Daniela', 'Ramirez Martinez', 3, 1),
(9, 'Carmelo', '08563287', 'CHurtado.745@hotmail.com', 'Carmelo', 'Hurtado Mendez', 3, 1),
(10, 'Lupe', '08763289', 'lopezluz.7584@hotmail.com', 'Luz Lupe', 'Lopez Larico', 3, 1);