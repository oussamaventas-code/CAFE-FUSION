# 📋 Proyecto: Fusión Café Bar — Punto de Control

## Estado actual
- **Versión**: v3 — Web con carta real + identidad de marca correcta
- **Fecha**: 2026-05-01
- **Archivo principal**: `index.html`

---

## Cliente
**Fusión Café Bar**
- Tipo: Cafetería / Restaurante latinoamericano
- Dirección: C. Infanta Elena, 1, bajo 4 — 30500 Molina de Segura, Murcia
- WhatsApp / Pedidos: **627 579 429** (número del propio negocio — usar este)
- Teléfono alternativo (Google): 601 67 90 67
- Horario: Lunes–Domingo desde las 10:00 h
- Rating: ⭐ 5,0 / 5 — 20 reseñas en Google Maps

---

## Identidad de marca (extraída del logo y menú real)

### Colores
```
--linen:  #eae0ca    /* fondo principal (lino cálido) */
--light:  #f5eedf    /* secciones más claras */
--bark:   #2c1405    /* texto principal (marrón oscuro espresso) */
--moss:   #1e4d1a    /* verde bosque (nombres de ítems, "café bar") */
--terra:  #b85c3a    /* terracota (círculo del logo, acentos) */
--warm:   #d4821a    /* ámbar/dorado (CTAs, highlights) */
--white:  #fdfaf4    /* blanco crema (tarjetas, fondo claro) */
```

### Tipografía (Google Fonts)
- `Oswald 700` → Títulos de categoría (ALL CAPS bold condensed, estilo igual que el menú)
- `Playfair Display 700 italic` → Taglines elegantes
- `Inter 300/400/500` → Cuerpo, descripciones, precios

### Logo
- Círculo terracota (#b85c3a) con anillo oscuro (#3d1e0a)
- Planta con 5 hojas en verde bosque (#1e4d1a)
- "FUSION" en marrón muy bold / "café bar" en verde
- Recreado como SVG inline en la web

---

## Carta completa (extraída de imágenes del cliente)

### ☕ Cafés e Infusiones
| Producto | Descripción | Precio |
|---|---|---|
| Café con Leche | Tradicional | 1,80 € |
| Asiático | Especialidad local | 3,50 € |
| Capuchino | Con espuma de leche | 2,50 € |
| Infusiones Especiales | — | 2,40 € |

### 🍺 Cervezas y Refrescos
| Producto | Descripción | Precio |
|---|---|---|
| Cerveza de Grifo | — | 2,20 € |
| Tercio Heineken | — | 3,00 € |
| Refrescos | Coca-Cola, Fanta, Aquarius | 2,50 € |
| Zumo de Naranja | Recién exprimido | 2,20 € |

### 🥤 Bebidas Frescas
| Producto | Descripción | Precio |
|---|---|---|
| Smoothie Tropical | Piña, papaya, fresa, kiwi | 5,50 € |
| Frappé de Caramelo | Café, caramelo, crema | 5,90 € |
| Papelón con Limón | Azúcar de caña y limón | 3,00 € |
| Capuchino Frío | Café de especialidad | 2,50 € |

### 🍸 Cócteles
| Producto | Descripción | Precio |
|---|---|---|
| Mojito | Ron blanco, lima, menta, soda | 7,00 € |
| Piña Colada | Ron, piña, coco | 4,00 € |
| Margarita | Tequila, Triple Sec, lima | 7,50 € |
| Daiquiri | Ron blanco, fresa o limón | 7,00 € |

### 🫓 Cachapas ⭐ Estrella de la carta
| Producto | Descripción | Precio |
|---|---|---|
| Con Queso | Doble porción de queso de mano | 9,90 € |
| Pabellón | Caraotas, carne, plátano, queso | 13,90 € |
| Mechada | Carne mechada y queso | 11,90 € |
| Reina Pepiada | Pollo, aguacate, queso | 11,90 € |

### 🌮 Quesadillas
| Producto | Descripción | Precio |
|---|---|---|
| Queso | Mozzarella derretida | 5,90 € |
| Carne y Queso | Carne mechada, mozzarella | 7,20 € |
| Pollo y Queso | Pollo mechado, mozzarella | 7,20 € |

### 🍟 Aperitivos
| Producto | Descripción | Precio |
|---|---|---|
| Tequeños de Queso | 5 piezas de masa dorada | 6,40 € |
| Bocados de Patacón | Copas de plátano con rellenos | 5,80 € |
| Tapas | Ensaladilla rusa o Almendras con salchicha | 5,00 € |

### 🍮 Postres
| Producto | Descripción | Precio |
|---|---|---|
| Crepe de Oreo | Sirope de Oreo, nata montada | 6,50 € |
| Crepe de Pistacho | Nata y topping de pistacho | 7,00 € |
| Waffle de Dulce de Leche | Dulce de leche, nata | 5,00 € |
| Waffle de Plátano | Plátano, Nutella, nata | 5,50 € |

> ⚠️ Las arepas aparecen en reseñas de Google pero no en las imágenes de carta proporcionadas.
> Añadir nota "Pregunta por nuestra carta de arepas" o solicitar imágenes al cliente.

---

## Stack técnico
- **HTML5** — archivo único `index.html` (sin framework)
- **CSS3** — variables CSS, grid, flexbox, animaciones
- **GSAP 3.12.5** — CDN jsdelivr
  - `ScrollTrigger` — reveals en scroll
  - `ScrollTrigger.batch` — stagger de cards
  - Tweens manuales — cursor, hero, tab indicator
- **Sin dependencias de servidor** — abre directo en navegador

---

## Estructura de archivos
```
CAFERETIA 2/
├── index.html        ← Página principal (web completa)
└── CLAUDE.md         ← Este archivo de memoria del proyecto
```

---

## Historial de versiones
| Versión | Fecha | Cambios |
|---|---|---|
| v1 | 2026-05-01 | Primera web con datos de Google Maps, menú inventado |
| v2 | 2026-05-01 | Reescritura completa: cursor custom, hero dramático, scroll horizontal pinneado, reviews reales |
| v3 | 2026-05-01 | **Actual** — Identidad de marca real (colores del logo), carta completa de imágenes del cliente |

---

## Próximos pasos posibles
- [ ] Añadir sección de arepas cuando el cliente proporcione datos
- [ ] Integrar fotos reales del local y platos
- [ ] Añadir Google Maps embed real
- [ ] Versión multiidioma (español + inglés)
- [ ] Formulario de reservas online
- [ ] Integrar pedidos WhatsApp con mensaje pre-escrito por producto
- [ ] Optimización SEO local (schema markup LocalBusiness)
- [ ] Publicar en dominio (dominio sugerido: fusioncafebar.es)

---

## Notas de agente
- El número de WhatsApp del negocio es **627 579 429** (no el de Google)
- Los colores vienen del logo real (imágenes proporcionadas por el cliente)
- Las animaciones GSAP están en vanilla JS al final del HTML
- El cursor personalizado solo se activa en desktop (pointer: fine)
- Todos los precios usan coma decimal (formato español): 1,80€
