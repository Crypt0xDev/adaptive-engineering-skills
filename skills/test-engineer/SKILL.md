---
name: test-engineer
description: Define que probar, con que tipo de test y cuanto, segun el riesgo y la etapa del proyecto. Usar al escribir tests, al decidir la estrategia de pruebas, ante bugs que se repiten o antes de un refactor.
---

# 🧪 Test Engineer

## Propósito
Decidir qué probar y con qué tipo de test según el riesgo real, para que los tests protejan lo importante sin frenar el desarrollo.

## Cuándo se usa
- Al escribir código nuevo con lógica de negocio, cálculos, permisos o manejo de dinero/datos.
- Al definir la estrategia de pruebas de un proyecto (qué capas, qué herramientas, qué se corre en CI).
- Ante un bug corregido: el test que lo reproduce va primero, antes del fix.
- Antes de un refactor: asegurar que el comportamiento actual está cubierto.
- Ante tests lentos, frágiles o que fallan de forma intermitente.

## Cuándo NO se usa
- Prototipos o spikes descartables (pero si se integran, se testean).
- Para perseguir un porcentaje de cobertura: la cobertura es un indicador, no un objetivo.
- Código trivial sin lógica (getters, wiring, configuración declarativa): testearlo es ruido.
- Para revisar la calidad general del código (eso es `code-reviewer`) o medir rendimiento (eso es `performance-engineer`).

## Entradas esperadas
- El código o la feature a cubrir y qué pasa si falla (impacto real).
- Etapa del proyecto (MVP, producción, legado sin tests).
- Stack y herramientas de test que el proyecto ya usa — respetarlas antes de proponer otras.

## Salida esperada
Tests concretos listos para correr, o un plan corto: qué se prueba, con qué tipo de test, qué se deja sin probar y por qué.

## Reglas internas

### Qué probar (por riesgo, de mayor a menor)
1. Lógica de negocio, cálculos y reglas de permisos.
2. Bordes: entradas vacías, nulas, límites, errores esperados.
3. Integraciones críticas (BD, APIs externas) en sus puntos de contacto, no en cada función.
4. Flujos de usuario clave de punta a punta: pocos, solo los que generan ingresos o pérdidas si fallan.

### Cómo escribirlos
- **Comportamiento, no implementación**: el test no se rompe si se refactoriza sin cambiar el resultado.
- **Un motivo de fallo por test**, con nombre que describe el caso (`rechaza_pedido_sin_stock`).
- **Deterministas**: sin depender de la hora, el orden, la red ni datos compartidos entre tests.
- **Mocks solo en los bordes** (red, reloj, servicios externos); no mockear el propio código bajo prueba.
- **Rápidos**: la suite unitaria corre en segundos; lo lento va a una etapa separada del CI.

### Proporcional a la etapa
- **MVP:** tests de la lógica crítica y del flujo principal. Nada más.
- **Producción:** + tests de regresión por cada bug y de integración en los puntos críticos.
- **Legado sin tests:** primero tests de caracterización sobre lo que se va a tocar; no intentar cubrir todo.

### Nunca
- Borrar o desactivar un test que falla para que pase el CI sin entender por qué falla.
- Escribir tests que solo verifican que se llamó a un mock, sin verificar el resultado.

## Ejemplos de uso

**Ejemplo 1:** Función que calcula descuentos por cupón en un e-commerce.
→ Riesgo alto (dinero). Tests unitarios: cupón válido, vencido, monto mínimo no alcanzado, descuento mayor que el total. Sin tests de UI para esto.
→ Resultado: 4 tests rápidos que cubren las reglas, sin mocks.

**Ejemplo 2:** "Agrega tests a todo el proyecto, tiene 0% de cobertura".
→ No se cubre todo. Se identifican los 2-3 módulos con más cambios y bugs, se escriben tests de caracterización ahí y se agrega el job de tests al CI.
→ Resultado: protección donde duele, en horas en lugar de semanas.
