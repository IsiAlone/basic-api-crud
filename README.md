# DEPLOY BASIC API CRUD

La API realiza peticiones HTTP. El código principal de este proyecto está en `app.py`.

La idea principal de la API es **obtener una lista de post que iremos actualizando mediante la peticion @POST, @PUT Y @DELETE desplegada en Heroku**.

La API se ha creado con [FastAPI](https://fastapi.tiangolo.com/) y me he servido de [Uvicorn](https://www.uvicorn.org/) para lanzar el servidor local.


### Ejecución

Para lanzar el proyecto se debe lanzar a través de [Uvicorn](https://www.uvicorn.org/), con el comando '`uvicorn app:app`', que nos creará un servidor local, con puerto por defecto 8000; iremos a la dirección `localhost:8000/docs` donde se podrán realizar las peticiones HTTP que hemos creado. En caso de haberlo desplegado en Heroku tendremos que comprobar la URL proporcionado por [Heroku](https://dashboard.heroku.com/apps).

![Alt text](/images/basic-api-crud-1.png)

![Alt text](/images/basic-api-crud-2.png)

![Alt text](/images/basic-api-crud-3.png)

