## Project variables
PROJECT_NAME ?= superrecord
TARGET_MAX_CHAR_NUM=10
## File names
DOCKER_DEV_COMPOSE_FILE := docker/dev/docker-compose.yml

.PHONY: help

## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo '${YELLOW} make ${RESET} ${GREEN}<target>'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		message = match(lastLine, /^## (.*)/); \
		if (message) { \
			command = substr($$1, 0, index($$1, ":")-1); \
			message = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} %s\n", command, message; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''

## Build the project docker images
build:
	@ ${INFO} "Building required docker images"
	@ docker-compose -f $(DOCKER_DEV_COMPOSE_FILE) build
	@ ${INFO} "Build Completed successfully"
	@ echo " "

## Start local development server in the background
start:build
	@ ${INFO} "Starting local development server"
	@ docker-compose -f $(DOCKER_DEV_COMPOSE_FILE) up -d

## Stop the running local development server
stop:
	@ ${INFO} "Stoping local development server"
	@ docker-compose -f $(DOCKER_DEV_COMPOSE_FILE) down

## Run project test cases
test:build
	@ ${INFO} "Running tests in docker container"
	@ docker-compose -f $(DOCKER_DEV_COMPOSE_FILE) run -d database
	@ docker-compose -f $(DOCKER_DEV_COMPOSE_FILE) run app python manage.py test

## Run  and report coverage results
report:
	@ ${INFO} "Generating and uploading test coverage"
	@ cd src/
	@ pipenv install --skip-lock
	@ . $(pipenv --venv)/bin/activate
	@ coverage run manage.py test
	@ coverage xml
	@ python-codacy-coverage -r coverage.xml

## Remove all images
clean:
	${INFO} "Cleaning your local environment"
	${INFO} "Note: All ephemeral volumes will be destroyed"
	@ docker-compose -f $(DOCKER_DEV_COMPOSE_FILE) down -v
	@ docker images -q -f label=application=$(PROJECT_NAME) | xargs -I ARGS docker rmi -f ARGS
	${INFO} "Removing dangling images"
	@ docker system prune
	${INFO} "Clean complete"

## COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
NC := "\e[0m"
RESET  := $(shell tput -Txterm sgr0)

## Shell Functions
INFO := @bash -c 'printf $(YELLOW); echo "===> $$1"; printf $(NC)' SOME_VALUE
SUCCESS := @bash -c 'printf $(GREEN); echo "===> $$1"; printf $(NC)' SOME_VALUE

