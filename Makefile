# Makefile

# Variables
CONDA_ENV_NAME = proyecto7

.PHONY: setup create_env run_flask

# Default rule
setup: create_env run_flask

create_env:
    conda env create -f environment.yml -n $(CONDA_ENV_NAME)

run_flask:
    conda run -n $(CONDA_ENV_NAME) flask run
