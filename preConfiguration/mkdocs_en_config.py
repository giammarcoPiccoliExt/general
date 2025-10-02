import yaml

with open('mkdocs.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# plugins è una lista, non un dict
for plugin in config['plugins']:
    if isinstance(plugin, dict) and 'i18n' in plugin:
        plugin['i18n']['languages'] = [
            {'locale': 'en', 'name': 'English', 'build': True},
            {'locale': 'it', 'name': 'Italian', 'build': True}
        ]

with open('mkdocs_en.yml', 'w', encoding='utf-8') as f:
    yaml.safe_dump(config, f, sort_keys=False)
