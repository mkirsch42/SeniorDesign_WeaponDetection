# UCONN Senior Design - Weapon Detection

## Getting Started

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
- *Optional*: [Docker Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

Docker and VcXsrv can both be installed via [Chocolatey](https://chocolatey.org/install#individual) on Windows:

> ```choco install docker-desktop vcxsrv```

### Initial Setup

- Run `./setup.sh`. The script will build the darknet library with GPU bindings and then build the Docker image.

### Running the Application

- Start VcXsrv (the start menu entry might be called XStart), using the default options:
    - Multiple windows
    - Display number: -1
    - Start no client
    - Native OpenGL enabled
- `docker-compose up`
    - If using the VS Code extension, you can also start the application through the Docker tab.