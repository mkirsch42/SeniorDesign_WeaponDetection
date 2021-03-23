# UCONN Senior Design - Weapon Detection

## Getting Started

### Requirements (Windows)

Ensure you are running WSL 2. Follow the directions at https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps.

Install [Ubuntu for WSL](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab).

- [Docker](https://docs.docker.com/get-docker/)
- Docker Compose
- *If using CV2WindowOutput*: [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
- *Optional*: [Docker Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

Docker and VcXsrv can both be installed via [Chocolatey](https://chocolatey.org/install#individual) on Windows:

> ```choco install docker-desktop docker-compose vcxsrv```

### Initial Setup

#### Windows
- Run `./setup.sh` in Ubuntu for WSL. The script will build the darknet library and install npm packages.
- In a regular command line, run `docker-compose build`.

### Running the Application

- If using CV2WindowOutput, start VcXsrv (the start menu entry might be called XStart), using the default options:
    - Multiple windows
    - Display number: -1
    - Start no client
    - Native OpenGL enabled
- `docker-compose up`
    - If using the VS Code extension, you can also start the application through the Docker tab.