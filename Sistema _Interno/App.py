def determinar_peso_segun_recomendacion_medica(recomendacion_medica):
    if recomendacion_medica == "Bajar de peso":
        print("Es necesario bajar de peso según la recomendación médica.")
    elif recomendacion_medica == "Aumentar de peso":
        print("Es necesario aumentar de peso según la recomendación médica.")
    elif recomendacion_medica == "Conservar peso":
        print("Es necesario conservar el peso actual según la recomendación médica.")
    else:
        print("Recomendación médica no reconocida. Por favor, consulte con su médico.")

def main():
    ha_consultado_medico = input("¿Ha consultado con un profesional de la salud sobre su peso? (Sí/No): ").lower()
    
    if ha_consultado_medico == "sí" or ha_consultado_medico == "si":
        recomendacion_medica = input("Por favor, ingrese la recomendación médica específica: ")
        determinar_peso_segun_recomendacion_medica(recomendacion_medica)
    elif ha_consultado_medico == "no":
        print("Se recomienda consultar con un profesional de la salud para determinar las acciones adecuadas.")
    else:
        print("Entrada no válida. Por favor, responda 'Sí' o 'No'.")

if __name__ == "__main__":
    main()
