import psycopg2

# 1. Parámetros de conexión (Tus datos personalizados)
host = "localhost"
port = "5432"
database = "prueba" # Asegúrate que esta DB exista en tu servidor
user = "postgres"
password = "321321"

try:
    # Crear la conexión
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        dbname=database,
        password=password
    )

    # Crear cursor para ejecutar consultas
    cursor = conn.cursor()
    print("✅ Conexión exitosa a PostgreSQL")

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM clientes LIMIT 5;") 

    # Mostrar resultados
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("❌ Error al conectar:", e)

finally:
    # Cerrar la conexión
    if 'conn' in locals():
        conn.close()