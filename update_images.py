import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's map certain keywords in item-name to premium unsplash IDs.
image_mapping = {
    "Sencilla": "1534620808146-d33bb39128b4", # Toast
    "Mediterránea": "1525351484163-7529414344d8", # Tomato toast
    "Catalana": "1625937286074-9ca519d5d9fc", # Jamon toast
    "Serrana": "1511690656952-34342bb7c2f2", # Jamon and cheese
    "Caprese": "1529312266112-b33cf4f68b48", # Caprese toast
    "Milano": "1588825835269-e970a049d5a9", # fancy toast
    "Toscana": "1564834724105-918b73d1b9e0", # another fancy toast
    "Fit": "1484723091791-0fee59ca0b28", # avocado toast
    "California": "1603048297172-c92544798d5e", # avocado egg toast
    "Provenzal": "1514362545857-3bc16c4c7d1b", # cheese honey toast
    "Suave de Pavo": "1515003197209-66380c55dc4b", # turkey toast
    "Croissant Mantequilla": "1555507036-ab1f40ce88cb",
    "Croissant Plancha": "1509365465985-25d11c17e812",
    "Napolitana Chocolate": "1622543925917-763c34d1a86e",
    "Mixto": "1528735602780-2552fd46c757", # sandwich
    "Vegetal": "1550583724-b2692b85b150", # sandwich
    "Tarta Casera": "1588195538326-c5b4e9f6aca1", # cake
    "Café Solo": "1514432324607-a09d9b4aefdd",
    "Café con Leche": "1497935586351-b67a49e012bf",
    "Latte Macchiato": "1509042239860-f550ce710b93",
    "Capuccino": "1572442388796-11668a67e53d",
    "Chocolate Caliente": "1544025162-81111420d48f",
    "Zumo de Naranja": "1600271886742-f049cd451bba",
    "Smoothie Tropical": "1556679343-c7306c1976bc",
    "Cerveza Artesanal": "1535958636474-b021ee887b13",
    "Mojito": "1551538827-9c037cb4f32a"
}

default_id = "1484723091791-0fee59ca0b28" # A generic beautiful food image

def replace_item(match):
    full_item = match.group(0)
    name_match = re.search(r'<div class="item-name">(.*?)</div>', full_item)
    if name_match:
        name = name_match.group(1).strip()
        image_id = image_mapping.get(name, default_id)
        # Create premium URL
        new_url = f"https://images.unsplash.com/photo-{image_id}?auto=format&fit=crop&w=400&h=400&q=80"
        
        # Replace the src inside this item
        new_item = re.sub(r'<img src=".*?"', f'<img src="{new_url}"', full_item)
        return new_item
    return full_item

new_html = re.sub(r'<div class="item">.*?</div></div></div>', replace_item, html, flags=re.DOTALL)

# Fallback: if there are any remaining w=150, replace them with w=400 to make sure they are high quality.
new_html = new_html.replace('w=150', 'w=400')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Images upgraded to premium size and quality!")
