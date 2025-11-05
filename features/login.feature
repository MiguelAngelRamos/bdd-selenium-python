# language: en
Feature: Inicio de sesión
  Como usuario registrado
  Quiero iniciar sesión en el sitio
  Para acceder a mi cuenta

  Background:
    Given el usuario está en la página de login

  Scenario: Inicio exitoso con credenciales válidas
    When ingresa usuario "emilys"
    And ingresa contraseña "emilyspass"
    And hace clic en el botón de inicio sesión
    Then debería ver la página principal
  
  Scenario: Inicio fallido con credenciales inválidas
    When
  