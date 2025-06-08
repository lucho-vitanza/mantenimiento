from parser_equipo import parsear_equipo, obtener_nombre_desde_id, obtener_id_desde_nombre

def test_equipo_por_id():
    texto = "Quiero detalles del equipo 10009195."
    equipo_id, nombre_equipo = parsear_equipo(texto)
    assert equipo_id == "10009195", f"ID incorrecto: {equipo_id}"
    assert nombre_equipo == "ATORNILLADORA NEUMATICA 2", f"Nombre incorrecto: {nombre_equipo}"
    print("✅ Encontrado por ID en parsear_equipo:", equipo_id, nombre_equipo)

def test_equipo_por_nombre():
    texto = "¿Qué se sabe de la ATORNILLADORA NEUMATICA 2?"
    equipo_id, nombre_equipo = parsear_equipo(texto)
    assert equipo_id == "10009195", f"ID incorrecto: {equipo_id}"
    assert nombre_equipo == "ATORNILLADORA NEUMATICA 2", f"Nombre incorrecto: {nombre_equipo}"
    print("✅ Encontrado por nombre en parsear_equipo:", equipo_id, nombre_equipo)

def test_obtener_nombre_desde_id():
    nombre = obtener_nombre_desde_id("10009195")
    assert nombre == "ATORNILLADORA NEUMATICA 2", f"Nombre incorrecto desde ID: {nombre}"
    print("✅ obtener_nombre_desde_id correcto:", nombre)

def test_obtener_id_desde_nombre():
    equipo_id = obtener_id_desde_nombre("ATORNILLADORA NEUMATICA 2")
    assert equipo_id == "10009195", f"ID incorrecto desde nombre: {equipo_id}"
    print("✅ obtener_id_desde_nombre correcto:", equipo_id)




if __name__ == "__main__":
    test_equipo_por_id()
    test_equipo_por_nombre()
    test_obtener_nombre_desde_id()
    test_obtener_id_desde_nombre()