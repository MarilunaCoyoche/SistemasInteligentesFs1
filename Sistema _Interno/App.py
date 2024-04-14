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
    imc = float(input("Por favor, ingrese el Índice de Masa Corporal (IMC) de la persona: "))
    
    if imc < 18.5:
        pregunta_2 = input("¿La persona tiene alguna condición médica que afecte su peso? (Sí/No): ").lower()
        if pregunta_2 == "sí" or pregunta_2 == "si":
            recomendacion_medica = input("Por favor, ingrese la recomendación médica específica: ")
            determinar_peso_segun_recomendacion_medica(recomendacion_medica)
        else:
            print("Es necesario aumentar de peso según el IMC.")
    elif 18.5 <= imc <= 24.9:
        pregunta_5 = input("¿La persona está satisfecha con su imagen corporal y nivel de energía? (Sí/No): ").lower()
        if pregunta_5 == "no":
            pregunta_4 = input("¿La persona ha consultado con un profesional de la salud sobre su peso? (Sí/No): ").lower()
            if pregunta_4 == "sí" or pregunta_4 == "si":
                recomendacion_medica = input("Por favor, ingrese la recomendación médica específica: ")
                determinar_peso_segun_recomendacion_medica(recomendacion_medica)
            else:
                print("Se recomienda consultar con un profesional de la salud para determinar las acciones adecuadas.")
        else:
            print("Conservar el peso actual.")
    elif imc > 24.9:
        pregunta_6 = input("¿La persona ha probado cambios en su dieta o estilo de vida para bajar de peso? (Sí/No): ").lower()
        if pregunta_6 == "no":
            pregunta_7 = input("¿La persona está dispuesta a realizar cambios en su dieta y estilo de vida para aumentar su peso? (Sí/No): ").lower()
            if pregunta_7 == "sí" or pregunta_7 == "si":
                print("Es necesario aumentar de peso según el IMC.")
            else:
                print("Conservar el peso actual.")
        else:
            print("Continuar con los cambios en la dieta y el estilo de vida o buscar ayuda profesional si no han sido efectivos.")

if __name__ == "__main__":
    main()
