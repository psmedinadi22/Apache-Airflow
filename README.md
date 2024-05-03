# Apache-Airflow


Cuando exista el error zsh: command not found: pip
```
alias pip="python3 -m pip"
```

## Inicializar la base de datos de metadatos y servidor web

Para iniciar airflow ejecutar en una terminal
```
airflow db init
airflow webserver --port 8080
```

En otra terminal ajecutar:
```
airflow scheduler
```

Asegúrate de haber activado el entorno virtual airflow_env antes de intentar ejecutar el comando airflow scheduler. Puedes hacerlo ejecutando el siguiente comando en la segunda terminal
```
source airflow_env/bin/activate
```

Forma de crear un usuario en Apache Airflow:
```
airflow users create \
    --role Admin \
    --username psmedinadi \
    --email paula.medina@payu.com \
    --firstname paula \
    --lastname medina \
    --password constraseña
```
