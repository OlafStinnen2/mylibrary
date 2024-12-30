### The first docker commands

```
docker run -it ubuntu
```

Here's a breakdown of what each part of this command does:

docker run: This is the command used to create and start a new container from a specified image.
-it: These are two flags combined:
-i (interactive): Keeps the STDIN (standard input) open even if not attached.
-t (tty): Allocates a pseudo-TTY (terminal), which allows you to interact with the container via the terminal.
ubuntu: This is the name of the Docker image you want to run. In this case, it is the official Ubuntu image from Docker Hub.
When you run this command, Docker will:

Pull the ubuntu image from Docker Hub if it is not already available locally.
Create a new container from the ubuntu image.
Start the container and attach your terminal to it, allowing you to interact with the container's shell.
This command is useful for starting a container where you need to interact with the shell, for example, to run commands or scripts manually.

Once you've started the linux ubuntu container, a shell opens up with "root@...". You could update the linux version of the container with linux command ```apt-get-update```.
If you want to install a programm with name "tree" for example you need the linux command ```apt-get install tree```

You could do the same to run python:

```
docker run -it python
```

Above installs the latest python version from docker hub.
If you need a different version, e.g. 3.8 then do the following:

```
docker run -it python:3.8
```

## Docker Run

```docker run```always creates a NEW container and it does the three steps:

1) ```docker [image] pull```. Downlaods an image in general from docker hub
2) ```docker [container] create``` Creates a container based on downloaded image
3) ```docker [container] start``` starts the container

However, ```docker start -it [CONTAINER ID]```starts an existing container depending on container id

### Installation of Programs into Existing Container

To install a program into an existing container using `docker exec`, follow these steps:

1. Use `docker exec` to run a command inside the running container. For example, to install `tree` on an Ubuntu container:

    ```
    docker exec -it [CONTAINER ID] apt-get update
    docker exec -it [CONTAINER ID] apt-get install -y tree
    ```

2. Verify the installation by running the installed program:

    ```
    docker exec -it [CONTAINER ID] tree --version
    ```

Replace `[CONTAINER ID]` with the actual ID of your container. This process allows you to execute commands inside the container without needing to start an interactive shell session.

Above will not work for a python container. To install a package like pandas into an existing Python container using `docker exec`, follow these steps:

1. Open an new bash terminal

2. Connect new bash terminal to the existing container with 
    ```
    root@container_id: /# docker exec -it container_id_or_name bash
    ```
3. Install pandas package into python container with
    ```
    root@container_id: /# pip install pandas
    ```
4. Go back to python shell:
    ```
    >>> import pandas as pd
    ```

5. Verify the installation by running a Python command to check the installed library:
    ```
    >>> print(pd.__version__)"
    ```

### Troubleshooting

If you enter this command

```
docker run -it ubuntu
```

and feedback is this
docker: Cannot connect to the Docker daemon at unix:///Users/olafstinnen/.docker/run/docker.sock. Is the docker daemon running?

Then you need to start docker desktop via Launchpad or via terminal command ```docker desktop start```

### Infos from Container
