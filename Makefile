# Makefile for AWS Re:Invent 2024 Catalog project

# Variables
DOCKER_COMPOSE = docker-compose

# Phony targets
.PHONY: build run

# Default target
.DEFAULT_GOAL := build

# Build the Docker images
build:
	$(DOCKER_COMPOSE) build

# Run the containers
run:
	$(DOCKER_COMPOSE) up -d
