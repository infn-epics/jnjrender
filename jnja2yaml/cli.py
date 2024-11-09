# jnja2yaml/cli.py

import argparse
import yaml
from jinja2 import Template
from .renderer import render_jinja_to_yaml

def main():
    parser = argparse.ArgumentParser(description="Render a Jinja2 template to YAML")
    parser.add_argument("jinja_file", type=str, help="Path to the Jinja2 template file")
    parser.add_argument("yaml_file", type=str, help="Path to the YAML file with variables")
    
    args = parser.parse_args()

    with open(args.yaml_file, 'r') as yaml_stream:
        variables = yaml.safe_load(yaml_stream)

    with open(args.jinja_file, 'r') as jinja_stream:
        jinja_content = jinja_stream.read()

    rendered_output = render_jinja_to_yaml(jinja_content, variables)
    print(rendered_output)

if __name__ == "__main__":
    main()

