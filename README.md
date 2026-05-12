# jnjrender

[![Tests](https://github.com/infn-epics/jnjrender/actions/workflows/test.yml/badge.svg)](https://github.com/infn-epics/jnjrender/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/jnjrender)](https://pypi.org/project/jnjrender/)

**jnjrender** is a Python CLI tool that renders [Jinja2](https://jinja.palletsprojects.com/) templates using variables from a YAML file. It is designed for generating EPICS IOC configuration files and other structured YAML-based configs from template libraries.

## Features

- Render a single `.j2` template file with variables from a YAML file.
- **Auto mode (`--auto`)**: given a template library directory and an output directory, automatically select and render only the template whose name matches the `template` key in the YAML file — no unrelated templates are touched.
- **Named template mode (`--template`)**: explicitly select a template by name from a directory.
- Render all `.j2` files in a directory when no specific template is specified.
- Render `.j2` files in-place inside a destination directory (useful for Kubernetes init-containers).
- Preserves the file permissions of the source template on the rendered output.
- Prints rendered output to stdout when no `--output` is given.

## Installation

```bash
pip install jnjrender
```

Or from source:

```bash
git clone https://github.com/infn-epics/jnjrender.git
cd jnjrender
pip install .
```

## Usage

```
jnjrender <template> <variables.yaml> [--output <output>] [--auto] [--template NAME] [--version]
```

| Argument | Description |
|---|---|
| `template` | Path to a `.j2` file **or** a directory containing `.j2` files |
| `variables.yaml` | YAML file supplying the template variables |
| `--output`, `-o` | Output file or directory. Prints to stdout if omitted |
| `--auto` | Select the template whose name matches the `template` key in the YAML file |
| `--template NAME` | Explicitly select template `NAME.yaml.j2` from the input directory |
| `--version` | Print the version and exit |

### Render a single file

```bash
jnjrender device.yaml.j2 config.yaml --output device.yaml
# or print to stdout
jnjrender device.yaml.j2 config.yaml
```

### Auto-select template from a library directory

Given `config.yaml` containing `template: pfeiffer-tpg`, only `pfeiffer-tpg.yaml.j2` is rendered — other `.j2` files in the same directory are ignored.

```bash
jnjrender /epics/support/templates/ config.yaml --auto --output /epics/ioc/config/
```

### Explicitly name the template

```bash
jnjrender /epics/support/templates/ config.yaml --template pfeiffer-tpg --output /epics/ioc/config/
```

### Render `.j2` files already present in the output directory

```bash
find /epics/ioc/config -name "*.j2" -exec sh -c \
  'jnjrender "$1" config.yaml --output "${1%.j2}"' _ {} \;
```

## How `--auto` / `--template` work with directories

When both the input and output are directories and a template name is known:

1. `jnjrender` walks the input directory tree to find a **subdirectory** named `<template>` or a file named `<template>.yaml.j2`.
2. Only that matching `.j2` file (and any non-`.j2` companion files) are copied to the output directory.
3. The selected `.j2` file is rendered and saved alongside the non-template files.

This prevents sibling templates (e.g. `pfeiffer-hiscroll6.yaml.j2` next to `pfeiffer-tpg.yaml.j2`) from being rendered unintentionally.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Template file not found in directory |
| 3 | `template` key missing and no template name provided |
| 4 | Jinja2 file not found |
| 5 | Template rendering failed |
| 6 | Failed to write output file |
| 7 | Template directory not found under input path |

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
