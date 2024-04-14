import random
import sqlite3
db_connection = sqlite3.connect('mi_base_de_datos.db')
cursor = db_connection.cursor()
class Recetas:
    def __init__(self, ingesta_calorica, num_comidas, alimentos_no_preferidos=None):
        self.ingesta_calorica = ingesta_calorica
        self.num_comidas = num_comidas
        self.alimentos_no_preferidos = alimentos_no_preferidos if alimentos_no_preferidos else []
        self.db_connection = sqlite3.connect('mi_base_de_datos.db')
        self.cursor = self.db_connection.cursor()

    def obtener_platillos(self, max_calorias):
        print("Alimentos no preferidos:", self.alimentos_no_preferidos)
        # Creamos una cadena de signos de interrogación para los alimentos no preferidos
        placeholders = ','.join(['?' for _ in range(len(self.alimentos_no_preferidos))])
        # Creamos la consulta SQL con los placeholders para los alimentos no preferidos
        query = f"SELECT nombre, calorias FROM desayunos WHERE calorias <= ? AND nombre NOT IN ({placeholders})"
        # Creamos la lista de parámetros para la consulta SQL
        params = [max_calorias] + self.alimentos_no_preferidos
        print("Query:", query)
        print("Parámetros:", params)
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def generar_dieta(self):
        dieta = {}
        for dia in range(1, 8):
            dieta[dia] = self.generar_receta()
        return dieta

    def generar_receta(self):
        receta = []
        total_calorias_platillos = 0
        for _ in range(self.num_comidas):
            max_calorias = self.ingesta_calorica - total_calorias_platillos
            platillos = self.obtener_platillos(max_calorias)
            if not platillos:
                break
            platillo = random.choice(platillos)
            receta.append(platillo)
            total_calorias_platillos += platillo[1]
        return receta, total_calorias_platillos

def calcular_ingesta_calorica(tmb, nivel_actividad, objetivo):
    if nivel_actividad == 'sedentario':
        factor_actividad = 1.2
    elif nivel_actividad == 'ligero':
        factor_actividad = 1.375
    elif nivel_actividad == 'moderado':
        factor_actividad = 1.55
    elif nivel_actividad == 'intenso':
        factor_actividad = 1.725
    else:
        print("Nivel de actividad no válido.")
        return None
    
    if objetivo == 'perder':
        factor_objetivo = 0.85
    elif objetivo == 'mantener':
        factor_objetivo = 1
    elif objetivo == 'ganar':
        factor_objetivo = 1.15
    else:
        print("Objetivo no válido.")
        return None
    
    ingesta_calorica = tmb * factor_actividad * factor_objetivo
    return ingesta_calorica

def calcular_tmb(sexo, peso, altura, edad):
    if sexo.lower() == 'masculino':
        tmb = 10 * peso + 6.25 * altura - 5 * edad + 5
    elif sexo.lower() == 'femenino':
        tmb = 10 * peso + 6.25 * altura - 5 * edad - 161
    else:
        print("Sexo no válido. Introduce 'masculino' o 'femenino'.")
        return None
    return tmb

def main():
    print("¡Bienvenido/a al generador de dietas saludables!")
    sexo = input("¿Cuál es tu sexo? (masculino/femenino): ")
    peso = float(input("¿Cuál es tu peso en kilogramos?: "))
    altura = float(input("¿Cuál es tu altura en centímetros?: "))
    edad = int(input("¿Cuál es tu edad?: "))
    nivel_actividad = input("¿Cuál es tu nivel de actividad física? (sedentario/ligero/moderado/intenso): ")
    objetivo = input("¿Cuál es tu objetivo de peso? (perder/mantener/ganar): ")
    num_comidas = int(input("¿Cuántas comidas deseas tener al día?: "))

    alimentos_no_preferidos = input("¿Hay algún alimento que no prefieras? (separa los alimentos con comas, por ejemplo: lechuga, tomate): ").split(',')

    tmb = calcular_tmb(sexo, peso, altura, edad)
    if tmb is not None:
        ingesta_calorica = calcular_ingesta_calorica(tmb, nivel_actividad, objetivo)

        recetas = Recetas(ingesta_calorica, num_comidas, alimentos_no_preferidos)
        dieta = recetas.generar_dieta()

        print("\n¡Aquí está tu dieta saludable para la semana!")
        for dia, (receta_dia, total_calorias) in dieta.items():
            print(f"\nDía {dia}:")
            for i, (nombre_platillo, calorias_platillo) in enumerate(receta_dia, start=1):
                print(f"Comida {i}:")
                print(f"Platillo: {nombre_platillo} - Calorías: {calorias_platillo}")
            print(f"Total de calorías para el día: {total_calorias}")

        print(f"\nTu ingesta calórica recomendada es de aproximadamente {int(ingesta_calorica)} calorías por día.")

        print("\nDatos personales:")
        print(f"Sexo: {sexo}")
        print(f"Peso: {peso} kg")
        print(f"Altura: {altura} cm")
        print(f"Edad: {edad}")
        print(f"Nivel de actividad física: {nivel_actividad}")
        print(f"Objetivo de peso: {objetivo}")

if __name__ == "__main__":
    main()