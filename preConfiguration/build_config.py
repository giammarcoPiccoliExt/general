import json
import yaml
from jinja2 import Template

# Carica le variabili base (site_name, author)
with open("preConfiguration/it/config.json") as f:
    config = json.load(f)

# Carica nav da nav.yml e converti in stringa YAML
with open("preConfiguration/it/nav_config.yml") as f:
    nav_yaml = f.read()

# Carica il template
with open("preConfiguration/it/mkdocs-template.yml.j2") as f:
    template = Template(f.read())

# Genera mkdocs.yml
output = template.render(**config, nav_yaml=nav_yaml)


# Salva mkdocs.yml (ITA)
import os
it_path = "documentation/config/it/mkdocs.yml"
it_dir = os.path.dirname(it_path)
if it_dir and not os.path.exists(it_dir):
    os.makedirs(it_dir, exist_ok=True)
with open(it_path, "w") as f:
    f.write(output)

print("✅ mkdocs.yml ITA  generato con successo.")


# Carica le variabili base (site_name, author)
with open("preConfiguration/en/config.json") as f:
    config = json.load(f)

# Carica nav da nav.yml e converti in stringa YAML
with open("preConfiguration/en/nav_config.yml") as f:
    nav_yaml = f.read()

# Carica il template
with open("preConfiguration/en/mkdocs-template.yml.j2") as f:
    template = Template(f.read())

# Genera mkdocs.yml
output = template.render(**config, nav_yaml=nav_yaml)


# Salva mkdocs.yml (EN)
en_path = "documentation/config/en/mkdocs.yml"
en_dir = os.path.dirname(en_path)
if en_dir and not os.path.exists(en_dir):
    os.makedirs(en_dir, exist_ok=True)
with open(en_path, "w") as f:
    f.write(output)

print("✅ mkdocs.yml EN generato con successo.")