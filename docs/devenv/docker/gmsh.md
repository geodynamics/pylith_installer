# Install gmsh outside Docker container

These commands will install Gmsh and the PyLith `gmsh_utils.py` Python module into a Python virtual environment in `$HOME/gmsh`.

:::{important}
For Gmsh we strongly recommend using your system Python or a binary Python package for your system downloaded from Python.org as opposed to Python from Conda or Anaconda.
This reduces the disk space and provides a simpler installation.
:::

```{code-block} bash
# Set some variables (tune to your system)
GMSH_DIR=$HOME/gmsh
PYTHON_VERSION=3.10

# Create and activate the Python virtual environment
python3 -m venv $GMSH_DIR
source $GMSH_DIR/bin/activate

# Install Gmsh
pip install gmsh

# Install the gmsh_utils.py Python module
mkdir -p $GMSH_DIR/lib/python$PYTHON_VERSION/site-packages/pylith/meshio
touch $GMSH_DIR/lib/python$PYTHON_VERSION/site-packages/pylith/meshio/__init.py__
touch $GMSH_DIR/lib/python$PYTHON_VERSION/site-packages/pylith/__init.py__

# Copy gmsh_utils.py from running Docker container
# (alternatively, download it from https://github.com/geodynamics/pylith/blob/main/pylith/meshio/gmsh_utils.py)
docker cp pylith-dev-workspace:/opt/pylith/src/pylith/pylith/meshio/gmsh_utils.py $GMSH_DIR/lib/python$PYTHON_VERSION/site-packages/pylith/meshio/
```
