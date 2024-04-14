import random
import sqlite3

class Recetas:
    def __init__(self, ingesta_calorica, num_comidas, alimentos_no_preferidos=None, usuario=None):
        self.ingesta_calorica = ingesta_calorica
        self.num_comidas = num_comidas
        self.alimentos_no_preferidos = alimentos_no_preferidos if alimentos_no_preferidos else []
        self.usuario = usuario
        self.db_connection = sqlite3.connect('mi_base_de_datos.db')
        self.cursor = self.db_connection.cursor()

    def obtener_platillos(self, max_calorias):
        placeholders = ','.join(['?' for _ in range(len(self.alimentos_no_preferidos))])
        problemas_salud_condition = " AND colesterol = 0" if self.usuario.problemas_salud.lower() == 'si' else ""  # Aquí se filtran los platillos según los problemas de salud

        # Consulta para obtener platillos principales
        query = f"SELECT nombre, calorias FROM desayunos WHERE calorias <= ? AND nombre NOT IN ({placeholders}){problemas_salud_condition}"
        params = [max_calorias] + self.alimentos_no_preferidos
        self.cursor.execute(query, params)
        platillos_principales = self.cursor.fetchall()

        # Consulta para obtener aperitivos  
        max_calorias_aperitivo = max_calorias // 2  # Define un límite para las calorías de los aperitivos
        query_aperitivos = f"SELECT nombre, calorias FROM aperitivos WHERE calorias <= ? AND nombre NOT IN ({placeholders}){problemas_salud_condition}"
        self.cursor.execute(query_aperitivos, [max_calorias_aperitivo] + self.alimentos_no_preferidos)
        aperitivos = self.cursor.fetchall()

        # Combina platillos principales y aperitivos
        platillos = platillos_principales + aperitivos

        return platillos        

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

        # Si las calorías consumidas superan la ingesta calórica recomendada por día,
        # se intenta ajustar eliminando un platillo de la receta
            while total_calorias_platillos > self.ingesta_calorica + 200:
                platillo_eliminado = receta.pop()
                total_calorias_platillos -= platillo_eliminado[1]

        # Si las calorías consumidas están por debajo de la ingesta calórica recomendada por día
        # y aún hay espacio para más calorías, se agregan aperitivos
            while total_calorias_platillos < self.ingesta_calorica - 200 and max_calorias > 0:
                aperitivos = self.obtener_platillos(max_calorias)
                if not aperitivos:
                    break
                aperitivo = random.choice(aperitivos)
                receta.append(aperitivo)
                total_calorias_platillos += aperitivo[1]

        return receta, total_calorias_platillos

class Usuario:
    def __init__(self, sexo, peso, altura, edad, nivel_actividad, objetivo, num_comidas, alimentos_no_preferidos, problemas_salud=None):
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.nivel_actividad = nivel_actividad
        self.objetivo = objetivo
        self.num_comidas = num_comidas
        self.alimentos_no_preferidos = alimentos_no_preferidos
        self.problemas_salud = problemas_salud

    def calcular_ingesta_calorica(self, tmb):
        nivel_actividad_validos = ['sedentario', 'ligero', 'moderado', 'intenso']
        objetivo_validos = ['perder', 'mantener', 'ganar']

        if self.nivel_actividad not in nivel_actividad_validos:
            print("Nivel de actividad no válido. Por favor, elige entre: sedentario, ligero, moderado, intenso.")
            return None

        if self.objetivo not in objetivo_validos:
            print("Objetivo no válido. Por favor, elige entre: perder, mantener, ganar.")
            return None

        if self.nivel_actividad == 'sedentario':
            factor_actividad = 1.2
        elif self.nivel_actividad == 'ligero':
            factor_actividad = 1.375
        elif self.nivel_actividad == 'moderado':
            factor_actividad = 1.55
        elif self.nivel_actividad == 'intenso':
            factor_actividad = 1.725
        else:
            print("Nivel de actividad no válido.")
            return None

        if self.objetivo == 'perder':
            factor_objetivo = 0.85
        elif self.objetivo == 'mantener':
            factor_objetivo = 1
        elif self.objetivo == 'ganar':
            factor_objetivo = 1.15
        else:
            print("Objetivo no válido.")
            return None

        ingesta_calorica = tmb * factor_actividad * factor_objetivo
        return ingesta_calorica

    def calcular_tmb(self):
        if self.sexo.lower() == 'masculino':
            tmb = 10 * self.peso + 6.25 * self.altura - 5 * self.edad + 5
        elif self.sexo.lower() == 'femenino':
            tmb = 10 * self.peso + 6.25 * self.altura - 5 * self.edad - 161
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
    
    problemas_salud = input("¿Tienes algún problema de salud como colesterol alto? (si/no): ")
    if problemas_salud.lower() == 'si':
        alimentos_no_preferidos_input = input("¿Hay algún alimento que no prefieras? (separa los alimentos con comas, por ejemplo: lechuga, tomate): ")
        if alimentos_no_preferidos_input.strip():  # Verifica si la entrada no está vacía
                alimentos_no_preferidos = alimentos_no_preferidos_input.split(',')
        else:
            alimentos_no_preferidos = [] 
    else:
        alimentos_no_preferidos = []

    usuario = Usuario(sexo, peso, altura, edad, nivel_actividad, objetivo, num_comidas, alimentos_no_preferidos, problemas_salud)

    tmb = usuario.calcular_tmb()
    if tmb is not None:
        ingesta_calorica = usuario.calcular_ingesta_calorica(tmb)

        if ingesta_calorica is not None:
            recetas = Recetas(ingesta_calorica, num_comidas, alimentos_no_preferidos, usuario)
            dieta = recetas.generar_dieta()

            if not dieta:
                print("No se pudo generar la dieta. Por favor, intenta ajustar tus preferencias.")
                return

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

    # Cerrar conexión de base de datos
    recetas.db_connection.close()

if __name__ == "__main__":
    main()

