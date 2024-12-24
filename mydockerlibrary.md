### The first docker commeands

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

### Troubleshooting
If you enter this command
```
docker run -it ubuntu
```
and feedback is this
docker: Cannot connect to the Docker daemon at unix:///Users/olafstinnen/.docker/run/docker.sock. Is the docker daemon running?

Then you need to start docker desktop via Launchpad or via terminal command ```docker desktop start```