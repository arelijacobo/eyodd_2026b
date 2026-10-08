'''
NOTAS:
1. Identificar el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2. Es ver cuanto crece el numero 
opetaciones en mi algoritmo conforme
crece el tamaño de la entrada.
Agrego las bigO indicadas
Teniendo en cuneta la Cota superior
O(n) + 0(4 = O(n+4) = O(n) 

'''

# Creando una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack']
student_list_02 = ['Mike','Saul','Walter','Jessy']

# Verificando presencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student: #0(n)
            print("✔️ Estudiante encontrado") #0(1)
            return 
    # Si no encuntro al estudiante
    print("✖️ Estudiante no encontrado") #0(1)
    return None

# Probando algoritmo
check_student("Walter",student_list_02)