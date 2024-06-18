docker exec -it my-mongodb mongo -u cagri -p 3541 --authenticationDatabase admin

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-mongodb
