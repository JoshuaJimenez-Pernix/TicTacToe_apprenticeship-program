"# ticTacToe_apprenticeship-program" 

### **Descripción General**

El aprendiz desarrollará el clásico juego de Tic-Tac-Toe en Ruby con una interfaz de línea de comandos, aplicando los conceptos aprendidos en los ejercicios previos. Además, el aprendiz gestionará el proyecto utilizando la metodología **Scrum** con la herramienta **Trello**, en la que el mentor actuará como el "cliente", proporcionando orientación y retroalimentación.

### **Descripción del Juego**

Tic-Tac-Toe es un juego de dos jugadores en el que cada jugador alterna turnos para marcar una celda en una cuadrícula de 3x3. El primer jugador utiliza el símbolo "X" y el segundo jugador utiliza el símbolo "O". El objetivo del juego es ser el primero en alinear tres de sus símbolos en una fila, columna o diagonal.

### **Requisitos del Proyecto**

### 1. **Lógica del Juego**

- Implementar la cuadrícula de 3x3 como un array bidimensional o una estructura de datos equivalente.
- Permitir que dos jugadores se turnen para ingresar su símbolo ("X" o "O") en una celda vacía.
- Comprobar después de cada turno si un jugador ha ganado, es decir, si ha conseguido alinear tres símbolos consecutivos en una fila, columna o diagonal.
- Manejar el caso de empate, es decir, cuando todas las celdas están ocupadas y ningún jugador ha ganado.

### 2. **Interfaz de Usuario en Consola**

- Mostrar el estado actual del tablero después de cada turno.
- Pedir a los jugadores que ingresen las coordenadas de la celda donde desean colocar su símbolo.
- Manejar entradas inválidas (por ejemplo, si un jugador elige una celda ya ocupada o ingresa coordenadas fuera del rango).
- Proporcionar mensajes claros sobre el estado del juego: quién ha ganado, si ha habido un empate, o si el juego continúa.

### 3. **Diseño Orientado a Objetos**

- Implementar una clase `Board` que gestione el estado del tablero, incluyendo la validación de movimientos y la verificación de condiciones de victoria o empate.
- Crear una clase `Player` para representar a los jugadores, manejando sus símbolos y turnos.
- Implementar una clase `Game` que coordine la interacción entre los jugadores y el tablero, controlando el flujo del juego y la lógica principal.

### 4. **Pruebas Unitarias**

- Escribir pruebas unitarias para las principales funcionalidades, como la validación de movimientos, la detección de un ganador, y la detección de empate.
- Utilizar una herramienta de pruebas como RSpec o Minitest para asegurar que cada parte del juego funcione correctamente.

### **Extras Opcionales**

- **Juego contra la computadora**: Implementar una opción para que un jugador pueda jugar contra la computadora. La computadora podría tomar decisiones aleatorias o aplicar una estrategia básica (como bloquear al oponente).
- **Historial de partidas**: Guardar el resultado de las partidas en un archivo, mostrando un historial con las victorias y empates.
- **Mejor de 3/5**: Añadir una opción para jugar varias rondas y determinar quién gana más partidas.

### **Manejo del Proyecto en GitHub**

- El aprendiz deberá utilizar **GitHub** para el control de versiones y mantener un historial de cambios claro y organizado.
- **Estructura de Branches**:
    - La rama principal será **main** o **master**.
    - Para cada funcionalidad o historia de usuario, el aprendiz debe crear una nueva rama siguiendo una convención de nombres consistente. Por ejemplo:
        - `feature/[ticket#]_add-move-validation`
        - `fix/[ticket#]_board-display-bug`
        - `refactor/[ticket#]_game-flow-optimization`
    - Cada nueva rama debe estar basada en la rama `main` y debe enfocarse en una sola tarea o funcionalidad.
- **Proceso de Pull Requests**:
    - Al completar una tarea, el aprendiz deberá hacer un **Pull Request** desde la rama correspondiente hacia la rama principal.
    - Las pull requests deben incluir una descripción clara de los cambios y cómo se relacionan con las historias de usuario.
    - El mentor revisará los pull requests como si fuera un código de revisión de un equipo real, proporcionando feedback si es necesario.

### **Gestión del Proyecto con Scrum**

- **Roles**:
    - El aprendiz asumirá los roles de **Scrum Master** y **Desarrollador**, gestionando todo el flujo del proyecto.
    - El mentor actuará como el **Product Owner** (cliente), revisando el progreso, proporcionando retroalimentación y definiendo prioridades.
- **Tablero de Trello**:
    - El aprendiz deberá crear un tablero en Trello con las siguientes columnas:
        1. **Backlog**: Lista de todas las historias de usuario que describen las características o tareas a realizar.
        2. **To Do**: Historias de usuario priorizadas que el aprendiz abordará en el sprint actual.
        3. **In Progress**: Tareas que el aprendiz está desarrollando en este momento.
        4. **Review**: Tareas completadas que deben ser revisadas por el mentor.
        5. **Done**: Tareas terminadas y aprobadas por el mentor.
- **Historias de Usuario**:
    - El aprendiz deberá escribir historias de usuario para cada funcionalidad del juego, por ejemplo:
        - "Como jugador, quiero poder ingresar las coordenadas para colocar mi símbolo en el tablero".
        - "Como jugador, quiero que se me notifique cuando he ganado, perdido o empatado".
        - "Como mentor, quiero ver un tablero visual del estado del juego después de cada turno".
    - Estas historias incluirán criterios de aceptación y estimaciones de tiempo.
- **Sprints**:
    - El aprendiz dividirá el trabajo en **sprints** de una semana.
    - Al inicio de cada sprint, hará una **planificación de sprint** con el mentor para determinar qué tareas abordar.
    - Al finalizar cada sprint, el aprendiz presentará los avances en una **revisión de sprint** al mentor para recibir feedback.
    - También realizará una **retrospectiva** para reflexionar sobre lo aprendido y mejorar en los siguientes sprints.

### **Desarrollo Técnico**

- **Requisitos del Juego**:
    - Implementar la lógica de Tic-Tac-Toe en Ruby con clases para el tablero (`Board`), los jugadores (`Player`), y la lógica del juego (`Game`).
    - Validar las entradas del jugador y gestionar el flujo del juego hasta que haya un ganador o un empate.
    - Mostrar el tablero de juego y mensajes claros sobre el estado actual del juego.
- **Extras Opcionales**:
    - Añadir funcionalidad de juego contra la computadora o implementar un historial de partidas.

### **Objetivos del Proyecto**

- **Técnicos**:
    - Desarrollar una aplicación de línea de comandos en Ruby, aplicando principios de programación orientada a objetos.
- **Gestión de Proyecto**:
    - Aprender a utilizar Scrum para gestionar el proyecto de manera autónoma.
    - Utilizar Trello como una herramienta visual para organizar tareas y realizar el seguimiento del progreso.
    - Utilizar Github como herramienta de manejos de código.
    - Recibir retroalimentación del mentor (cliente) y ajustar el trabajo según los comentarios recibidos.

Este proyecto permitirá al aprendiz combinar habilidades técnicas y de gestión de proyectos, preparándolo para escenarios en los que deba trabajar de manera independiente, organizando su tiempo y tareas de manera efectiva.