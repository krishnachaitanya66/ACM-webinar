import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('assets/icons', exist_ok=True)

# Generate high-resolution PNG icons for reliable email rendering across all clients
def create_circle_icon(filename, bg_color, draw_func, size=64):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((2, 2, size - 3, size - 3), fill=bg_color)
    draw_func(draw, size)
    img.save(os.path.join('assets/icons', filename))

# 1. Open Source icon (People / network)
def draw_users(d, s):
    # Head 1
    d.ellipse((s*0.35, s*0.25, s*0.65, s*0.55), fill='white')
    # Shoulders 1
    d.pieslice((s*0.2, s*0.58, s*0.8, s*0.95), 180, 360, fill='white')

create_circle_icon('icon-open-source.png', '#0066cc', draw_users)

# 2. Build Profile (Bar Chart)
def draw_chart(d, s):
    # Bars
    d.rounded_rectangle((s*0.22, s*0.55, s*0.36, s*0.78), radius=3, fill='white')
    d.rounded_rectangle((s*0.43, s*0.35, s*0.57, s*0.78), radius=3, fill='white')
    d.rounded_rectangle((s*0.64, s*0.22, s*0.78, s*0.78), radius=3, fill='white')

create_circle_icon('icon-profile.png', '#0066cc', draw_chart)

# 3. Programs & Opportunities (Lightbulb / Gear)
def draw_bulb(d, s):
    # Bulb circle
    d.ellipse((s*0.32, s*0.22, s*0.68, s*0.58), fill='white')
    d.rectangle((s*0.40, s*0.54, s*0.60, s*0.72), fill='white')
    d.rectangle((s*0.42, s*0.75, s*0.58, s*0.80), fill='white')

create_circle_icon('icon-programs.png', '#0066cc', draw_bulb)

# 4. Build & Earn (Rocket)
def draw_rocket(d, s):
    # Rocket body
    d.polygon([(s*0.5, s*0.18), (s*0.65, s*0.48), (s*0.65, s*0.68), (s*0.35, s*0.68), (s*0.35, s*0.48)], fill='white')
    # Wings
    d.polygon([(s*0.35, s*0.55), (s*0.20, s*0.74), (s*0.35, s*0.74)], fill='white')
    d.polygon([(s*0.65, s*0.55), (s*0.80, s*0.74), (s*0.65, s*0.74)], fill='white')
    # Flame
    d.polygon([(s*0.42, s*0.72), (s*0.5, s*0.84), (s*0.58, s*0.72)], fill='#ffaa00')

create_circle_icon('icon-earn.png', '#0066cc', draw_rocket)

# 5. AI & Modern Engineering (Brain / Network nodes)
def draw_ai(d, s):
    # Center node
    d.ellipse((s*0.42, s*0.42, s*0.58, s*0.58), fill='white')
    # Orbiting nodes
    coords = [(s*0.25, s*0.3), (s*0.75, s*0.3), (s*0.25, s*0.7), (s*0.75, s*0.7), (s*0.5, s*0.18), (s*0.5, s*0.82)]
    for cx, cy in coords:
        d.line([(s*0.5, s*0.5), (cx, cy)], fill='white', width=2)
        d.ellipse((cx-4, cy-4, cx+4, cy+4), fill='white')

create_circle_icon('icon-ai.png', '#0066cc', draw_ai)

# 6. From Idea to Product (Spark / Cube)
def draw_product(d, s):
    d.polygon([(s*0.5, s*0.22), (s*0.78, s*0.38), (s*0.78, s*0.68), (s*0.5, s*0.84), (s*0.22, s*0.68), (s*0.22, s*0.38)], fill='white')
    d.line([(s*0.5, s*0.22), (s*0.5, s*0.84)], fill='#0066cc', width=2)
    d.line([(s*0.5, s*0.53), (s*0.22, s*0.38)], fill='#0066cc', width=2)
    d.line([(s*0.5, s*0.53), (s*0.78, s*0.38)], fill='#0066cc', width=2)

create_circle_icon('icon-product.png', '#0066cc', draw_product)

# Verified badge for speaker
def create_verified_badge():
    s = 40
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((2, 2, s-3, s-3), fill='#0066cc')
    # Checkmark
    d.line([(s*0.28, s*0.52), (s*0.44, s*0.68)], fill='white', width=4)
    d.line([(s*0.44, s*0.68), (s*0.72, s*0.36)], fill='white', width=4)
    img.save('assets/icons/badge-verified.png')

create_verified_badge()

# Calendar, Clock, Pin icons for event details strip
def create_strip_icon(name, draw_fn):
    s = 48
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((2, 2, s-3, s-3), radius=10, fill='#eaf3fb')
    draw_fn(d, s)
    img.save(f'assets/icons/{name}.png')

def draw_cal(d, s):
    d.rounded_rectangle((s*0.25, s*0.25, s*0.75, s*0.75), radius=4, outline='#0066cc', width=3)
    d.line([(s*0.25, s*0.42), (s*0.75, s*0.42)], fill='#0066cc', width=3)
    d.line([(s*0.38, s*0.18), (s*0.38, s*0.28)], fill='#0066cc', width=3)
    d.line([(s*0.62, s*0.18), (s*0.62, s*0.28)], fill='#0066cc', width=3)

def draw_clock(d, s):
    d.ellipse((s*0.22, s*0.22, s*0.78, s*0.78), outline='#0066cc', width=3)
    d.line([(s*0.5, s*0.5), (s*0.5, s*0.32)], fill='#0066cc', width=3)
    d.line([(s*0.5, s*0.5), (s*0.65, s*0.5)], fill='#0066cc', width=3)

def draw_pin(d, s):
    d.ellipse((s*0.32, s*0.24, s*0.68, s*0.60), outline='#0066cc', width=3)
    d.ellipse((s*0.44, s*0.36, s*0.56, s*0.48), fill='#0066cc')
    d.polygon([(s*0.36, s*0.52), (s*0.64, s*0.52), (s*0.5, s*0.78)], fill='#0066cc')

create_strip_icon('icon-calendar', draw_cal)
create_strip_icon('icon-clock', draw_clock)
create_strip_icon('icon-pin', draw_pin)

# Trophy icon for Q&A Recognition
def create_trophy_icon():
    s = 64
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Cup
    d.pieslice((s*0.25, s*0.18, s*0.75, s*0.68), 0, 180, fill='#0066cc')
    # Handles
    d.arc((s*0.15, s*0.20, s*0.35, s*0.45), 90, 270, fill='#0066cc', width=3)
    d.arc((s*0.65, s*0.20, s*0.85, s*0.45), 270, 90, fill='#0066cc', width=3)
    # Stem & Base
    d.rectangle((s*0.46, s*0.58, s*0.54, s*0.72), fill='#0066cc')
    d.rounded_rectangle((s*0.30, s*0.72, s*0.70, s*0.82), radius=3, fill='#0066cc')
    img.save('assets/icons/icon-trophy.png')

create_trophy_icon()

# Agenda list icon
def create_agenda_icon():
    s = 48
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((2, 2, s-3, s-3), radius=10, fill='#0066cc')
    # Page
    d.rounded_rectangle((s*0.26, s*0.20, s*0.74, s*0.80), radius=3, fill='white')
    d.line([(s*0.35, s*0.35), (s*0.65, s*0.35)], fill='#0066cc', width=2)
    d.line([(s*0.35, s*0.48), (s*0.65, s*0.48)], fill='#0066cc', width=2)
    d.line([(s*0.35, s*0.61), (s*0.55, s*0.61)], fill='#0066cc', width=2)
    img.save('assets/icons/icon-agenda.png')

create_agenda_icon()

# Social icons for footer
def create_social_icons():
    # Instagram
    s = 36
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((3, 3, s-4, s-4), radius=8, outline='white', width=2)
    d.ellipse((s*0.32, s*0.32, s*0.68, s*0.68), outline='white', width=2)
    d.ellipse((s*0.70, s*0.25, s*0.76, s*0.31), fill='white')
    img.save('assets/icons/icon-instagram.png')
    
    # LinkedIn
    img2 = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(img2)
    d2.rounded_rectangle((3, 3, s-4, s-4), radius=8, outline='white', width=2)
    # 'in' text representation
    d2.ellipse((s*0.28, s*0.25, s*0.36, s*0.33), fill='white')
    d2.rectangle((s*0.28, s*0.40, s*0.36, s*0.74), fill='white')
    d2.rectangle((s*0.46, s*0.40, s*0.54, s*0.74), fill='white')
    d2.arc((s*0.46, s*0.38, s*0.72, s*0.64), 180, 360, fill='white', width=3)
    d2.rectangle((s*0.64, s*0.51, s*0.72, s*0.74), fill='white')
    img2.save('assets/icons/icon-linkedin.png')

create_social_icons()

print('All PNG icons generated successfully.')
