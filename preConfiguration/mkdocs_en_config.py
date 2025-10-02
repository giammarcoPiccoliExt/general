import yaml
from pathlib import Path

base_path = Path(__file__).parent.parent / 'documentation'
mkdocs_file = base_path / 'mkdocs.yml'
mkdocs_en_file = base_path / 'mkdocs_en.yml'

# Leggi mkdocs.yml
with mkdocs_file.open('r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Modifica solo il plugin i18n
for plugin in config.get('plugins', []):
    if isinstance(plugin, dict) and 'i18n' in plugin:
        plugin['i18n']['languages'] = [
            {'locale': 'en', 'name': 'English', 'default': True, 'build': True},
            {'locale': 'it', 'name': 'Italian', 'default': False, 'build': True}
        ]

# Salva in mkdocs_en.yml
with mkdocs_en_file.open('w', encoding='utf-8') as f:
    yaml.safe_dump(config, f, sort_keys=False)
