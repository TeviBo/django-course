# Copia de Seguridad de una Base de datos Django

## Comando para crear Copia de Seguridad con Django

    ```sh
    python3 manage.py dumpdata --exclude auth.permission > django_store_data.json 
    ```

## Comando para Volcar la copia de seguridad en un base de datos existente con Django

    ```sh
    python3 manage.py loaddata django_store_data.json
    ```

Con estos 2 simples comandos puede crear una copia y re-establecer datos de una base de datos.
