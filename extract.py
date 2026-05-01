import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

emojis = set(re.findall(r'<div class="item-e">(.*?)</div>', html))
with open('emojis.json', 'w', encoding='utf-8') as f:
    json.dump(list(emojis), f, ensure_ascii=False)
