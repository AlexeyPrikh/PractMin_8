.PHONY: clean build run stop

IMAGE_NAME = my_flask_app
CONTAINER_NAME = flask_app

build: 
	docker build -t $(IMAGE_NAME) .

start: 
	docker run -p 8080:8080 --name $(CONTAINER_NAME) $(IMAGE_NAME)


shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh

stop: 
	docker stop $(CONTAINER_NAME)

clean: 
	docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \
	docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi

healthcheck:
	docker inspect $(CONTAINER_NAME)