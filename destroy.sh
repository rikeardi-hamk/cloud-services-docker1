#!/bin/bash

# Confirm with the user
read -p "Are you sure you want to destroy the containers? [y/N]: " confirm
confirm=${confirm:-'n'}

if [[ $confirm =~ ^[Yy]$ ]]
then
    # Destroy the containers
    docker-compose down
    echo "Containers destroyed"
else
    echo "Containers not destroyed"
fi