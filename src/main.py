from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
import subprocess
import shutil
import os

ini = JSONDecoder().decode(open("config.json").read())
champ = "ahri"
skin = 37 # KDA All Out - Emerald

# read original skin
src = f"{ini['league_path']}\\Game\\DATA\\FINAL\\Champions\\{champ.capitalize()}.wad.client"
dst = f"..\\orig\\{champ}"
cmd = f"{ini['cslol_manager_path']}\\cslol-tools\\wad-extract.exe"
code = subprocess.run([cmd, src, dst])

src = f"..\\orig\\{champ}\\data\\characters\\{champ}\\skins\\skin0.bin"
dst = f"..\\temp\\{champ}\\data\\characters\\{champ}\\skins\\skin0.json"
cmd = f"{ini['ritobin_path']}\\ritobin_cli.exe"
code = subprocess.run([cmd, src, dst])

base_skin = JSONDecoder().decode(open(dst).read())
SKIN_HASH = 2607278582
RESOURCE_HASH = 4013559603
for item in base_skin['entries']['value']['items']:
    if item['value']['name'] == SKIN_HASH:
        skin_hash = item['key']
    if item['value']['name'] == RESOURCE_HASH:
        resource_hash = item['key']

# read and modify new skin
src = f"..\\orig\\{champ}\\data\\characters\\{champ}\\skins\\skin{skin}.bin"
dst = f"..\\temp\\{champ}\\data\\characters\\{champ}\\skins\\skin{skin}.json"
cmd = f"{ini['ritobin_path']}\\ritobin_cli.exe"
code = subprocess.run([cmd, src, dst])

new_skin = JSONDecoder().decode(open(dst).read())
for item in new_skin['entries']['value']['items']:
    if item['value']['name'] == SKIN_HASH:
        item['key'] = skin_hash
    if item['value']['name'] == RESOURCE_HASH:
        item['key'] = resource_hash
open(dst, mode='w').write(JSONEncoder().encode(new_skin))

src = f"..\\temp\\{champ}\\data\\characters\\{champ}\\skins\\skin{skin}.json"
dst = f"..\\mod\\{champ}\\data\\characters\\{champ}\\skins\\skin0.bin"
cmd = f"{ini['ritobin_path']}\\ritobin_cli.exe"
code = subprocess.run([cmd, src, dst])

exit(0)
# integrate new skin into cslol-manager
name = f"{champ} {skin}"
src = f"..\\mod\\{champ}\\data"
dst = f"{ini['cslol_manager_path']}\\installed\\{name}\\WAD\\{champ.capitalize()}.wad.client"
cmd = f"{ini['cslol_manager_path']}\\cslol-tools\\wad-make.exe"
code = subprocess.run([cmd, src, dst])

info = JSONDecoder().decode(open("default_info.json").read())
info['name'] = name.capitalize()
dst = f"{ini['cslol_manager_path']}\\installed\\{name}\\META"
os.makedirs(dst, exist_ok=True)
open(f"{dst}\\info.json", mode='w').write(JSONEncoder().encode(info))

# delete obsolete directories
shutil.rmtree("..\\temp\\")
shutil.rmtree("..\\orig\\")
#shutil.rmtree("..\\mod\\")