import re

with open(r'C:\Users\Voldemort\.gemini\antigravity\brain\8acbd6f1-3836-4ade-b01d-2d365eafd980\.tempmediaStorage\dom_1777639631872.txt', 'r', encoding='utf-8') as f:
    dom_text = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def repl(match):
    desc_html = match.group(1)
    desc_text = re.sub(r'<.*?>', '', desc_html).strip()
    
    idx = dom_text.find(desc_text)
    name = 'Producto'
    if idx != -1:
        lines = dom_text[:idx].strip().split('\n')
        for line in reversed(lines):
            line = line.strip()
            # Ignore empty lines
            if line:
                name = line
                break
    return f'<div class="item-name">{name}</div>{desc_html}'

new_html = re.sub(r'<div class="item-name">(<div class="item-desc">.*?</div>)</div>', repl, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Restored item names!')
