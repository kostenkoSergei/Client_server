import yaml

dict_to_yaml = {
    "first": ["one", "two", "tree"],
    "second": 5,
    "third": {
        "nested_one": "50€",
        "nested_two": "150€"
    }
}

with open("file.yaml", "w") as f:
    yaml.dump(dict_to_yaml, f, default_flow_style=False, allow_unicode=True)

with open("file.yaml", "r") as f:
    print(f.read())
