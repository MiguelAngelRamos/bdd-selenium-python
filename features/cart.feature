# language: en

@cart
Feature: Carrito de Compras
  Como usuario autenticado
  Quiero gestionar mi carrito
  Para revisar productos antes de comprar

  Background:
    Given el usuario ha iniciado sesión con usuario "emilys" y contraseña "emilyspass"

  Scenario: Ver carrito vacío
    Given el carrito está vacío
    When el usuario navega a la página del carrito
    Then debería ver el mensaje "Tu carrito está vacío"

  Scenario: Ver productos en el carrito
    Given el usuario ha agregado un producto al carrito
    When el usuario navega a la página del carrito
    Then debería ver el producto en la lista
    And debería ver el total calculado

  Scenario: Eliminar producto del carrito
    Given el usuario tiene un producto en el carrito
    When el usuario hace clic en "Quitar"
    Then el producto debería eliminarse del carrito

  Scenario: Proceder al checkout
    Given el usuario tiene productos en el carrito
    When el usuario navega a la página del carrito
    And el usuario hace clic en "Continuar"
    Then el usuario debería estar en la página "checkout"
