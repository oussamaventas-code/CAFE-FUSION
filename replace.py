import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

emoji_map = {
  "🍻": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?auto=format&fit=crop&w=150&q=80",
  "🍵": "https://images.unsplash.com/photo-1597481499750-3e6b22637e12?auto=format&fit=crop&w=150&q=80",
  "🦃": "https://images.unsplash.com/photo-1514516345957-556ca7d90a29?auto=format&fit=crop&w=150&q=80",
  "🍌": "https://images.unsplash.com/photo-1481349518771-20055b2a7b24?auto=format&fit=crop&w=150&q=80",
  "🥓": "https://images.unsplash.com/photo-1606851094655-b25cb7a63973?auto=format&fit=crop&w=150&q=80",
  "🍪": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?auto=format&fit=crop&w=150&q=80",
  "🌅": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=150&q=80",
  "🍮": "https://images.unsplash.com/photo-1563805042-7684c8a9e9cb?auto=format&fit=crop&w=150&q=80",
  "🌟": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=150&q=80",
  "🍑": "https://images.unsplash.com/photo-1533722741913-7d7d24d27161?auto=format&fit=crop&w=150&q=80",
  "🍟": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=150&q=80",
  "🫓": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=150&q=80",
  "🍋": "https://images.unsplash.com/photo-1609505848912-b7c3b8b4beda?auto=format&fit=crop&w=150&q=80",
  "🥜": "https://images.unsplash.com/photo-1535515714777-62f97cecb2a2?auto=format&fit=crop&w=150&q=80",
  "🧀": "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&w=150&q=80",
  "🥑": "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?auto=format&fit=crop&w=150&q=80",
  "🥭": "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=150&q=80",
  "🍓": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=150&q=80",
  "🥗": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=150&q=80",
  "🍅": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=150&q=80",
  "🥩": "https://images.unsplash.com/photo-1544025162-81111420d48f?auto=format&fit=crop&w=150&q=80",
  "🥥": "https://images.unsplash.com/photo-1526653054245-2070c06ab869?auto=format&fit=crop&w=150&q=80",
  "🫔": "https://images.unsplash.com/photo-1626200419189-39c8c1915496?auto=format&fit=crop&w=150&q=80",
  "🍫": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?auto=format&fit=crop&w=150&q=80",
  "🍗": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=150&q=80",
  "💍": "https://images.unsplash.com/photo-1599824634351-a0ea21894a4c?auto=format&fit=crop&w=150&q=80",
  "🫙": "https://images.unsplash.com/photo-1582285311054-94ffcdd6db17?auto=format&fit=crop&w=150&q=80",
  "💧": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?auto=format&fit=crop&w=150&q=80",
  "🫧": "https://images.unsplash.com/photo-1556881286-fc6915169721?auto=format&fit=crop&w=150&q=80",
  "🥐": "https://images.unsplash.com/photo-1555507036-ab1e4006aa07?auto=format&fit=crop&w=150&q=80",
  "🍛": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=150&q=80",
  "🧇": "https://images.unsplash.com/photo-1562376552-0d160a2f9fa4?auto=format&fit=crop&w=150&q=80",
  "🍍": "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=150&q=80",
  "🍺": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?auto=format&fit=crop&w=150&q=80",
  "🍊": "https://images.unsplash.com/photo-1558223395-5db6055d72f1?auto=format&fit=crop&w=150&q=80",
  "🫒": "https://images.unsplash.com/photo-1555543453-61b606ea8fb5?auto=format&fit=crop&w=150&q=80",
  "🍞": "https://images.unsplash.com/photo-1584316656345-98516084cb95?auto=format&fit=crop&w=150&q=80",
  "🍹": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=150&q=80",
  "☕": "https://images.unsplash.com/photo-1511920170033-f8396924c648?auto=format&fit=crop&w=150&q=80",
  "🐟": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=150&q=80",
  "🥤": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=150&q=80",
  "🧃": "https://images.unsplash.com/photo-1622543925917-763c34d1a86e?auto=format&fit=crop&w=150&q=80",
  "🥛": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=150&q=80"
}

def replacer(match):
    content = match.group(1)
    if content in emoji_map:
        return f'<div class="item-e"><img src="{emoji_map[content]}" alt="product image" loading="lazy"/></div>'
    return match.group(0) # fallback

new_html = re.sub(r'<div class="item-e">(.*?)</div>', replacer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done replacing emojis!")
