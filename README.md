# Sneakers MVP service 

### This is the main repo for sneakers  project

# Other project repos : 

### Triton inference server [triton](https://github.com/Best-sneakers/triton-inference-server)
### Airflow service  [airflow](https://github.com/Best-sneakers/Airflow_sneakers)
### EDA [eda](https://github.com/Best-sneakers/EDA)

## Application Launch

### Development

To launch the application in the development environment,
there are options to run it directly using python and through 
docker-compose. Both options use environment variables for configuration, 
which are described in the app/settings/settings.py file. 
In these run modes, it's possible to update the application code on the fly without restarting 
(except when adding new dependencies).


#### Python Runner

```bash
python -m mvp_sneakers_api
```

#### Docker runner

```bash
docker compose up -d
```

```bash
make build
```
This command will create a .env file from .env.example and build the containers.

#### Project linting:

```bash
make lint
```


### Before You Begin


```bash
make dev
```

This command to set up pre commit config in order to check your code before commit 

### Dependency's

Dependency management is handled by the poetry utility. 
The list of dependencies is in the pyproject.toml file. 
Instructions for setting up a poetry environment for PyCharm can be found here.
To add a dependency, simply write poetry add requests,
and the utility will automatically choose a version that does not conflict with current dependencies. 
Dependencies with exact versions are recorded in the poetry.lock file. To get a dependency tree, you can use the command poetry show --tree. 
Other commands are available in the official documentation for the utility.


### Testing 

Tests are designed as a completely independent solution. Tests require. 
To run the tests, use the following command in the project root:

```bash
make tests
```
