import csv
import os

ARCHIVO = "inventario.csv"

def menu():
    print("\n--- Menú Inventario ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(["Nombre", "Cantidad", "Precio"])

def ver_inventario():
    with open(ARCHIVO, newline='') as file:
        lector = csv.reader(file)
        next(lector, None)  # Saltar encabezado
        productos = list(lector)
        if not productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for fila in productos:
                print(f"Nombre: {fila[0]}, Cantidad: {fila[1]}, Precio: ${fila[2]}")

def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    cantidad = input("Cantidad: ").strip()
    precio = input("Precio: ").strip()

    if not nombre or not cantidad.isdigit() or not precio.replace('.', '', 1).isdigit():
        print("Entrada no válida. Inténtalo de nuevo.")
        return

    with open(ARCHIVO, "a", newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow([nombre, cantidad, precio])
    print("✅ Producto agregado.")

def buscar_producto():
    nombre = input("Nombre a buscar: ").strip()
    with open(ARCHIVO, newline='') as file:
        lector = csv.reader(file)
        next(lector, None)
        for fila in lector:
            if fila and fila[0].lower() == nombre.lower():
                print(f"🔍 Producto encontrado: Nombre: {fila[0]}, Cantidad: {fila[1]}, Precio: ${fila[2]}")
                return
        print("❌ Producto no encontrado.")

def eliminar_producto():
    nombre = input("Producto a eliminar: ").strip()
    filas = []
    encontrado = False

    with open(ARCHIVO, newline='') as file:
        lector = csv.reader(file)
        encabezado = next(lector, None)
        for fila in lector:
            if fila and fila[0].lower() != nombre.lower():
                filas.append(fila)
            else:
                encontrado = True

    with open(ARCHIVO, "w", newline='') as file:
        escritor = csv.writer(file)
        if encabezado:
            escritor.writerow(encabezado)
        escritor.writerows(filas)

    if encontrado:
        print("🗑️ Producto eliminado.")
    else:
        print("❌ Producto no encontrado.")

# --- Programa principal ---
inicializar_archivo()

while True:
    menu()
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        ver_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("👋 Saliendo...")
        break
    else:
        print("⚠️ Opción inválida.")
