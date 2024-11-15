from sympy import symbols, Or, And, Not
from sympy.logic.inference import satisfiable

# Definición de símbolos con sympy
mustard, plum, scarlet = symbols("ColMustard ProfPlum MsScarlet")
characters = [mustard, plum, scarlet]

ballroom, kitchen, library = symbols("ballroom kitchen library")
rooms = [ballroom, kitchen, library]

knife, revolver, wrench = symbols("knife revolver wrench")
weapons = [knife, revolver, wrench]

symbols_list = characters + rooms + weapons

# Función para verificar el conocimiento
def check_knowledge(knowledge):
    for symbol in symbols_list:
        if satisfiable(knowledge & symbol):
            print(f"\033[92m{symbol}: YES\033[0m")  # Verde
        elif satisfiable(knowledge & Not(symbol)):
            print(f"{symbol}: MAYBE")

# Definición inicial del conocimiento
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

# Agregar conocimiento adicional (equivalente a 'add' en tu código original)
knowledge = And(
    knowledge,
    Not(mustard),
    Not(kitchen),
    Not(revolver),
    Or(Not(scarlet), Not(library), Not(wrench)),
    Not(plum),
    Not(ballroom)
)

# Imprimir la fórmula completa del conocimiento
print("Conocimiento lógico:", knowledge)

# Verificar el conocimiento
check_knowledge(knowledge)
