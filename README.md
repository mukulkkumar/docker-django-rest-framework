# Docker Compose and Django

If you don't have docker compose installed. You can install it by using the following steps:-

1. Run this command to download the current stable release of Docker Compose:

    sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. Apply executable permissions to the binary:

    sudo chmod +x /usr/local/bin/docker-compose
    
3. Create a  symbolic link to /usr/bin

    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

4. Test the installation

    docker-compose --version

#### Now you can clone the repository

Execute the following commands in your cloned repository:-

1. docker-compose up - for starting the server

2. docker-compose down - for stopping the server

##### If you want to see the list of running containers, you can execute the following commands

1. docker ps
