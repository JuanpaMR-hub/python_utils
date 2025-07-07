import os
import csv
os.system('cls')

seccion = "151-3"
asignatura = "TI3032"
path = os.path.abspath(f"archivos/{asignatura}/{seccion}")

def cambiar_nombre_carpetas(path):
    for entrega in os.listdir(path):
        nombre_alumno = ''.join(entrega.split('_')[0])
        try:
            os.rename(os.path.join(path,entrega),os.path.join(path,nombre_alumno))
        except Exception as e:
            print(e)
    return

def listar_alumnos(path):
    alumnos = []
    for alumno in os.listdir(path):
        alumnos.append(alumno)
    return alumnos


def exportar_alumnos_csv(asignatura:str,seccion:str,path:str) -> bool:
    alumnos = listar_alumnos(path)
    if "_" in alumnos[0]:
        cambiar_nombre_carpetas(path)
        alumnos = listar_alumnos(path)
    
    directorio_creado = False
    while directorio_creado == False:
        if os.path.exists(f"archivos/csv/{asignatura}"):
            print("existe csv")
            directorio_creado = True
        else:
            os.mkdir(f"archivos/csv/{asignatura}")
    
    with open (f"archivos/csv/{asignatura}/{seccion}.csv", 'w',encoding="utf-8", newline='') as f:
        w = csv.writer(f)
        w.writerow(['Alumno'])
        for alumno in alumnos:
            w.writerow([alumno])
            
            
exportar_alumnos_csv(asignatura,seccion,path)
        
        
    