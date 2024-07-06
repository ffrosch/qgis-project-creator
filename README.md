# Python QGIS Project Creator

- [Python QGIS Project Creator](#python-qgis-project-creator)
  - [Usage](#usage)
  - [Installation](#installation)
    - [Linux with `conda`](#linux-with-conda)
  - [Development](#development)
    - [Build](#build)
    - [Style guide](#style-guide)
      - [Commits](#commits)
      - [Changelog](#changelog)

## Usage

QGIS has to be installed on the system and needs to support Python 3.12 (e.g. QGIS 3.34 or newer).
Python needs to know the path to the QGIS Python API, which can be set with the `PYTHONPATH` environment variable.

```bash
export PYTHONPATH=/path/to/qgis/python
```

The preferred way to use this package is with `conda`, because it's possible to also install a specific version of QGIS with conda and the `PYTHONPATH` environment variable is set automatically by `qgis` from `conda-forge`.

```bash
CONDA_ENV=<your-env-name>
conda activate ${CONDA_ENV}
```

## Installation

The package itself is installed with `pip`:

```bash
pip install qgis-project-creator
```

### Linux with `conda`

Preferred way to use this package, because you are free to use whichever version of QGIS you want.

```bash
export CONDA_ENV=<your-env-name>
# make sure conda version is >=4.9
# conda --version
# conda update conda
# add conda-forge as the highest priority channel
conda config --add channels conda-forge
# Strict channel priority can dramatically speed up conda operations and also reduce package incompatibility problems
conda config --set channel_priority strict
# Create your environment
conda create -n ${CONDA_ENV} python=3.12.3 qgis=3.34
conda activate ${CONDA_ENV}
conda install pip
pip install qgis-project-creator qgis-stubs
# Set on KDE Plasma 6 with Wayland to run QGIS with the X11 backend:
conda env config vars set QT_QPA_PLATFORM=xcb
# reactivate the environment for changes to take effect
conda activate ${CONDA_ENV}
```

## Development

Use the conda environment from `environment.dev.yml`:

```bash
conda env create -f environment.dev.yml
conda activate qgis-project-creator-dev
```

Changes to the environment should be defined in `environment.dev.yml` and then applied with:

```bash
conda env update -f environment.dev.yml --prune
```

### Build

```bash
python -m build
```

### Style guide

- [Python Packages - Modern and efficient workflows](https://py-pkgs.org/welcome)
- [Releasing and versioning](https://py-pkgs.org/07-releasing-versioning.html#releasing-and-versioning)
- [Changelog](https://py-pkgs.org/06-documentation#changelog)

#### Commits

[Commit style](https://py-pkgs.org/07-releasing-versioning.html#automatic-version-bumping):

- `feat`: A new feature.
- `fix`: A bug fix.
- `docs`: Documentation changes.
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `perf`: A code change that improves performance.
- `test`: Changes to the test framework.c
- `build`: Changes to the build process or tools.

`scope` is an optional keyword that provides context for where the change was made. It can be anything relevant to your package or development workflow (e.g., it could be the module or function name affected by the change).

```text
<type>(optional scope): short summary in present tense

(optional body: explains motivation for the change)

(optional footer: note BREAKING CHANGES here, and issues to be closed)
```

#### Changelog

The changelog is documented in `CHANGELOG.md` and should look something like this:

```markdown
# Changelog

<!--next-version-placeholder-->

## v0.2.0 (10/09/2021)

### Feature

- Added new datasets modules to load example data

### Fix

- Check type of argument passed to `plotting.plot_words()`

### Tests

- Added new tests to all package modules in test_pycounts.py

## v0.1.0 (24/08/2021)

- First release of `pycounts`
```
