import yaml

with open("documentation/mkdocs.yml", "r") as f:
    config = yaml.safe_load(f)

# Mantieni solo EN per la build PDF
config['plugins']['i18n']['languages'] = [
    {"locale": "en", "default": True, "name": "English", "build": True}
]
config['plugins']['i18n']['default_language_only'] = True

# Salva configurazione temporanea
with open("documentation/mkdocs_en.yml", "w") as f:
    yaml.dump(config, f)
