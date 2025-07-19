# Swap Nodes Algorithm - Solución Detallada

## Problema
Dado un árbol binario y una serie de consultas `k`, necesitamos:
1. Para cada consulta `k`, intercambiar los subárboles izquierdo y derecho de todos los nodos cuya profundidad sea múltiplo de `k`
2. Después de cada intercambio, retornar el recorrido in-order del árbol

## Análisis del Problema

### Ejemplo Visual
```
                                    Profundidad
        1               1            [1]
       / \             / \
      2   3     ->    3   2          [2]
       \   \           \   \
        4   5           5   4        [3]
```
- Recorrido in-order original: `2 4 1 3 5`
- Después del intercambio en profundidad 1: `3 5 1 2 4`

## Pensamiento de la Solución Step-by-Step

### Paso 1: Análisis de Complejidad
- **Problema principal**: Necesitamos saber qué nodos están en cada profundidad
- **Desafío**: Por cada consulta, debemos intercambiar múltiples niveles y hacer recorrido in-order
- **Optimización clave**: Pre-calcular las profundidades para evitar recálculos

### Paso 2: Elección de Estructuras de Datos

#### 2.1 `defaultdict(list)` para `nodes_by_depth`

```python
nodes_by_depth = defaultdict(list)
# Ejemplo: {1: [1], 2: [2, 3], 3: [4, 5]}
```
**¿Por qué esta estructura?**
- Agrupa nodos por profundidad automáticamente
- Acceso O(1) a todos los nodos de una profundidad específica
- `defaultdict` evita verificar si la clave existe

#### 2.2 Array `depth` para mapear nodo → profundidad

```python
depth = [0] * (n + 1)  # depth[0] unused
```
**¿Por qué un array?**
- Acceso O(1) a la profundidad de cualquier nodo
- Los nodos están numerados 1 a n, perfecto para indexación directa

#### 2.3 `deque` para BFS

```python
from collections import deque
q = deque([(1, 1)])  # (node, depth)
```
**¿Por qué deque?**
- BFS requiere FIFO (First In, First Out)
- `deque.popleft()` es O(1), mientras que `list.pop(0)` es O(n)

### Paso 3: Algoritmo Detallado

#### Fase 1: Pre-procesamiento con BFS

```python
# Calculamos profundidades de una sola vez
q = deque([(1, 1)])  # (nodo, profundidad)
while q:
    node, d = q.popleft()
    if node == -1:  # nodo inexistente
        continue
    depth[node] = d
    nodes_by_depth[d].append(node)

    left, right = indexes[node - 1]
    q.append((left, d + 1))
    q.append((right, d + 1))
```

**¿Por qué BFS y no DFS?**
- BFS garantiza que procesamos nodos nivel por nivel
- Más natural para agrupar por profundidad
- Evita recursión (problemas de stack overflow en árboles profundos)

#### Fase 2: Recorrido In-Order Iterativo

```python
def inorder_iterative() -> list[int]:
    result = []
    stack = []
    node = 1  # comenzar en la raíz

    while stack or node != -1:
        # Ir lo más a la izquierda posible
        while node != -1:
            stack.append(node)
            node = indexes[node - 1][0]  # hijo izquierdo

        # Visitar nodo
        node = stack.pop()
        result.append(node)

        # Ir al subárbol derecho
        node = indexes[node - 1][1]

    return result
```

**¿Por qué iterativo y no recursivo?**
- Evita stack overflow en árboles muy profundos
- Más control sobre el flujo de ejecución
- Misma complejidad temporal O(n) pero más seguro

#### Fase 3: Procesamiento de Consultas

```python
for k in queries:
    # Intercambiar niveles que son múltiplos de k
    d = k
    while nodes_by_depth.get(d):  # solo si ese nivel existe
        for node in nodes_by_depth[d]:
            left, right = indexes[node - 1]
            indexes[node - 1][0], indexes[node - 1][1] = right, left
        d += k

    # Guardar recorrido in-order actual
    final_result.append(inorder_iterative())
```

**Optimización clave**: `nodes_by_depth.get(d)`
- Evita KeyError si la profundidad no existe
- Más eficiente que verificar `if d in nodes_by_depth`

## Análisis Completo del Código

### Imports y Setup

```python
import os
from collections import deque, defaultdict
```
- `deque`: Para BFS eficiente
- `defaultdict`: Para agrupación automática por profundidad

### Función Principal: Estructura General

```python
def swapNodes(indexes, queries):
    n = len(indexes)

    # 1) Pre-procesamiento
    depth = [0] * (n + 1)
    nodes_by_depth = defaultdict(list)

    # 2) BFS para calcular profundidades
    # ...

    # 3) Función helper para in-order
    def inorder_iterative():
        # ...

    # 4) Procesar cada consulta
    final_result = []
    for k in queries:
        # ...

    return final_result
```

### Detalles de Implementación

#### Manejo de Nodos Inexistentes
```python
if node == -1:
    continue
```
- En el input, -1 representa un hijo inexistente
- Simplemente lo saltamos en BFS

#### Indexación Cuidadosa
```python
indexes[node - 1]  # Los nodos están numerados 1-n, pero arrays son 0-indexados
```

#### Intercambio Elegante
```python
indexes[node - 1][0], indexes[node - 1][1] = right, left
```
- Intercambio simultáneo usando tuple unpacking de Python
- Más legible que usar variable temporal

## Complejidad del Algoritmo

### Complejidad Temporal
- **Pre-procesamiento**: O(n) - BFS una sola vez
- **Por consulta**:
  - Intercambio: O(nodos en niveles múltiplos de k) = O(n) en el peor caso
  - In-order: O(n)
- **Total**: O(n + q×n) donde q = número de consultas

### Complejidad Espacial
- `nodes_by_depth`: O(n)
- `depth`: O(n)
- Stack para in-order: O(altura del árbol) = O(n) en el peor caso
- **Total**: O(n)

## Ventajas de esta Aproximación

1. **Pre-cálculo inteligente**: Las profundidades se calculan una sola vez
2. **Acceso eficiente**: Estructura de datos optimizada para consultas por profundidad
3. **Robustez**: Manejo seguro de nodos inexistentes (-1)
4. **Escalabilidad**: Funciona eficientemente para árboles grandes
5. **Claridad**: Código bien estructurado y fácil de entender

## Casos Edge Considerados

1. **Nodos inexistentes**: Manejados con verificación `node == -1`
2. **Profundidades inexistentes**: `nodes_by_depth.get(d)` retorna None
3. **Árbol vacío**: El algoritmo maneja correctamente árboles de un solo nodo
4. **Múltiples consultas**: Estado del árbol se mantiene entre consultas
5. **Niveles sin nodos**: El while loop termina automáticamente

## Alternativas Consideradas y Por Qué No Se Usaron

### ❌ Recursión para In-Order
```python
def inorder_recursive(node):
    if node == -1:
        return []
    left = indexes[node-1][0]
    right = indexes[node-1][1]
    return inorder_recursive(left) + [node] + inorder_recursive(right)
```
**Problemas:**
- Stack overflow en árboles profundos
- Overhead de llamadas recursivas
- Menos control sobre la ejecución

### ❌ Recalcular Profundidades en Cada Consulta
```python
def get_depth(node, current_depth=1):
    # Recalcular desde raíz cada vez
```
**Problemas:**
- O(n) por cada consulta = O(q×n) solo para profundidades
- Trabajo redundante
- Complejidad total sería O(q×n×n)

### ❌ Usar Dict Normal en Lugar de defaultdict
```python
nodes_by_depth = {}
if d not in nodes_by_depth:
    nodes_by_depth[d] = []
nodes_by_depth[d].append(node)
```
**Problemas:**
- Más verboso
- Verificaciones adicionales
- Menos Pythónico

## Conclusión

Esta solución es óptima para el problema planteado, balanceando eficiencia temporal y espacial mientras mantiene la claridad del código. La clave está en el pre-procesamiento inteligente y la elección correcta de estructuras de datos para cada subtarea específica.

### Lecciones Aprendidas
1. **Pre-cálculo**: Cuando tienes múltiples consultas, vale la pena invertir tiempo inicial en pre-procesar
2. **Estructura de datos**: La elección correcta puede simplificar enormemente el algoritmo
3. **Iterativo vs Recursivo**: Para problemas con árboles potencialmente profundos, lo iterativo es más seguro
4. **Python idioms**: Usar características del lenguaje como `defaultdict` y tuple unpacking hace el código más elegante
