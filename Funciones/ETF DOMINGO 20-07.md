# Descripción de las opciones del programa `practicadomingoetf.py`

Este documento describe las funciones y funcionalidades que componen el menú principal del programa contenido en el archivo `practicadomingoetf.py`. Cada opción del menú corresponde a una función que realiza una tarea específica relacionada con la gestión de inventario de notebooks.

---

## Opción 1: Stock por marca  
**Enunciado:**  
Crear una función que reciba como parámetro el nombre de una marca y calcule el total de unidades en stock para todos los modelos que pertenecen a esa marca. Si no se encuentra la marca, mostrar un mensaje claro indicando que no hay registros de esa marca.

---

## Opción 2: Búsqueda por rango de precio  
**Enunciado:**  
Desarrollar una función que permita al usuario ingresar un rango de precios (valor mínimo y máximo) y muestre todos los modelos cuyo precio esté dentro de ese rango y que tengan stock disponible. Si no existen modelos que cumplan el criterio, informar al usuario.

---

## Opción 3: Actualizar precio  
**Enunciado:**  
Implementar una función que reciba un modelo y un nuevo precio para actualizar el valor del producto en el inventario. Si el modelo no existe, notificar al usuario con un mensaje claro. Permitir realizar múltiples actualizaciones consecutivas hasta que el usuario decida salir.

---

## Opción 4: Salir  
**Enunciado:**  
Finalizar la ejecución del programa mostrando un mensaje de despedida o cierre.

---

## Opción 5: Mostrar modelos sin stock  
**Enunciado:**  
Crear una función que recorra los modelos en stock y muestre aquellos que tengan cantidad igual a cero, indicando la marca y el modelo. Si todos los productos tienen stock disponible, mostrar un mensaje confirmándolo.

---

## Opción 6: Verificar datos sincronizados entre productos y stock  
**Enunciado:**  
Desarrollar una función que compare las claves (modelos) existentes en los diccionarios `productos` y `stock`. Informar qué modelos están en `stock` pero no en `productos` y viceversa, para detectar inconsistencias en la base de datos. Si todo está sincronizado, mostrar un mensaje de confirmación.

---

## Opción 7: Listar modelos con bajo stock  
**Enunciado:**  
Crear una función que reciba un umbral numérico y muestre todos los modelos cuyo stock sea menor o igual a ese valor, mostrando también la marca, el modelo y la cantidad disponible. Si no hay modelos que cumplan con el criterio, informar al usuario.

---

## Opción 8: Buscar notebooks por procesador  
**Enunciado:**  
Desarrollar una función que permita ingresar una palabra o fragmento de texto relacionado con el procesador (por ejemplo, "i5") y muestre todos los modelos que contengan ese texto en la descripción de su procesador. Si no se encuentran coincidencias, mostrar un mensaje claro.

---

## Opción 9: Buscar notebooks por tipo de disco  
**Enunciado:**  
Implementar una función que permita ingresar un tipo de disco (por ejemplo, "SSD" o "DD") y liste todos los modelos que utilicen ese tipo de disco. En caso de no encontrar modelos que cumplan, informar al usuario.

---

## Opción 10: Agregar un nuevo modelo al inventario  
**Enunciado:**  
Crear una función que solicite al usuario todos los datos técnicos, precio y cantidad de stock de un nuevo modelo. Validar que el modelo no exista previamente y que los datos ingresados para precio y cantidad sean numéricos. Luego, agregar el nuevo modelo a los diccionarios correspondientes e informar el éxito de la operación.

---

## Opción 11: Mostrar el modelo más caro y más barato disponible  
**Enunciado:**  
Implementar una función que recorra todos los modelos con stock disponible para identificar cuál es el modelo con el precio más alto y cuál el más bajo. Mostrar ambos modelos con su marca, precio y cantidad en stock. En caso de que no haya stock disponible, informar al usuario.

---

## Opción 12: Eliminar modelo  
**Enunciado:**  
Desarrollar una función que permita eliminar un modelo ingresado por el usuario, removiéndolo tanto del diccionario `productos` como del diccionario `stock`. Si el modelo no existe, mostrar un mensaje claro indicando que no se encontró.

---

## Opción 13: Mostrar estadísticas del inventario  
**Enunciado:**  
Crear una función que calcule y muestre el total de notebooks en stock, el promedio ponderado del precio por unidad y la cantidad de modelos que usan tarjeta de video integrada. Si no hay stock, mostrar un mensaje que lo indique.

---

## Opción 14: Listar modelos de una marca con tipo de disco específico  
**Enunciado:**  
Crear una función que reciba una marca y un tipo de disco (por ejemplo, lenovo, SSD) y muestre todos los modelos que coincidan con ambas condiciones. Si no se encuentran coincidencias, mostrar un mensaje claro al usuario.

---

## Opción 15: Actualizar stock de un modelo  
**Enunciado:**  
Implementar una función que permita actualizar la cantidad en stock de un modelo existente, validando que la cantidad ingresada sea un número positivo. Si el modelo no existe, informar al usuario con un mensaje claro.

---

Este documento es un acompañamiento para el archivo [`practicadomingoetf.py`.py`](practicadomingoetf.py)., donde se implementan todas estas funcionalidades.

