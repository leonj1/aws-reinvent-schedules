# Makefile for AWS Re:Invent 2024 Catalog project

# Variables
DOCKER_COMPOSE = docker-compose

# Phony targets
.PHONY: build up down clean logs

# Default target
all: build up

# Build the Docker images
build:
	$(DOCKER_COMPOSE) build

# Start the containers
up:
	$(DOCKER_COMPOSE) up -d

# Stop the containers
down:
	$(DOCKER_COMPOSE) down

# Remove containers, networks, and volumes
clean:
	$(DOCKER_COMPOSE) down -v

# View logs
logs:
	$(DOCKER_COMPOSE) logs -f

# Build and start the containers
start: build up

# Stop and remove the containers
stop: down

# Rebuild and restart the containers
restart: down build up
