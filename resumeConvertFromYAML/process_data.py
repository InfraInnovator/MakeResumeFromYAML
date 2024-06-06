import argparse
import importlib
import pkgutil
import yaml
from collections import defaultdict

def load_modules():
    modules = {}
    for finder, name, ispkg in pkgutil.iter_modules(['modules']):
        if not ispkg:
            module = importlib.import_module(f'modules.{name}')
            modules[name.lower()] = module  # Store modules in lowercase for case insensitivity
    return modules

def load_data(input_file):
    with open(input_file, 'r') as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Generate a document from a YAML file.")
    parser.add_argument("-i", "--input_file", required=True, help="Path to the YAML file containing data.")
    parser.add_argument("-o", "--output_file", required=True, help="Path to the output file.")
    parser.add_argument("-m", "--module", action='append', required=True, help="Modules to use for processing.")
    parser.add_argument("-l", "--list_modules", action="store_true", help="List available modules.")
    
    modules = load_modules()

    if len(modules) == 0:
        print("No modules found.")
        return

    args = parser.parse_args()

    if args.list_modules:
        print("Available modules:")
        for name in modules.keys():
            print(f"  {name}")
        return

    # Let each module add its specific arguments if necessary
    for name, mod in modules.items():
        if hasattr(mod, 'add_arguments'):
            mod.add_arguments(parser)

    # Validate and load data from YAML
    data = load_data(args.input_file)
    if data is None:
        print("No data loaded from file.")
        return

    shared_state = defaultdict(dict)  # Shared state for cross-module communication

    # Process each specified module in the order they were provided
    for module_name in args.module:
        module_name = module_name.lower()
        if module_name in modules:
            module = modules[module_name]
            if hasattr(module, 'generate'):
                module.generate(data, args.output_file, shared_state)  # Pass shared state to each module
            else:
                print(f"Module {module_name} is not properly configured to process data.")
        else:
            print(f"Module {module_name} not found.")

if __name__ == '__main__':
    main()
