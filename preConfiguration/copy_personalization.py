import os
import shutil

# Copy personalization folder to generated/it and generated/en
src = os.path.join("documentation", "overrides", "personalization")
destinations = [
    os.path.join("documentation", "generated", "it","overrides", "personalization"),
    os.path.join("documentation", "generated", "en","overrides", "personalization"),
]

for dst in destinations:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"Copied {src} to {dst}")
