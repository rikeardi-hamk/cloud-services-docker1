#!/bin/bash

# Ask the user for the containers to create
echo "Which containers do you want to create?"
echo "1. Server + Client"
echo "2. Server"
echo "3. Client"
read -p "Enter your choice [1-3]: " choice

# Ask the user for the server IP
read -p "Enter the server host (default server): " server_host


# Ask the user for the server port
read -p "Enter the server port (default 8000): " server_port

# Ask the user for the network
read -p "Enter the CIDR network (default 192.168.99.0/24): " network
network=${network:-'192.168.99.0/24'}
server_host=${server_host:-'server'}
server_port=${server_port:-'8000'}

# Export the variables to env file
echo "DOCKER_NETWORK=$network" > .env
echo "DOCKER_SERVER_HOST=$server_host" >> .env
echo "DOCKER_SERVER_PORT=$server_port" >> .env

# Create the containers
case $choice in
    1)
        echo "Creating Server + Client..."
        docker-compose up -d
        ;;
    2)
        echo "Creating Server..."
        docker-compose up -d server
        ;;
    3)
        echo "Creating Client..."
        docker-compose up -d client
        ;;
    *)
        echo "Invalid choice"
        ;;
esac