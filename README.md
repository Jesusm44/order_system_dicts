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

.