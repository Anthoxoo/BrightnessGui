#!/bin/bash

DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
CONDA_EXEC="conda"
$CONDA_EXEC run -n base python "$DIR_PATH/main.py"