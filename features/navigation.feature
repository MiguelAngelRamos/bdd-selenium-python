# language: en
@navigation
Feature: Navegación en la Página principal
  Como usuario autenticado
  Quiero navegar por el sitio
  Para acceder a diferentes secciones

  Background:
    Given el usuario ha iniciado sesión con usuario "emilys" y contraseña "emilyspass"
    And el usuario está en la página principal

  Scenario: Verificar elementos de navegación
    Then debería ver el menú de navegación
    And debería ver el enlace "Productos"
    And debería ver el enlace "Carrito"

  Scenario: Navegar a Productos
    When el usuario hace clic en el enlace "Productos"
    Then el usuario debería estar en la página "products"

  Scenario: Navegar al Carrito
    When el usuario hace clic en el enlace "Carrito"
    Then el usuario debería estar en la página "cart"

  # Scenario: Eliminar uno de dos productos en el carrito
  #   Given el usuario ha agregado 2 productos al carrito
  #   When el usuario elimina uno de los productos haciendo clic en "Quitar"
  #   Then debería quedar 1 producto en la lista
  #   And el total debería actualizarse correctamente

  Scenario: Cerrar sesión
    When el usuario hace clic en cerrar sesión
    Then el localStorage debería estar vacio
    And el usuario debería estar en la página "index"