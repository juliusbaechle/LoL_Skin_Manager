from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
import subprocess

ini = JSONDecoder().decode(open("config.json").read())
print(ini)

champ = "Ahri"
skin = 37  # KDA All Out - Emerald


src = f"{ini['league_path']}\\Game\\DATA\\FINAL\\Champions\\{champ}.wad.client"
dst = f"..\\orig\\{champ}"
code = subprocess.run([f"{ini['wadextract_path']}", src, dst])

src = f"..\\orig\\{champ}\\data\\characters\\ahri\\skins\\skin0.bin"
dst = f"..\\temp\\{champ}\\data\\characters\\ahri\\skins\\skin0.json"
code = subprocess.run([f"{ini['ritobin_path']}", src, dst])

skin0 = JSONDecoder().decode(open(dst).read())
SKIN_HASH = 2607278582
RESOURCE_HASH = 4013559603
for item in skin0['entries']['value']['items']:
    if item['value']['name'] == SKIN_HASH:
        skin_hash = item['key']
    if item['value']['name'] == RESOURCE_HASH:
        resource_hash = item['key']

src = f"..\\orig\\{champ}\\data\\characters\\ahri\\skins\\skin{skin}.bin"
dst = f"..\\temp\\{champ}\\data\\characters\\ahri\\skins\\skin{skin}.json"
code = subprocess.run([f"{ini['ritobin_path']}", src, dst])

skin37 = JSONDecoder().decode(open(dst).read())
for item in skin37['entries']['value']['items']:
    if item['value']['name'] == SKIN_HASH:
        item['key'] = skin_hash
    if item['value']['name'] == RESOURCE_HASH:
        item['key'] = resource_hash
open(dst, mode='w').write(JSONEncoder().encode(skin37))

src = f"..\\temp\\{champ}\\data\\characters\\ahri\\skins\\skin{skin}.json"
dst = f"..\\mods\\{champ}\\data\\characters\\ahri\\skins\\skin0.bin"
code = subprocess.run([f"{ini['ritobin_path']}", src, dst])