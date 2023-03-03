# Python Polylith Example

This is a repository with an example `Python` setup of the Polylith Architecture.
Here you will find examples of code being shared between different kind of projects, and the developer tooling setup.

## Developer experience

### Mypy
Have a look at the `mypy.ini` configuration file, to make `Mypy` work really well with this type of architecture.

``` ini
[mypy]
mypy_path = components, bases
namespace_packages = True
explicit_package_bases = True
```

#### The "loose" theme
This repository is setup with the `loose` theme, a Python exclusive addition to the architecture.
The theme is about the folder structure of components:

`components/<namespace>/<name>`, and a separate `tests` top folder.

Currently, there is poor support in Mypy for the original Polylith component structure:

`components/<name>/<src or test>/<namespace>/<name>/`

With the original Polylith structure, you will have to explicitly add each component path to the `mypy_path`.
There is [a feature request](https://github.com/python/mypy/issues/9965) in the mypy repo about adding regex support to the `mypy_path` property.
Hopefully it will be implemented in the future. :pray:

### .venv
It is recommended to create the virtual environment locally, for a great code editor experience.
By default, `Poetry` will create a `venv` outside of the repo. You can override that behaviour by adding a configuration in a `poetry.toml` file:

``` toml
[virtualenvs]
path = ".venv"
in-project = true
```

### Tooling support
There's tooling support for using Polylith in Python. Have a look at this repository:
[Python tools for the Polylith Architecture](https://github.com/DavidVujic/python-polylith)


### Tests

Run tests with:

```bash
poetry run pytest test/
```