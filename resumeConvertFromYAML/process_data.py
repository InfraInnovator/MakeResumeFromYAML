# process_data.py

import argparse
import importlib
import pkgutil
import yaml

def load_modules():
    modules = {}
    for finder, name, ispkg in pkgutil.iter_modules(['modules']):
        if not ispkg:
            module = importlib.import_module(f'modules.{name}')
            modules[name] = module
    return modules

def load_data(input_file):
    with open(input_file, 'r') as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Generate a document from a YAML file.")
    parser.add_argument("-i", "--input_file", required=True, help="Path to the YAML file containing data.")
    parser.add_argument("-o", "--output_file", required=True, help="Path to the output file.")
    parser.add_argument("-m", "--module", required=True, help="Module to use for processing.")
    parser.add_argument("-l", "--list_modules", action="store_true", help="List available modules.")
    # parser.add_argument("-v", "--verbose", action="store_true", help="Print debug information.")

    modules = load_modules()

    if len(modules) == 0:
        print("No modules found.")
        return

    if parser.parse_args().list_modules:
        print("Available modules:")
        for name in modules.keys():
            print(f"  {name}")
        return


    # Let each module add its specific arguments if necessary
    for name, mod in modules.items():
        if hasattr(mod, 'add_arguments'):
            mod.add_arguments(parser)

    args = parser.parse_args()

    # Validate and load data from YAML
    data = load_data(args.input_file)
    if data is None:
        print("No data loaded from file.")
        return

    # Module processing
    if args.module in modules:
        module = modules[args.module]
        if hasattr(module, 'generate'):
            module.generate(data, args.output_file)
        else:
            print(f"Module {args.module} is not properly configured to process data.")
    else:
        print("Selected module not found.")

if __name__ == '__main__':
    main()
