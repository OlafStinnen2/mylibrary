# Docker Command Library

## The First Docker Commands

```bash
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

Once you've started the linux ubuntu container, a shell opens up with "root@...". You could update the linux version of the container with linux command ```apt-get update```.
If you want to install a programm with name "tree" for example you need the linux command ```apt-get install tree```

You could do the same to run python:

```bash
docker run -it python
```

Above installs the latest python version from docker hub.
If you need a different version, e.g. 3.8 then do the following:

```bash
docker run -it python:3.8
```

## Docker Pull and Push

### Docker Pull

The `docker pull` command downloads an image from a Docker registry (like Docker Hub) to your local machine.

```bash
docker pull ubuntu:latest
docker pull python:3.9
```

You can also pull from specific registries:

```bash
docker pull ghcr.io/owner/image:tag
```

### Docker Push

The `docker push` command uploads an image to a Docker registry.

```bash
docker push myusername/my-image:latest
```

Before pushing, you need to:
1. Login to the registry: `docker login`
2. Tag your image appropriately: `docker tag my-image myusername/my-image:latest`

## Docker Login and Logout

### Docker Login

Authenticate to a Docker registry:

```bash
docker login
docker login registry.example.com
docker login -u username -p password
```

### Docker Logout

Log out from a Docker registry:

```bash
docker logout
docker logout registry.example.com
```

### Docker Search

Search for images on Docker Hub:

```bash
docker search ubuntu
docker search --filter stars=100 nginx
```

## Docker System Management

### Docker System Info

Display system-wide information about Docker:

```bash
docker system info
# or shorthand:
docker info
```

### Docker System Disk Usage

Show Docker disk usage including images, containers, and volumes:

```bash
docker system df
docker system df -v  # verbose output
```

### Docker System Prune

Remove all unused Docker objects (containers, networks, images, and optionally volumes):

```bash
docker system prune           # Remove stopped containers, unused networks, dangling images
docker system prune -a        # Also remove all unused images (not just dangling)
docker system prune -a --volumes  # Also remove unused volumes
docker system prune -f        # Force prune without confirmation
```

## Container Monitoring and Stats

### Docker Stats

Display live resource usage statistics for containers:

```bash
docker stats                    # Show stats for all running containers
docker stats [Container-ID]     # Show stats for specific container
docker stats --no-stream        # Display stats once without streaming
```

### Docker Top

Display running processes inside a container:

```bash
docker top [Container-ID]
docker top [Container-ID] aux   # With detailed process info
```

### Docker Port

List port mappings for a container:

```bash
docker port [Container-ID]
docker port [Container-ID] 80   # Show mapping for specific port
```

## Container Pause and Unpause

### Docker Pause

Pause all processes in a container (freezes the container state):

```bash
docker pause [Container-ID]
```

### Docker Unpause

Resume a paused container:

```bash
docker unpause [Container-ID]
```

The difference between `docker pause` and `docker stop`:
- `pause`: Freezes all processes using cgroups, very fast, state remains in memory
- `stop`: Gracefully stops the container, sends SIGTERM then SIGKILL

## Docker Image Export and Import

### Docker Save

Save an image to a tar archive (includes all layers and metadata):

```bash
docker save -o my-image.tar my-image:latest
docker save my-image:latest | gzip > my-image.tar.gz  # Compressed
```

### Docker Load

Load an image from a tar archive:

```bash
docker load -i my-image.tar
docker load < my-image.tar
```

### Docker Export

Export a container's filesystem as a tar archive (flattened, no history):

```bash
docker export [Container-ID] > container-backup.tar
docker export -o container-backup.tar [Container-ID]
```

### Docker Import

Import a container filesystem tar archive as an image:

```bash
docker import container-backup.tar my-new-image:latest
cat container-backup.tar | docker import - my-new-image:latest
```

**Key Difference:**
- `save`/`load`: Preserves image layers, history, and metadata (use for images)
- `export`/`import`: Creates a flat filesystem snapshot without history (use for containers)

## Docker Commit

Create a new image from a container's changes:

```bash
docker commit [Container-ID] my-new-image:v1
docker commit -m "Added nginx" -a "Author Name" [Container-ID] my-image:v2
```

This is useful for capturing manual changes made to a container, but using Dockerfiles is the recommended approach for reproducibility.

## Docker Image Tag

The `docker image tag` command is used to create a new tag for an existing Docker image. This command does not alter the image itself but allows you to refer to the same image by a different name or tag within a Docker registry or on your local system.

The general syntax for the command is:

- `SOURCE_IMAGE[:TAG]` refers to the existing image and optional specific tag you want to add a new tag to. If the tag isn't specified, Docker assumes `latest`.
- `TARGET_IMAGE[:TAG]` refers to the new name and tag you want to assign to the image.

This is particularly useful for versioning images or when you need to push them to a different repository.

Example:

```bash
docker image tag my-image:1.0 my-image:latest
```

## Docker Image Remove

The `docker image remove` (or `docker rmi`) command is used to delete one or more Docker images from your local Docker environment. This helps in managing disk space and keeping your local environment clean.

The general syntax for the command is:

```bash
docker image remove [OPTIONS] IMAGE [IMAGE...]
```

or its shorthand:

```bash
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

Here, `IMAGE` can be the image ID, image tag, or the image name with a specific tag.

Some important points about `docker image remove`:

- An image cannot be removed if there are any containers using it, unless you force the removal.
- If you want to remove all unused images, you can combine it with commands like `docker image prune`.

Example of removing an image:

```bash
docker image remove my-image:latest
```

This will remove the image tagged `my-image:latest` from your system if no containers are currently using it. You can use the `-f` or `--force` option to forcibly remove an image being used by stopped containers.

## Docker Run vs. Docker Start and Docker Create

The `docker run`, `docker create`, and `docker start` commands are used to manage the lifecycle of Docker containers, but they serve different purposes in that process.

# `docker run`

- `docker run` is the most commonly used command for running containers.
- It combines the functions of `docker create` and `docker start`.
- When you run `docker run`, Docker does the following:
  1. **Creates** a new container from the specified image.
  2. **Starts** the container.
  3. **Attaches** to the container's output (unless `-d` or `--detach` is specified to run the container in the background).
- It is equivalent to running `docker create` followed by `docker start`.
- Example:

```bash
docker run ubuntu:latest
```

## `docker create`

- `docker create` is used to create a new container without starting it.
- This command is useful if you want to set up a container’s configuration before starting it, such as setting environment variables or network settings.
- It prepares the container and returns the container ID without actually starting it.
- Example:

```bash
docker create --name my_container ubuntu:latest
```

## `docker start`

- `docker start` is used to start an existing, stopped container.
- If you use `docker create` to prepare a container, you'll use `docker start` to start it whenever needed.
- It only starts containers and does not create new instances.
- It does not attach to the container’s output by default, which means it runs the container in the background (to attach, use `docker start -i`).
- Example:

```bash
docker start my_container
```

**Differences:**

- `docker run` combines creation and starting of a new container and is a one-step command to both create and start with output attached to it
- `docker create` only creates the container, allowing for delayed starting or further configuration beforehand.
- `docker start` only works on existing containers that have been created, making it suitable for restarting purposes.

# Run a new container

```bash
docker run ubuntu:latest
```

# Run a new container but keep it running in the background (-d flag for detached)

```bash
docker run -d ubuntu:latest
```

This is similar to a combination of `docker create`& `docker start`

# Create a container without starting it

```bash
docker create --name my_container ubuntu:latest
```

# Start the previously created container

```bash
docker start my_container
```

## Docker Inspect, Docker History, Docker Logs

Above commands are utilities for obtaining detailed information about Docker images and containers. Each serves a unique purpose in providing insight into Docker objects.

## `docker inspect`

- `docker inspect` is used to return detailed information about Docker containers, images, volumes, or networks.
- It provides comprehensive JSON output with all the configurations and metadata of the specified object.
- Commonly used to troubleshoot or understand the configurations such as environment variables, mounts, network settings, etc.
- You can filter specific data using the `--format` option.
- Example:

```bash
docker inspect my_container
```

## `docker history`

- `docker history` displays the history of an image, showing the layers, and the creation history.
- It lists all layers that make up an image with details like command, size, and timestamp for each layer.
- Useful for understanding how an image was built and what commands were used to create each layer.
- Example:

```bash
docker history my_container
```

## `docker logs``

This command retrieves the logs from a running or stopped container. It shows the standard output and standard error streams from the container's main process. For example, `docker logs <container_id>` will display the logs output by the application running in the specified container.

```bash
docker logs my_container
```

## Docker Rename and the flag --Name

The `docker rename` command and the `--name` flag are both used to manage container naming but in different contexts.

## `docker rename`

- The `docker rename` command is used to change the name of an existing Docker container.
- This is useful if the original name assigned to the container is not descriptive or was given a generic name but you later wish to rename it for clarity.
- The syntax for renaming a container is:

- Example: To rename a container named `my-old-container` to `my-new-container`, you would run:

```bash
docker rename my-old-container my-new-container
  ```

## `--name` flag

- The `--name` flag is used during the container creation process (e.g., with `docker run` or `docker create`) to assign a specific name to a container.
- By default, Docker assigns a random and unique name to containers unless specified.
- Using `--name`, you can specify a human-readable and easily recognizable name for your container upon creation.
- Example: To run a container with a specific name, you could use:

```bash
docker run --name my-container ubuntu:latest
```

**Differences:**

- The `docker rename` command changes the name of an already existing container.
- The `--name` flag sets the name of a container at the time of its creation.

**Rename an existing container**

```bash
docker rename my-old-container my-new-container
```

**Run a new container with a specific name**

```bash
docker run --name my-container ubuntu:latest
```

### Installation of Programs into Existing Container

To install a program into an existing container using `docker exec`, follow these steps:

1. Use `docker exec` to run a command inside the running container. For example, to install `tree` on an Ubuntu container:

    ```bash
    docker exec -it [CONTAINER ID] apt-get update
    docker exec -it [CONTAINER ID] apt-get install -y tree
    ```

2. Verify the installation by running the installed program:

    ```bash
    docker exec -it [CONTAINER ID] tree --version
    ```

Replace `[CONTAINER ID]` with the actual ID of your container. This process allows you to execute commands inside the container without needing to start an interactive shell session.

Above will not work for a python container. To install a package like pandas into an existing Python container using `docker exec`, follow these steps:

1. Open an new bash terminal

2. Connect new bash terminal to the existing container with

    ```bash
    root@container_id: docker exec -it container_id_or_name bash
    ```

3. Install pandas package into python container with

    ```bash
    root@container_id: pip install pandas
    ```

4. Go back to python shell:

    ```python
    >>>import pandas as pd
    ```

5. Verify the installation by running a Python command to check the installed library:

    ```python
    >>> print(pd.__version__)
    ```

### Ports freigeben, Container im Hintergrund laufen lassen

Standardmäßig wird ein Container nicht neu gestartet.
Es gibt aber eine **restart policy**

- ```on-failur[:max-retries]```: Startet den Container "may-retries"-mal neu, wenn es einen Fehler gibt
- ```always```: Startet den Container immer neu. Außer wir haben ihn gestoppt. Dann wird erst beim nächsten Docker Daemon erneut gestartet
- ```unless-stopped```: Startet den Container immer neu (und wenn wir ihn stoppen bleibt er gestoppt)

Beispiele:
Wir setzen die Restart Policy so: (Der Container läuft im Backround Modus ohne Terminal (-d) und wird dann automatisch neu gestartet)

```bash
docker run -d --restart unless-stopped[Image-Name]
```

Die Restart Policy kann dann so aktualisiert werden

```bash
docker update --restart always [Container-ID / Name]
```

oder so:

```bash
docker update --restart onfailure:5 [Container-ID / Name]
```

## Portweiterleitung

Beim erstellen des Containers die Portweiterleitung spezifizieren, da ja der Start eines Containers auch automatisch durchgeführt werden kann.

```bash
docker container create -p Host-Port:Container Port Image-Name
```

### Datemnagement in Docker Containern

## Dateien in und aus einen Container kopieren

Entweder einen neuen Docker container starten/erstellen mit:

```bash
docker run ubuntu -t
```

oder einen bestehenden Container starten mit:

```bash
docker start [container_id]
docker exec -it [container_id] /bin/bash
```

Dann in einer neuen Shell in diesen Container wechseln und in diesem Container dann ein neues Verzeichnis "Folder" erstellen

```bash
mkdir Folder
```

und dann in der urpsprünglichen Shell mit dem Befehl z.B. die Text Datei file.txt im Verzeichnis "/Users/olafstinnen/Projects/mylibrary/"

```bash
docker cp /Users/olafstinnen/Projects/mylibrary/file.txt [container_id]:/Folder
```

hineinkopieren.

Wechsel man dann wieder zurück in die Shell für den den Container findent man dann die Dater über "cd Folder" und dann mit "ls" wieder.

## Das Verlinken von Host-Verzeichniss mit einem Container

Das Verlinken bzw. das Verküpfen einer Verzeichnisstruktur eines Containers mit Daten, die außerhalb vom Container liegen. Diese Daten, die außerhalb vom Container liegen sind persistent.
Sie werden als nicht gelöscht wenn wir den Container löschen. Im wesentlichen gibt es zwei Arten von mounts:
"bind" und "volume".

**Bind Mounts**

Bind mounts allow you to mount a file or directory from the host machine into the container. This means that changes made to the files in the container are reflected on the host and vice versa. Bind mounts are useful when you need to share data between the host and the container.

Example:

```bash
docker run -it \
  --name my_container \
  --mount type=bind,source=/path/on/host,target=/path/in/container \
  my_image
  ```

In this example:

- `type=bind` specifies that this is a bind mount.
- `source=/path/on/host` is the path on the host machine.
- `target=/path/in/container` is the path inside the container where the host path will be mounted.

### Volumes

Volumes are managed by Docker and are stored in a part of the host filesystem which is managed by Docker (`/var/lib/docker/volumes/` on Linux).
Volumes are useful for persisting data beyond the lifecycle of a container and for sharing data between multiple containers.
It is not possible to rename a volume. You need to create a new volume first and then copy the contents from the to be deleted volume into it.

For example by using databases stored in volumes.
With

```bash
docker volume create [Name]
```

you create a new volme.

To inspect a volume:

```bash
docker volume inspect [Name]
```

To delete a volume:

```bash
docker volume rm [Name]
```

To delete all volumes not connected to a container:

```bash
docker volume prune
```

If you want to know which volume is connected to a container then you need copy the volume id and:

```bash
docker container ls -a --filter volume=[Volume_Name]
```

Above lists all containers (Ls -a) and filter the container for the specified volume.

If you want to delete a volume you need to delete the container first:

```bash
docker container rm [Container_ID] && docker volume rm [Volume_Name]
```

#### Example

```bash
docker run -it \
  --name my_container \
  --mount type=volume,source=my_volume,target=/path/in/container \
  my_image
```

In this example:

- `type=volume` specifies that this is a volume mount.
- `source=my_volume` is the name of the volume.
- `target=/path/in/container` is the path inside the container where the volume will be mounted.

### Key Differences

1. **Location**:
   - **Bind Mounts**: Use any location on the host filesystem.
   - **Volumes**: Managed by Docker and stored in Docker's storage area.

2. **Use Case**:
   - **Bind Mounts**: Ideal for sharing data between the host and container, especially during development.
   - **Volumes**: Ideal for persisting data and sharing data between multiple containers.

3. **Management**:
   - **Bind Mounts**: Managed by the host system.
   - **Volumes**: Managed by Docker, which provides better isolation and management.

### Example Code for Mount

```bash
# Bind Mount Example
docker run -it \
  --name my_bind_container \
  --mount type=bind,source=/path/on/host,target=/path/in/container \
  my_image
```

With "pwd" you get the source path e.g. "/Users/olafstinnen/Projects/mylibrary"
and should in destination "Projects" in container and my_image is Ubuntu

```bash
docker run -it \
  --name Olafs_Container \
  --mount type=bind,source=/Users/olafstinnen/Projects/mylibrary,target=/projects \
  ubuntu
```

# Volume Mount Example

With

```bash
docker volume create volume_name
```

you create a volume on your local machine. And with ```bash docker volume rm volume_name``` you remove it.

With

```bash
docker run --name="mycontainer" -v myvolume:/project -it ubuntu
```

you create a new container that links the volume myvolume to project folder on mycontainer.

If you store a file in this project folder on container (e.g. touch help.txt) then you can make it available to a second container via

```bash
docker run --name="mynextcontainer" -v myvolume:/project -it ubuntu
```

**but** if you provide instead of volume name "myvolume" a path then then "-v" command will be interpreted as "bind mount" and you link the folder that the path points to the container

```bash
docker run --name="mynextcontainer" -v $(pwd):/projeckt -it ubuntu
```

# Udpating data in docker world #

To update a database version in docker world is done be creating a new container with the new database version
and then linking this new container and the new database version with the existing volume.
Once done you delete the old container with the old database version.

# Netzwerke in Docker #

## Grundlagen ##

*Zweck:* Docker Netzwerk ermöglichen die Kommunikation zwischen Containern, dem Host-System und externen Netzwerken

*Standard-Netzwerke:* Docker erstellt automatisch drei Netzwerke bzw drei Netzwerktypen:

- bridge: Standardnetzwerk für Container (isolierte Kommunikation auf demselben Host). Dieses Netzwerk wird automatisch einem neuen Docker Container zugeordnet. Bei Bridge-Netzwerken handelt es sich um private Subnetzwerke, deren IP immer mit 192 beginnt

- host: Container teilen sich das Netzwerk des Host-Systems (keine Isolation)

- none: Keine Netzwerkverbindung (Container ist komplett isoliert)

## Benutzerdefinierte Netzwerke ##

- Vorteile: Bessere Kontrolle, DNS-Auflösung zwischen Containern (über Container-Namen) und Isolation

- Beispiel:

```bash
docker network create mein-netzwerk
```

## Wichtige Befehle ##

- Netzwerke erstellen:

```bash
docker network create mein-netzwerk
```

- Netzwerkfunktionalität eines Containers ausschalten:

```bash
docker run --network none --name mein-container ubuntu
```

- Netzwerke auflisten:

```bash
docker network ls
```

- Details anzeigen:

```bash
docker network inspect netzerk-name
```

- Container mit Netzwerk verbinden:

```bash
docker network connect netzwer-name container-name
```

- Container löschen

```bash
docker network rm netzerk-name
```

Herausfinden welche Container in Netzwer mein-netzwerk laufen:

```bash
docker network inspect -f "{{.Containers}}" mein-netzwerk
```

# Dockerfiles: Develop own images

Dockerfiles allow us to write a configuration of a new image into a file called **Dockerfile**. The file is then used to build an image with the command **docker build**. The output is an image according to our description in the Dockerfile.

Each line of the dockerfile contains a command used to build the image. The syntax is [COMMAND][Parameter][^1]
[^1]: Parameter refers to the arguments passed to the command. COMMANDS are written in capital letters to differentiate them from parameter. "#" is used at the beginning to start a commentary. A "Dockerfile" has no file extension like ".md" for example. The standard name is always **Dockerfile**.

**Best Practice** is to have the dockerfile in an empty folder. This folder should contain the dockerfile only. Because if you build the dockerfile then image e has access to all files in your folder.

Each command in the dockerfile builds a new layer in the imagem and at the very end the image id is generated.

The first commmand in your dockerfile is always **FROM [Image]:[tag]**

The next commmand **RUN** updates the base image with the installation of additional packages

- Alpine: **RUN apk update && apk add [Package]**
- Ubuntu/Debia: **RUN apt-get update && apt-get install -y [Package]**
- Each RUN command line adds a new layer to the image

The command **COPY** copies local data from the project folder into the image. **ADD** is similar to **COPY** but with different capabilities. **ADD** allows to unpack archives like gzip, tar, bzip2, xz. Each COPY or ADD command adds a new line to the image.

The command **CMD ["Program / Datei", "Parameter 1", "Parameter 2"]** specifies which command or program should be executed after the image is build.

The command **ENTRYPOINT** is similar to **CMD** but with some differencies:

The **ENTRYPOINT** instruction in a Dockerfile specifies a command that will always be executed when the container starts. Unlike **CMD**, which can be overridden by providing a command at the end of `docker run`, **ENTRYPOINT** ensures that the specified command is always executed, making it useful for setting up containers that should always run a specific application.

## Key Points

- **ENTRYPOINT** is used to define a container's main executable.
- It ensures that the specified command is always executed.
- You can still pass additional arguments to the **ENTRYPOINT** command when running the container.
- You can pass this arguments with **CMD** in the dockerfile and overwrite this argument later when running the containiner




A Dockerfile typically contains a series of instructions, such as:

- **FROM**: Specifies the base image to use.
- **RUN**: Executes commands in the container.
- **COPY** or **ADD**: Copies files from the host to the container.
- **CMD** or **ENTRYPOINT**: Specifies the command to run when the container starts.
- **EXPOSE**: Defines the port on which the container will listen.
- **ENV**: Sets environment variables.
- **WORKDIR**: Sets the working directory inside the container and is a replacement for **RUN cd[Path]**

Example Dockerfile:

```Dockerfile
# Use the official Ubuntu base image
FROM ubuntu:latest

# Update and install tree
RUN apt-get update && apt-get install -y tree

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run tree command when the container launches
CMD ["tree"]
```

To build an image from this Dockerfile that is named "my-ubuntu-image", use the following command:

```bash
docker build -t my-ubuntu-image .
```

This command will create an image named `my-ubuntu-image` based on the instructions in the Dockerfile.

## Advanced Dockerfile Instructions

### ARG - Build-time Variables

The `ARG` instruction defines variables that users can pass at build-time to the builder with the `docker build` command using the `--build-arg` flag.

```Dockerfile
# Define build argument with default value
ARG PYTHON_VERSION=3.9
ARG APP_HOME=/app

# Use the argument
FROM python:${PYTHON_VERSION}
WORKDIR ${APP_HOME}
```

Build with custom arguments:

```bash
docker build --build-arg PYTHON_VERSION=3.11 -t my-app .
```

**Note:** `ARG` values are NOT available after the image is built, only during build-time. Use `ENV` for runtime variables.

### LABEL - Add Metadata

The `LABEL` instruction adds metadata to an image as key-value pairs:

```Dockerfile
FROM ubuntu:latest

LABEL maintainer="name@example.com"
LABEL version="1.0"
LABEL description="This is a custom Docker image"
LABEL org.opencontainers.image.authors="Your Name"
```

View labels:

```bash
docker inspect --format='{{json .Config.Labels}}' [Image-ID]
```

### USER - Set User

The `USER` instruction sets the user (and optionally group) to use when running the image:

```Dockerfile
FROM ubuntu:latest

# Create a non-root user
RUN useradd -m -u 1000 appuser

# Switch to non-root user
USER appuser

# All subsequent commands run as this user
WORKDIR /home/appuser
CMD ["whoami"]
```

**Security Best Practice:** Always run containers as non-root users when possible.

### VOLUME - Create Mount Points

The `VOLUME` instruction creates a mount point and marks it as holding externally mounted volumes:

```Dockerfile
FROM ubuntu:latest

# Create volume mount points
VOLUME /data
VOLUME ["/var/log", "/var/db"]

CMD ["bash"]
```

When you run this container, Docker automatically creates anonymous volumes for these paths.

### HEALTHCHECK - Container Health Monitoring

The `HEALTHCHECK` instruction tells Docker how to test if a container is still working:

```Dockerfile
FROM nginx:latest

# Check if nginx is responding every 30 seconds
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

Options:
- `--interval=DURATION` (default: 30s) - Time between checks
- `--timeout=DURATION` (default: 30s) - Max time for check to complete
- `--start-period=DURATION` (default: 0s) - Initialization time before starting checks
- `--retries=N` (default: 3) - Consecutive failures needed to mark unhealthy

Check health status:

```bash
docker ps  # Shows health status in STATUS column
docker inspect --format='{{.State.Health.Status}}' [Container-ID]
```

### ONBUILD - Trigger Instructions

The `ONBUILD` instruction adds a trigger instruction to be executed later when the image is used as a base for another build:

```Dockerfile
FROM node:14
WORKDIR /app

# These will execute when someone uses this image as base
ONBUILD COPY package*.json ./
ONBUILD RUN npm install
ONBUILD COPY . .
```

### .dockerignore File

Similar to `.gitignore`, the `.dockerignore` file excludes files and directories from the build context:

Create a `.dockerignore` file in the same directory as your Dockerfile:

```
# Ignore git files
.git
.gitignore

# Ignore documentation
*.md
docs/

# Ignore dependencies
node_modules/
__pycache__/
*.pyc

# Ignore logs and temp files
*.log
tmp/
.DS_Store

# Ignore secrets
.env
*.key
*.pem
```

Benefits:
- Faster builds (smaller context)
- Improved security (exclude sensitive files)
- Smaller images (if using COPY . .)

## Multi-Stage Builds

Multi-stage builds allow you to use multiple `FROM` statements in your Dockerfile. Each `FROM` instruction can use a different base, and each begins a new stage of the build. This is extremely useful for:

1. **Reducing final image size** - Keep build tools out of production images
2. **Separating build and runtime dependencies**
3. **Creating cleaner, more secure production images**

### Example 1: Go Application

```Dockerfile
# Stage 1: Build stage
FROM golang:1.20 AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o myapp

# Stage 2: Production stage
FROM alpine:latest

# Install certificates for HTTPS
RUN apk --no-cache add ca-certificates

WORKDIR /root/
# Copy only the compiled binary from builder stage
COPY --from=builder /app/myapp .

EXPOSE 8080
CMD ["./myapp"]
```

Result: Final image is ~10MB instead of 800MB+

### Example 2: Node.js Application

```Dockerfile
# Stage 1: Dependencies and build
FROM node:18 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Stage 2: Production runtime
FROM node:18-alpine

WORKDIR /app

# Copy only necessary files
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

# Run as non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Example 3: Python Application

```Dockerfile
# Stage 1: Build dependencies
FROM python:3.11 AS builder

WORKDIR /app
COPY requirements.txt .

# Install dependencies to a specific directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "app.py"]
```

### Example 4: Using Specific Stage for Testing

```Dockerfile
# Base stage
FROM node:18 AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Development stage
FROM base AS development
COPY . .
CMD ["npm", "run", "dev"]

# Test stage
FROM base AS test
COPY . .
RUN npm run test
RUN npm run lint

# Production build stage
FROM base AS builder
COPY . .
RUN npm run build

# Production runtime stage
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

Build specific stages:

```bash
# Build and run development
docker build --target development -t myapp:dev .

# Build and run tests only
docker build --target test -t myapp:test .

# Build production (default, last stage)
docker build -t myapp:prod .
```

### Benefits of Multi-Stage Builds

1. **Smaller Images:** Final image only contains runtime dependencies
2. **Better Security:** No build tools or source code in production images
3. **Faster Deployments:** Smaller images transfer faster
4. **Cleaner Separation:** Clear distinction between build and runtime
5. **No need for build scripts:** Everything in one Dockerfile

### Troubleshooting# ###

If you enter this command

```bash
docker run -it ubuntu
```

and feedback is this
docker: Cannot connect to the Docker daemon at unix:///Users/olafstinnen/.docker/run/docker.sock. Is the docker daemon running?

Then you need to start docker desktop via Launchpad or via terminal command ```docker desktop start```

### Infos from Container

Allgemeine Docker-Befehle zum Vergleich was evtl. noch fehlen könnte

    docker run: Startet einen Container basierend auf einem Image.
    docker ps / docker ps -a: Listet laufende bzw. alle Container auf.
    docker stop [Container-ID]: Stoppt einen laufenden Container.
    docker start [Container-ID]: Startet einen gestoppten Container.
    docker rm [Container-ID]: Entfernt einen Container.
    docker kill [Container-ID]: Beendet einen Container sofort.
    docker images: Zeigt alle lokal gespeicherten Images an.
    docker rmi [Image-ID]: Löscht ein Docker-Image.
    docker exec -it [Container-ID] [Befehl]: Führt Befehle in einem laufenden Container aus.
    docker logs [Container-ID]: Zeigt die Logs eines Containers an.
    docker inspect [Container-ID oder Image-ID]: Gibt detaillierte Konfigurationsdaten aus.
    docker build -t [Image-Name] .: Erzeugt ein Image aus einem Dockerfile.
    docker commit [Container-ID] [Image-Name]: Erstellt ein Image aus einem laufenden oder gestoppten Container.

Netzwerk-Related

    docker network create [Netzwerkname]: Erstellt ein benutzerdefiniertes Netzwerk.
    docker network ls: Zeigt alle Netzwerke an.
    docker network inspect [Netzwerkname]: Zeigt Details zu einem bestimmten Netzwerk.
    docker network prune: Entfernt ungenutzte Netzwerke.

Volumes

    docker volume create [Volume-Name]: Erstellt ein Volume.
    docker volume ls: Zeigt alle Volumes an.
    docker volume inspect [Volume-Name]: Gibt Details über ein Volume.
    docker volume rm [Volume-Name]: Löscht ein Volume.

## Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes. Then, with a single command, you create and start all the services from your configuration.

### Basic Docker Compose Commands

```bash
# Start all services defined in docker-compose.yml
docker-compose up

# Start in detached mode (background)
docker-compose up -d

# Stop and remove all containers, networks
docker-compose down

# Stop and remove including volumes
docker-compose down -v

# Build or rebuild services
docker-compose build

# Build without cache
docker-compose build --no-cache

# View logs from all services
docker-compose logs

# Follow log output
docker-compose logs -f

# View logs for specific service
docker-compose logs -f servicename

# List running services
docker-compose ps

# Execute command in running service
docker-compose exec servicename bash

# Run a one-off command
docker-compose run servicename command

# Stop services without removing them
docker-compose stop

# Start existing stopped services
docker-compose start

# Restart services
docker-compose restart

# Pause services
docker-compose pause

# Unpause services
docker-compose unpause

# Scale a service to multiple instances
docker-compose up -d --scale servicename=3
```

### Example 1: Simple Web Application with Database

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  # Web application service
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://user:password@db:5432/myapp
    depends_on:
      - db
    volumes:
      - ./app:/usr/src/app
    restart: unless-stopped

  # PostgreSQL database service
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

# Named volumes
volumes:
  postgres_data:
```

### Example 2: Full Stack Application with Multiple Services

```yaml
version: '3.8'

services:
  # Frontend React application
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:5000
    depends_on:
      - backend
    networks:
      - app-network

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/appdb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - ./backend/uploads:/app/uploads
    networks:
      - app-network
    restart: unless-stopped

  # PostgreSQL database
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: appdb
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - app-network
    restart: unless-stopped

  # Redis cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - app-network
    restart: unless-stopped

  # Nginx reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - frontend
      - backend
    networks:
      - app-network
    restart: unless-stopped

volumes:
  db_data:
  redis_data:

networks:
  app-network:
    driver: bridge
```

### Example 3: Using Environment Files

Create a `.env` file:

```env
# Database
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase

# Application
APP_PORT=3000
NODE_ENV=production
```

Reference in `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "${APP_PORT}:3000"
    environment:
      - NODE_ENV=${NODE_ENV}
      - DB_HOST=db
      - DB_USER=${POSTGRES_USER}
      - DB_PASS=${POSTGRES_PASSWORD}
    env_file:
      - .env

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```

### Example 4: Development with Hot Reload

```yaml
version: '3.8'

services:
  dev:
    build:
      context: .
      target: development  # Use development stage from multi-stage Dockerfile
    ports:
      - "3000:3000"
      - "9229:9229"  # Node debugger port
    volumes:
      - ./src:/app/src  # Mount source for hot reload
      - /app/node_modules  # Don't override node_modules
    environment:
      - NODE_ENV=development
      - DEBUG=app:*
    command: npm run dev
```

### Docker Compose with Healthchecks

```yaml
version: '3.8'

services:
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### Key Docker Compose Concepts

**depends_on:** Controls service startup order (but doesn't wait for service to be "ready")

**networks:** Isolate services, create custom networks

**volumes:** Persist data, share data between services

**environment:** Set environment variables

**env_file:** Load environment variables from file

**restart policies:**
- `no`: Don't restart (default)
- `always`: Always restart
- `on-failure`: Restart on failure
- `unless-stopped`: Always restart unless manually stopped

### Docker Compose Override

Create a `docker-compose.override.yml` for local development:

```yaml
version: '3.8'

services:
  web:
    volumes:
      - ./src:/app/src
    environment:
      - DEBUG=true
```

Docker Compose automatically merges `docker-compose.yml` and `docker-compose.override.yml`.

## Docker Security Best Practices

Security should be a primary concern when working with Docker. Here are essential best practices to secure your containers and images.

### 1. Use Official and Verified Images

Always prefer official images from trusted sources:

```Dockerfile
# Good - Official image
FROM node:18-alpine

# Avoid - Unknown source
FROM randomuser/node
```

Verify image sources:

```bash
docker search --filter is-official=true nginx
docker pull nginx  # Official images don't have username prefix
```

### 2. Run Containers as Non-Root User

Running containers as root is a security risk. Create and use a non-root user:

```Dockerfile
FROM node:18-alpine

# Create a non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Set ownership
WORKDIR /app
COPY --chown=nodejs:nodejs . .

# Switch to non-root user
USER nodejs

CMD ["node", "server.js"]
```

Verify user in running container:

```bash
docker exec [Container-ID] whoami
```

### 3. Use Specific Image Tags

Never use `latest` tag in production:

```Dockerfile
# Bad - Unpredictable
FROM node:latest

# Good - Specific version
FROM node:18.17.0-alpine3.18

# Also good - Major version pinning
FROM node:18-alpine
```

### 4. Scan Images for Vulnerabilities

Use Docker Scout or other scanning tools:

```bash
# Scan an image for vulnerabilities
docker scout cves my-image:latest

# Get recommendations
docker scout recommendations my-image:latest

# Use Trivy (third-party tool)
trivy image my-image:latest
```

### 5. Minimize Image Size and Attack Surface

Use multi-stage builds and minimal base images:

```Dockerfile
# Use minimal base images
FROM alpine:3.18  # ~5MB
FROM node:18-alpine  # Smaller than node:18
FROM gcr.io/distroless/nodejs:18  # Even smaller, no shell

# Remove unnecessary packages
RUN apk add --no-cache curl && \
    rm -rf /var/cache/apk/*
```

### 6. Don't Store Secrets in Images

Never hardcode secrets in Dockerfiles or images:

```Dockerfile
# Bad - Hardcoded secrets
ENV API_KEY=abc123secret
ENV DATABASE_PASSWORD=mypassword

# Good - Use secrets at runtime
# Pass via environment variables or Docker secrets
```

Use Docker secrets or environment variables:

```bash
# Pass secrets at runtime
docker run -e API_KEY="${API_KEY}" my-image

# Use Docker secrets (Swarm mode)
echo "my-secret-value" | docker secret create api_key -
docker service create --secret api_key my-service
```

### 7. Limit Container Resources

Prevent resource exhaustion attacks:

```bash
# Limit memory and CPU
docker run -m 512m --cpus="1.5" my-image

# In docker-compose.yml
services:
  app:
    image: my-app
    deploy:
      resources:
        limits:
          cpus: '1.5'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

### 8. Use Read-Only Filesystem

Make container filesystem read-only when possible:

```bash
# Run with read-only root filesystem
docker run --read-only --tmpfs /tmp my-image

# In docker-compose.yml
services:
  app:
    image: my-app
    read_only: true
    tmpfs:
      - /tmp
```

### 9. Disable Unnecessary Capabilities

Drop Linux capabilities you don't need:

```bash
# Drop all capabilities and add only what's needed
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE my-image

# In docker-compose.yml
services:
  app:
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
```

### 10. Use Security Scanning in CI/CD

Integrate security scanning in your pipeline:

```yaml
# GitHub Actions example
- name: Build Docker image
  run: docker build -t my-app:${{ github.sha }} .

- name: Scan image
  run: |
    docker scout cves my-app:${{ github.sha }}
    trivy image --severity HIGH,CRITICAL my-app:${{ github.sha }}
```

### 11. Keep Images Updated

Regularly update base images and dependencies:

```bash
# Pull latest version of base image
docker pull node:18-alpine

# Rebuild your images
docker build --no-cache -t my-app:latest .

# Update all containers
docker-compose pull
docker-compose up -d
```

### 12. Use Docker Bench for Security

Run Docker Bench Security to audit your Docker installation:

```bash
# Run Docker Bench for Security
docker run --rm --net host --pid host --userns host --cap-add audit_control \
  -v /var/lib:/var/lib \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /etc:/etc --label docker_bench_security \
  docker/docker-bench-security
```

### 13. Network Isolation

Use custom networks to isolate containers:

```bash
# Create isolated networks
docker network create --driver bridge frontend-net
docker network create --driver bridge backend-net

# Connect containers to appropriate networks
docker run --network frontend-net web-app
docker run --network backend-net database
```

### 14. Enable Docker Content Trust

Sign and verify images:

```bash
# Enable Docker Content Trust
export DOCKER_CONTENT_TRUST=1

# Now all pulls and pushes require signatures
docker pull my-image:latest  # Will verify signature
docker push my-image:latest  # Will require signing
```

### 15. Secure Docker Daemon

Configure Docker daemon securely:

```json
// /etc/docker/daemon.json
{
  "icc": false,
  "log-level": "info",
  "userland-proxy": false,
  "no-new-privileges": true,
  "live-restore": true
}
```

### Security Checklist

- [ ] Use official or trusted base images
- [ ] Specify exact image versions (avoid `latest`)
- [ ] Run containers as non-root user
- [ ] Scan images for vulnerabilities regularly
- [ ] Use multi-stage builds to minimize image size
- [ ] Never store secrets in images
- [ ] Limit container resources (CPU, memory)
- [ ] Use read-only filesystems where possible
- [ ] Keep images and dependencies updated
- [ ] Implement network isolation
- [ ] Drop unnecessary Linux capabilities
- [ ] Enable security scanning in CI/CD
- [ ] Use `.dockerignore` to exclude sensitive files
- [ ] Implement proper logging and monitoring
- [ ] Enable Docker Content Trust for production

### Example: Secure Dockerfile Template

```Dockerfile
# Use specific version of minimal base image
FROM node:18.17.0-alpine3.18 AS builder

# Install only necessary build dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && \
    npm cache clean --force

# Copy application code
COPY . .
RUN npm run build

# Production stage with minimal image
FROM node:18.17.0-alpine3.18

# Add security labels
LABEL security.scan="enabled" \
      maintainer="security@example.com"

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --chown=nodejs:nodejs package*.json ./

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Run application
CMD ["node", "dist/server.js"]
```

Swarm-Modus

    docker swarm init: Initialisiert ein neues Docker Swarm-Cluster.
    docker swarm join: Fügt einen Knoten zu einem bestehenden Swarm hinzu.
    docker swarm leave: Verlässt einen bestehenden Swarm.
    docker service create: Erstellt einen neuen Service.
    docker service ls: Zeigt alle Services in einem Swarm an.
    docker service ps [Service-Name]: Zeigt alle Tasks eines bestimmten Services.
    docker service update: Aktualisiert einen existierenden Service.
    docker service rm [Service-Name]: Entfernt einen Service.

Kubernetes (wenn behandelt)

    kubectl apply -f [Datei.yml]: Erstellt Ressourcen in einem Kubernetes-Cluster.
    kubectl get pods: Zeigt eine Liste aller Pods im Cluster.
    kubectl delete pod [Pod-Name]: Löscht einen bestimmten Pod.
    kubectl describe [Ressourcen-Typ] [Name]: Gibt Details zu einer Ressource aus.
