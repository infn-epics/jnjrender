import argparse
import os
import yaml
from jinja2 import Template

def render_jinja_to_yaml(jinja_file, yaml_file, output_file=None):
    try:
        # Load Jinja2 template
        with open(jinja_file) as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: Jinja2 file '{jinja_file}' does not exist.")
        return

    try:
        # Load YAML variables
        with open(yaml_file) as file:
            variables = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: YAML file '{yaml_file}' does not exist.")
        return

    # Render template with variables
    template = Template(template_content)
    rendered_content = template.render(variables)

    # Output to file or stdout
    if output_file:
        try:
            # Get the file permissions of the Jinja file
            jinja_permissions = os.stat(jinja_file).st_mode

            # Write the rendered content to the output file
            with open(output_file, 'w') as file:
                file.write(rendered_content)
            
            # Apply the same permissions as the Jinja file to the output file
            os.chmod(output_file, jinja_permissions)
            
            print(f"* rendered {jinja_file} -> {output_file} using {yaml_file}")
        except Exception as e:
            print(f"Error writing to output file '{output_file}': {e}")
    else:
        print(rendered_content)

def main():
    parser = argparse.ArgumentParser(description="Render a Jinja2 file with YAML variables.")
    parser.add_argument("jinja_file", help="Path to the Jinja2 template file.")
    parser.add_argument("yaml_file", help="Path to the YAML file with variables.")
    parser.add_argument("--output", "-o", help="File to write rendered output. Prints to stdout if not specified.")
    
    args = parser.parse_args()
    render_jinja_to_yaml(args.jinja_file, args.yaml_file, args.output)
    
if __name__ == "__main__":
    main()
