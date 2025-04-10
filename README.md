Portal: 

https://<codespaces generated>-8082.app.github.dev/ 

Geonetwork: 

https://<codespaces generated>-8080.app.github.dev/srv/eng/catalog.search#/home

Keycloak: 

https://<codespaces generated>-8085.app.github.dev/

Create the network before running the docker-compose for the first time in a new codespaces: 

docker network create web

Best to bring it down first and then build again
docker-compose down
docker-compose up -d --force-recreate

Note that docker-compose down -v will also remove the volumes, careful! 

