Pyenv is a tool that allows you to easily switch between different versions of Python on your system. Here is a quick cheatsheet of some common pyenv commands:

pyenv install <version>: Installs a specific version of Python. For example, pyenv install 3.9.1.
pyenv uninstall <version>: Uninstalls a specific version of Python.
pyenv versions: Lists all the versions of Python currently installed on your system.
pyenv global <version>: Sets the global version of Python for your system. This version will be used by default when you run python on the command line.
pyenv local <version>: Sets the local version of Python for the current directory. This version will be used by default when you run python in the current directory.
pyenv version: Shows the current version of Python that is being used.
pyenv virtualenv <version> <name>: Creates a new virtual environment with the specified version of Python and name.
pyenv activate <name>: Activates a virtual environment.
pyenv deactivate: Deactivates the current virtual environment.
pyenv which python: Shows the path to the Python executable that is currently being used.
pyenv shell <version>: Changes the shell environment to use the specified version of Python.
pyenv rehash: Rebuilds the shim binaries used by pyenv.
pyenv install -l: list all available python versions
Install a specific python version
>pyenv install 3.9.0a4
# Rehash your new installables. Needed to update pyenv shims.
>pyenv rehash
# Set global python version
>pyenv global 3.9.0a4
# Check global python version
>pyenv global
3.9.0a4
# Install other verion of python
>pyenv install 3.8.2
# Change directory to your project
>cd DreamProject
# Set local python version inside your project
DreamProject>pyenv local 3.8.2
# Check your local python version
DreamProject>pyenv local
3.8.2
