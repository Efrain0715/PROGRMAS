# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:18:25 2024

@author: Efrain Jimenez M
"""
from collections import deque

# Grafo representando síntomas (nodos) conectados con posibles diagnósticos, con un grado de severidad
grafo = {
    "dolor en el pecho": ["infarto", "ansiedad", "reflujo",],
    "dificultad para respirar": ["insuficiencia respiratoria", "asma", "ansiedad"],
    "desmayo": ["infarto", "hemorragia cerebral", "deshidratación"],
    "fiebre alta": ["sepsis", "infección", "gripe"],
    "dolor abdominal agudo": ["apendicitis", "pancreatitis", "gastritis"],
    "náuseas": ["gripe", "intoxicación alimentaria", "apendicitis"],
    "infarto": ["emergencia"],
    "asma": ["grave", "leve"],
    "sepsis": ["emergencia"],
    "hemorragia cerebral": ["emergencia"],
    "pancreatitis": ["grave"],
    "apendicitis": ["grave"],
    "gripe": ["leve"],
    "ansiedad": ["leve"],
    "reflujo": ["leve"],
    "deshidratación": ["leve"],
    "infección": ["leve", "grave"],
    "intoxicación alimentaria": ["leve"]
}

# Entrada del usuario (síntomas)
sintoma_inicial = input("Introduce el síntoma inicial: ")
posible_diagnostico = input("Introduce el diagnóstico esperado: ")

# Función para determinar la gravedad basada en el grafo
def bfs_gravedad(grafo, sintoma_inicial, posible_diagnostico):
    visitados = set()
    padres = {}
    cola = deque([sintoma_inicial])

    while cola:
        nodo = cola.popleft()
        
        if nodo not in visitados:
            visitados.add(nodo)
            vecinos = grafo.get(nodo, [])
            for vecino in vecinos:
                if vecino not in visitados:
                    padres[vecino] = nodo
                    cola.append(vecino)

    if posible_diagnostico not in padres:
        return "No se encontró un diagnóstico correspondiente."

    # Recopilamos el camino desde el síntoma inicial hasta el diagnóstico
    camino = []
    nodo_actual = posible_diagnostico
    while nodo_actual != sintoma_inicial:
        padre = padres[nodo_actual]
        camino.append((padre, nodo_actual))
        nodo_actual = padre

    camino.reverse()
    return camino

# Ejecutar la búsqueda para determinar la ruta
camino = bfs_gravedad(grafo, sintoma_inicial, posible_diagnostico)

# Determinación de la gravedad
if isinstance(camino, str):
    print(camino)
else:
    print(f"Posibles conexiones entre síntomas y enfermedades desde {sintoma_inicial} hasta {posible_diagnostico}:")
    for eslabon in camino:
        print(f"{eslabon[0]} -> {eslabon[1]}")

    # Verificar la gravedad del diagnóstico final
    gravedad = grafo.get(posible_diagnostico, ["Desconocido"])
    
    if "emergencia" in gravedad:
        print(f"El diagnóstico {posible_diagnostico} es una REANIMACIÓN de nivel ROJO requiere atencion inmediata.")
    elif "grave" in gravedad:
        print(f"El diagnóstico {posible_diagnostico} es una EMERGENCIA de nivel NARANJA atencion en menos de 30 min.")
    elif "leve" in gravedad:
        print(f"El diagnóstico {posible_diagnostico} es una URGENCIA de nivel AMARILLA atención en menos de 2 horas.")
    else:
        print(f"No se pudo determinar la gravedad del diagnóstico {posible_diagnostico}.")

