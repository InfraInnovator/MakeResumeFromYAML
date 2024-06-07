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
    parser.add_argument("-l", "--list_modules", action="store_true", help="List available modules.")
    parser.add_argument("-i", "--input_file", help="Path to the YAML file containing data.", required=False)
    parser.add_argument("-o", "--output_file", help="Path to the output file.", required=False)
    parser.add_argument("-m", "--module", action='append', help="Modules to use for processing.", required=False)

    args, unknown = parser.parse_known_args()  # Parse known args first

    modules = load_modules()

    if args.list_modules:
        if len(modules) == 0:
            print("No modules found.")
        else:
            print("Available modules:")
            for name in modules.keys():
                print(f"  {name}")
        return

    if not args.module or not args.input_file:
        parser.error("The following arguments are required: -i/--input_file, -m/--module")

    # Let each module add its specific arguments if necessary
    for name, mod in modules.items():
        if hasattr(mod, 'add_arguments'):
            mod.add_arguments(parser)

    args = parser.parse_args()  # Re-parse all arguments now that module-specific args are added

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
                if 'generate_preview' not in args.module and not args.output_file:
                    parser.error("The output file is required for modules other than generate_preview.")
                module.generate(data, args.output_file, shared_state)  # Pass shared state to each module
            else:
                print(f"Module {module_name} is not properly configured to process data.")
        else:
            print(f"Module {module_name} not found.")

if __name__ == '__main__':
    main()
