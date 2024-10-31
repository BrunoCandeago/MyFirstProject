Clases de Animales en Python 🐾

Este proyecto implementa un modelo básico de clases en Python para representar distintos tipos de animales y su comportamiento. Utiliza conceptos de Programación Orientada a Objetos (POO), como la herencia, el polimorfismo y las clases abstractas, para estructurar diferentes tipos de animales y sus comportamientos específicos.

Descripción

El objetivo de este proyecto es crear una jerarquía de clases que represente distintos tipos de animales (Animal, AnimalAcuatico, Leon, Jirafa, Delfin) y sus métodos. La clase base Animal define características y comportamientos básicos, mientras que las subclases representan tipos específicos de animales con sus propias acciones y comportamientos.

Clases Principales
Animal (Clase abstracta):

Clase base abstracta que define los atributos comunes (nombre, tipo, alimentacion, habitat) y un método abstracto comer.
Métodos:
descripcion(): Muestra una descripción del animal.
caminar(): Muestra un mensaje indicando que el animal camina.
comer(): Método abstracto que debe implementarse en cada subclase.
AnimalAcuatico (Clase abstracta):

Subclase de Animal que añade el método nadar() para los animales acuáticos.
Sobrescribe el método caminar() para hacer que los animales acuáticos "naden" en lugar de "caminar".
Subclases específicas:

Leon: Representa un león, implementa el método comer() para mostrar que come carne y tiene el método adicional rugido().
Jirafa: Representa una jirafa, implementa el método comer() para mostrar que come plantas.
Delfin: Representa un delfín, implementa el método comer() para mostrar que come peces y hereda nadar() de AnimalAcuatico.
