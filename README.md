## Crear el Entorno

```sh
python -m venv venv
```

## Activar el Entorno 

```sh
.\venv\Scripts\activate
```

## Instalar dependencias

```sh
pip install -r .\requirements.txt
```

## Comando de Ejecución

#### Todos los test

```sh
python -m pytest -v
```

#### Para un test en especifico invoca al marcador (marker) que especifico en su archivo pytest.ini por ejemplo cart: Cart feature tests

```sh
python -m pytest -m cart -v
```