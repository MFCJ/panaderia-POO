
def main():
# Lista de prueba
    productos_prueba = [
        {"nombre": "Pan", "precio": 500, "tipo": "unidad"},
        {"nombre": "Leche", "precio": 800, "tipo": "unidad"},
        {"nombre": "Harina", "precio": 1200, "tipo": "peso"}
    ]
    for i, pro in enumerate (productos_prueba, start =1):
        print (f"{i}. {productos_prueba[i-1]["nombre"]} - 
               {productos_prueba[i-1]["precio"]} - {productos_prueba[i-1]["tipo"]}")
# Intenta mostrar:
# 1. Pan - $500 (unidad)
# 2. Leche - $800 (unidad)
# 3. Harina - $1200 (peso)
        
if __name__ == "__main__":
    main()