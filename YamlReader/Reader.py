import yaml

with open('example.yaml', 'r') as file:
    example = yaml.safe_load(file)

print(example['package1']['version'])
print(example['package1']['dependencies'])