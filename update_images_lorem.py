import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update CSS for larger columns
html = html.replace('minmax(280px, 1fr)', 'minmax(360px, 1fr)')

# Add missing CSS for .item-body wrapping
css_to_add = '.item-body { flex: 1; min-width: 0; }\n  .item-name { font-size: 1.15rem; font-weight: 700; color: var(--bark); margin-bottom: .25rem; white-space: normal; }\n  .item-desc { font-size: .85rem; color: var(--muted); line-height: 1.4; white-space: normal; }'
if '.item-body { flex: 1' not in html:
    html = html.replace('.item-e img {', css_to_add + '\n  .item-e img {')

# Use regex to find and replace images with LoremFlickr targeted URLs
def repl(match):
    prefix = match.group(1)
    old_src = match.group(2)
    suffix = match.group(3)
    name = match.group(4).strip()
    
    # Generate deterministic lock id
    lock_id = sum(ord(c) for c in name) % 100 + 300
    
    # Assign category keywords
    keyword = 'toast,food'
    name_lower = name.lower()
    
    if 'croissant' in name_lower or 'napolitana' in name_lower or 'boller' in name_lower:
        keyword = 'croissant,pastry'
    elif 'café' in name_lower or 'latte' in name_lower or 'capuccino' in name_lower:
        keyword = 'coffee,latte'
    elif 'smoothie' in name_lower or 'zumo' in name_lower:
        keyword = 'smoothie,fruit'
    elif 'pancake' in name_lower or 'tortita' in name_lower:
        keyword = 'pancakes'
    elif 'mojito' in name_lower or 'cerveza' in name_lower:
        keyword = 'cocktail,drink'
    elif 'huevo' in name_lower or 'bacon' in name_lower:
        keyword = 'brunch,egg'
        
    new_src = f'https://loremflickr.com/400/400/{keyword}?lock={lock_id}'
    
    return f'{prefix}{new_src}{suffix}'

# Regex matches `<div class="item"><div class="item-e"><img src="...` and captures the name
pattern = re.compile(r'(<div class="item"><div class="item-e"><img src=")(.*?)(" alt="product image".*?<div class="item-name">)(.*?)</div>')
html = pattern.sub(repl, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated images to loremflickr and fixed grid!')
