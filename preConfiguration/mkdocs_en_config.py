import yaml
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python mkdocs_lang_config.py <lang>")
    sys.exit(1)

lang = sys.argv[1].lower()
if lang not in ['it', 'en']:
    print("Language must be 'it' or 'en'")
    sys.exit(1)

# Path del file mkdocs.yml
config_file = Path(__file__).parent.parent / "documentation" / "mkdocs.yml"

with open(config_file, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Configurazione i18n dinamica
config['plugins'] = config.get('plugins', [])
for i, plugin in enumerate(config['plugins']):
    if isinstance(plugin, dict) and 'i18n' in plugin:
        config['plugins'][i]['i18n']['languages'] = [
            {
                'locale': 'it',
                'default': lang=='it',
                'name': 'Italian',
                'build': lang=='it'
            },
            {
                'locale': 'en',
                'default': lang=='en',
                'name': 'English',
                'build': lang=='en'
            }
        ]
        # Rimuove eventuali opzioni obsolete
        config['plugins'][i].pop('default_language_only', None)

# Salva config temporanea per build
temp_file = Path(__file__).parent.parent / "documentation" / f"mkdocs_{lang}.yml"
with open(temp_file, 'w', encoding='utf-8') as f:
    yaml.dump(config, f, sort_keys=False)

print(f"Generated temporary config for language '{lang}': {temp_file}")
