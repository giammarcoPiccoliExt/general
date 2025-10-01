import json
import yaml
from jinja2 import Template

# Carica le variabili base (site_name, author)
with open("preConfiguration/config.json") as f:
    config = json.load(f)

# Carica nav da nav.yml e converti in stringa YAML
with open("preConfiguration/nav_config.yml") as f:
    nav_yaml = f.read()

# Carica il template
with open("preConfiguration/mkdocs-template.yml.j2") as f:
    template = Template(f.read())

# Genera mkdocs.yml
output = template.render(**config, nav_yaml=nav_yaml)


# Salva mkdocs.yml (ITA)
import os
it_path = "documentation/mkdocs.yml"
it_dir = os.path.dirname(it_path)
if it_dir and not os.path.exists(it_dir):
    os.makedirs(it_dir, exist_ok=True)
with open(it_path, "w") as f:
    f.write(output)

print("✅ mkdocs.yml ITA  generato con successo.")

