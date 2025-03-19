import random
import sys
puntaje = 0
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */",
     "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]


# El usuario deberá contestar 3 preguntas


questions_to_ask = random.choices(
    list(zip(questions, answers, correct_answers_index)), k=3)

# Se muestra la pregunta y las respuestas posibles
for que, opt, ans in questions_to_ask:
    print(que)

    for i, answer in enumerate(opt):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if not user_answer.isdigit() or not (1 <= int(user_answer) <= 4):
            print("Respuesta no válida.")
            sys.exit(1)
        user_answer = int(user_answer) - 1

        # Se verifica si la respuesta es correcta
        if user_answer == ans:
            puntaje += 1
            print("¡Correcto!")
            break
        else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            if puntaje > 0:
                puntaje -= 0.5
            print("Incorrecto. La respuesta correcta es:")
            print(opt[ans])
    # Se imprime un blanco al final de la pregunta
    print()
print("el puntaje fue de: ", puntaje)
