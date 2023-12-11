import json
import yaml
import os
import argparse

# Function to get all the definitions referenced in a given operation
def get_definitions_from_operation(definitions, data):
    definitions = definitions if definitions is not None else set()
    for key, value in data.items():
        if isinstance(value, dict):
            definitions = get_definitions_from_operation(definitions, value)
        else:
            if key == '$ref' and value.startswith('#/definitions/'):
                definitions.add(value.split('/')[-1])
    return definitions

def filter_swagger(swagger_file, endpoints_to_keep):
    file_extension = os.path.splitext(swagger_file)[1]

    # Load the original Swagger file
    with open(swagger_file, 'r') as file:
        if file_extension == '.json':
            swagger_data = json.load(file)
        elif file_extension == '.yaml' or file_extension == '.yml':
            swagger_data = yaml.safe_load(file)
        else:
            print("Unsupported file type")

    # Filter the paths and collect definitions that are used
    filtered_paths = {}
    used_definitions = set()
    for path, info in swagger_data['paths'].items():
        if path in endpoints_to_keep:
            filtered_paths[path] = info
            for method in info.values():
                used_definitions.update(get_definitions_from_operation(used_definitions, method))

    # Filter the definitions
    filtered_definitions = {def_name: def_info for def_name, def_info in swagger_data['definitions'].items() if def_name in used_definitions}

    # Replace the paths and definitions in the original Swagger data
    swagger_data['paths'] = filtered_paths
    swagger_data['definitions'] = filtered_definitions

    # Save the filtered Swagger JSON to a new file
    with open('filtered_swagger.yaml', 'w') as file:
        yaml.dump(swagger_data, file, default_flow_style=False)

def main():
    parser = argparse.ArgumentParser(description='Filter a Swagger file to only include certain endpoints.')
    parser.add_argument('--swagger_file', type=str, default='swagger.json', help='The full path for a swagger.json (or yaml) file')
    parser.add_argument('--endpoints_to_keep', nargs='+', default=[], help='The endpoints you want to keep')
    args = parser.parse_args()

    filter_swagger(args.swagger_file, args.endpoints_to_keep)

if __name__ == "__main__":
    main()
