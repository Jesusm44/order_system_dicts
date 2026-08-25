Simple Order Management System (CLI)

---English

---Overview

This is a command-line application written in Python that simulates a basic order management system. It allows creating and managing users, products, and orders while maintaining data consistency through simple validation and control logic.

--- Features

* Create users with unique IDs
* Create products with price and stock
* Create orders linked to users and products
* Automatic stock update when an order is created
* Delete orders
* Prevent duplicate IDs using sets
* Basic input validation

--- Data Structures

---The system is built using core Python data structures:

* list: stores users, products, and orders
* dict: represents entities such as users, products, and orders
* set: ensures uniqueness of IDs

---System Flow

Validation → Processing → Decision → Persistence

---Limitations

* Supports only one product per order
* No data persistence (data is lost after execution ends)
* Stock is not restored when an order is deleted
* No modular structure (no functions or classes)

----Purpose

This project was developed to practice:

* Core data structures
* Control flow
* Input validation
* Basic system design

---------------------------------------------------------------

---Español

---Descripción

Este es un sistema por consola desarrollado en Python que simula un gestor básico de órdenes. Permite crear y administrar usuarios, productos y órdenes, manteniendo la consistencia de los datos mediante validaciones simples y control del flujo.

---Funcionalidades

* Crear usuarios con IDs únicos
* Crear productos con precio y stock
* Crear órdenes asociadas a usuarios y productos
* Actualización automática del stock al crear una orden
* Eliminar órdenes
* Evitar IDs duplicados usando sets
* Validación básica de datos

---Estructuras de Datos

El sistema está construido utilizando estructuras básicas de Python:

* list: almacena usuarios, productos y órdenes
* dict: representa entidades como usuario, producto y orden
* set: garantiza la unicidad de los IDs

---Flujo del Sistema

Validación → Procesamiento → Decisión → Persistencia

---Limitaciones

* Solo permite un producto por orden
* No hay persistencia de datos (se pierden al cerrar el programa)
* El stock no se restaura al eliminar una orden
* No está modularizado (no usa funciones ni clases)



---Este proyecto fue desarrollado para practicar:

* Estructuras de datos
* Control de flujo
* Validación de datos
* Diseño básico de sistemas

--------------------------------------
# order_system_dict refactored

## English

### Overview

`order_system_dict` is a command-line order management system developed in Python. The project manages users, products, and orders using dictionaries, lists, and sets stored in memory.

The project focuses on practicing function-based programming, data validation, control flow, data structures, and the refactoring of procedural logic into separate functions.

### Features

* Create users with unique IDs.
* Create products with price and stock.
* Create orders associated with existing users and products.
* Validate user, product, and order IDs.
* Check product stock before creating an order.
* Automatically update product stock when an order is created.
* Display stored orders.
* Delete orders.
* Use sets to prevent duplicate IDs.
* Keep all data in memory during execution.

### Data Structures

| Structure | Purpose                                                   |
| --------- | --------------------------------------------------------- |
| `list`    | Stores users, products, and orders.                       |
| `dict`    | Represents users, products, and orders.                   |
| `set`     | Stores IDs to prevent duplicates and validate references. |

### Main Functions

| Function           | Description                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `add_user()`       | Validates and creates a new user.                                                              |
| `create_product()` | Validates and creates a new product.                                                           |
| `create_order()`   | Validates the order, checks stock, calculates the total, updates stock, and creates the order. |
| `print_order()`    | Displays all stored orders.                                                                    |
| `delete_order()`   | Deletes an order using its ID.                                                                 |

### System Flow

The main order creation process follows this flow:

```text
Validate Order ID
       |
Validate User ID
       |
Validate Product ID
       |
Find Product
       |
Check Stock
       |
Calculate Total
       |
Update Stock
       |
Create Order
       |
Store Order
```

### Refactoring

The project is a refactored version of a procedural implementation.

The original implementation contained the main operations directly inside the application's control flow. The refactored version separates the main responsibilities into functions:

```text
User creation      -> add_user()
Product creation   -> create_product()
Order creation     -> create_order()
Order display      -> print_order()
Order deletion     -> delete_order()
```

This organization makes each operation easier to identify and reuse while maintaining the original in-memory approach.

### Requirements

* Python 3.10 or later.

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/order_system_dict.git
```

Enter the project directory:

```bash
cd order_system_dict
```

Run the application:

```bash
python refactored_system.py
```

### Limitations

* Data is lost when the program terminates.
* An order supports only one product.
* Deleting an order does not restore the product stock.
* Numeric input is not protected with exception handling.
* The project does not use a database.
* The project does not use classes or object-oriented programming.

### Future Improvements

* Add exception handling for user input.
* Add a dedicated menu function.
* Support multiple products per order.
* Restore stock when an order is deleted.
* Add persistent storage.
* Add automated tests.
* Separate the application into multiple modules.
* Introduce object-oriented programming.

### Purpose

This project was created to practice Python programming fundamentals, data structures, validation, function design, and the refactoring of procedural code into a function-based structure.

### License

This project was created for educational purposes.

---

# order_system_dict refactorizado

## Español

### Descripción

`order_system_dict` es un sistema de gestión de órdenes desarrollado en Python y ejecutado mediante línea de comandos. El proyecto administra usuarios, productos y órdenes utilizando diccionarios, listas y sets almacenados en memoria.

El proyecto está enfocado en practicar programación basada en funciones, validación de datos, control de flujo, estructuras de datos y refactorización de lógica procedural hacia funciones independientes.

### Características

* Crear usuarios con IDs únicos.
* Crear productos con precio y stock.
* Crear órdenes asociadas a usuarios y productos existentes.
* Validar IDs de usuarios, productos y órdenes.
* Comprobar el stock antes de crear una orden.
* Actualizar automáticamente el stock cuando se crea una orden.
* Mostrar las órdenes almacenadas.
* Eliminar órdenes.
* Utilizar sets para evitar IDs duplicados.
* Mantener todos los datos en memoria durante la ejecución.

### Estructuras de Datos

| Estructura | Propósito                                                  |
| ---------- | ---------------------------------------------------------- |
| `list`     | Almacena usuarios, productos y órdenes.                    |
| `dict`     | Representa usuarios, productos y órdenes.                  |
| `set`      | Almacena IDs para evitar duplicados y validar referencias. |

### Funciones Principales

| Función            | Descripción                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------ |
| `add_user()`       | Valida y crea un nuevo usuario.                                                            |
| `create_product()` | Valida y crea un nuevo producto.                                                           |
| `create_order()`   | Valida la orden, comprueba el stock, calcula el total, actualiza el stock y crea la orden. |
| `print_order()`    | Muestra todas las órdenes almacenadas.                                                     |
| `delete_order()`   | Elimina una orden utilizando su ID.                                                        |

### Flujo del Sistema

El proceso principal de creación de una orden sigue este flujo:

```text
Validar ID de la orden
        |
Validar ID del usuario
        |
Validar ID del producto
        |
Buscar producto
        |
Comprobar stock
        |
Calcular total
        |
Actualizar stock
        |
Crear orden
        |
Almacenar orden
```

### Refactorización

El proyecto es una versión refactorizada de una implementación procedural.

La implementación original contenía las operaciones principales directamente dentro del flujo de control de la aplicación. La versión refactorizada separa las responsabilidades principales mediante funciones:

```text
Creación de usuarios       -> add_user()
Creación de productos      -> create_product()
Creación de órdenes        -> create_order()
Visualización de órdenes   -> print_order()
Eliminación de órdenes     -> delete_order()
```

Esta organización permite identificar y reutilizar cada operación con mayor facilidad, manteniendo el enfoque original basado en almacenamiento en memoria.

### Requisitos

* Python 3.10 o superior.

### Instalación

Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/order_system_dict.git
```

Ingresa al directorio del proyecto:

```bash
cd order_system_dict
```

Ejecuta la aplicación:

```bash
python refactored_system.py
```

### Limitaciones

* Los datos se pierden cuando termina el programa.
* Una orden admite únicamente un producto.
* Eliminar una orden no restaura el stock del producto.
* Las entradas numéricas no están protegidas mediante manejo de excepciones.
* El proyecto no utiliza una base de datos.
* El proyecto no utiliza clases ni Programación Orientada a Objetos.

### Mejoras Futuras

* Agregar manejo de excepciones para las entradas del usuario.
* Crear una función específica para el menú.
* Permitir múltiples productos por orden.
* Restaurar el stock cuando se elimina una orden.
* Agregar almacenamiento persistente.
* Agregar pruebas automatizadas.
* Separar la aplicación en múltiples módulos.
* Introducir Programación Orientada a Objetos.

### Propósito

Este proyecto fue creado para practicar fundamentos de programación en Python, estructuras de datos, validación, diseño de funciones y refactorización de código procedural hacia una estructura basada en funciones.

### Licencia

Este proyecto fue creado con fines educativos.
