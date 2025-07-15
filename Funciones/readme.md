# ♟️ Torneo de Ajedrez Interestelar

## 📝 Enunciado del Programa

Se debe implementar un sistema en Python para administrar las inscripciones al **Torneo de Ajedrez Interestelar**.  
El menú principal debe permitir realizar las siguientes acciones:

---

## 📋 Menú del sistema

1. **Inscribir participante**  
   - Solicita el nombre, la categoría (I, J o A), el código de registro y el ELO del jugador.
   - Reglas de validación:
     - El nombre no puede repetirse.
     - La categoría debe ser:
       - `I` para Infantil
       - `J` para Juvenil
       - `A` para Adulto
     - El código debe tener:
       - Mínimo 8 caracteres
       - Al menos una letra mayúscula
       - Al menos un número
       - Sin espacios
     - El ELO debe ser un número entre 800 y 2800.

2. **Consultar inscripción**  
   - Permite buscar un jugador por su nombre (ignora mayúsculas/minúsculas).
   - Si lo encuentra, muestra todos sus datos.
   - Si no lo encuentra, indica que no está inscrito.

3. **Cancelar inscripción**  
   - Elimina a un participante de la lista por su nombre.
   - Si no existe, muestra un mensaje correspondiente.

4. **Ver estadísticas**  
   - Muestra:
     - Total de inscritos
     - Cantidad por categoría (Infantil, Juvenil, Adulto)
     - Promedio del ranking ELO de los jugadores inscritos

5. **Exportar inscritos**  
   - Guarda todos los inscritos en un archivo llamado `inscritos.txt`, con los datos separados por punto y coma.

6. **Salir del sistema**  
   - Termina la ejecución del programa mostrando un mensaje de despedida.

---

## 💻 Código fuente

El código se encuentra en el archivo [`torneo_ajedrez_practica_etf.py`](torneo_ajedrez_practica_etf.py).
