#!fontforge -script 
import fontforge
import psMat  # Import psMat for transformations

# ASCII to Braille dot pattern mapping
ascii_to_brl = [
    0x40, 0x6e, 0x50, 0x7c, 0x6b, 0x69, 0x6f, 0x44, 0x77, 0x7e, 0x61, 0x6c, 0x60, 0x64, 0x68, 0x4c,
    0x74, 0x42, 0x46, 0x52, 0x72, 0x62, 0x56, 0x76, 0x66, 0x54, 0x71, 0x70, 0x63, 0x7f, 0x5c, 0x79,
    0x00, 0x2e, 0x10, 0x3c, 0x2b, 0x29, 0x2f, 0x04, 0x37, 0x3e, 0x21, 0x2c, 0x20, 0x24, 0x28, 0x0c,
    0x34, 0x02, 0x06, 0x12, 0x32, 0x22, 0x16, 0x36, 0x26, 0x14, 0x31, 0x30, 0x23, 0x3f, 0x1c, 0x39,
    0x48, 0x41, 0x43, 0x49, 0x59, 0x51, 0x4b, 0x5b, 0x53, 0x4a, 0x5a, 0x45, 0x47, 0x4d, 0x5d, 0x55,
    0x4f, 0x5f, 0x57, 0x4e, 0x5e, 0x65, 0x67, 0x7a, 0x6d, 0x7d, 0x75, 0x6a, 0x73, 0x7b, 0x58, 0x38,
    0x08, 0x01, 0x03, 0x09, 0x19, 0x11, 0x0b, 0x1b, 0x13, 0x0a, 0x1a, 0x05, 0x07, 0x0d, 0x1d, 0x15,
    0x0f, 0x1f, 0x17, 0x0e, 0x1e, 0x25, 0x27, 0x3a, 0x2d, 0x3d, 0x35, 0x2a, 0x33, 0x3b, 0x18, 0x78,
    0xc0, 0xee, 0xd0, 0xfc, 0xeb, 0xe9, 0xef, 0xc4, 0xf7, 0xfe, 0xe1, 0xec, 0xe0, 0xe4, 0xe8, 0xcc,
    0xf4, 0xc2, 0xc6, 0xd2, 0xf2, 0xe2, 0xd6, 0xf6, 0xe6, 0xd4, 0xf1, 0xf0, 0xe3, 0xff, 0xdc, 0xf9,
    0x80, 0xae, 0x90, 0xbc, 0xab, 0xa9, 0xaf, 0x84, 0xb7, 0xbe, 0xa1, 0xac, 0xa0, 0xa4, 0xa8, 0x8c,
    0xb4, 0x82, 0x86, 0x92, 0xb2, 0xa2, 0x96, 0xb6, 0xa6, 0x94, 0xb1, 0xb0, 0xa3, 0xbf, 0x9c, 0xb9,
    0xc8, 0xc1, 0xc3, 0xc9, 0xd9, 0xd1, 0xcb, 0xdb, 0xd3, 0xca, 0xda, 0xc5, 0xc7, 0xcd, 0xdd, 0xd5,
    0xcf, 0xdf, 0xd7, 0xce, 0xde, 0xe5, 0xe7, 0xfa, 0xed, 0xfd, 0xf5, 0xea, 0xf3, 0xfb, 0xd8, 0xb8,
    0x88, 0x81, 0x83, 0x89, 0x99, 0x91, 0x8b, 0x9b, 0x93, 0x8a, 0x9a, 0x85, 0x87, 0x8d, 0x9d, 0x95,
    0x8f, 0x9f, 0x97, 0x8e, 0x9e, 0xa5, 0xa7, 0xba, 0xad, 0xbd, 0xb5, 0xaa, 0xb3, 0xbb, 0x98, 0xf8
]

# Load the existing font
existing_font = fontforge.open('AtkinsonHyperlegible-Regular.ttf')

# Create a new font based on the existing one
font = fontforge.font()
font.fontname = "asciibraille"
font.fullname = "ASCII Braille Font"
font.familyname = "ASCII Braille"
font.encoding = "UnicodeFull"

# Define the Braille cell dimensions and dot radius
cell_width = 1500
cell_height = cell_width
dot_radius = 180 
dot_distance_x = 600
dot_distance_y = dot_distance_x  # Same distance for x and y

# Function to draw a circle (approximation using cubic Bézier curves)
def draw_circle(pen, cx, cy, r):
    c = 0.552284749831  # This constant is (4/3)*(sqrt(2)-1), for approximating a circle with Bézier curves
    pen.moveTo((cx + r, cy))
    pen.curveTo((cx + r, cy + c*r), (cx + c*r, cy + r), (cx, cy + r))
    pen.curveTo((cx - c*r, cy + r), (cx - r, cy + c*r), (cx - r, cy))
    pen.curveTo((cx - r, cy - c*r), (cx - c*r, cy - r), (cx, cy - r))
    pen.curveTo((cx + c*r, cy - r), (cx + r, cy - c*r), (cx + r, cy))
    pen.closePath()

# Function to draw a Braille cell
# Braille dots layout (for 8-dot Braille):
# 1 4
# 2 5
# 3 6
# 7 8
def draw_braille_cell(pen, dots):
    drop =  -1000 # -2.5*dot_distance_y #-4.0*dot_distance_y
    shift = 0  #0.5*dot_distance_x
    dot_positions = [
        (shift+0, cell_height - dot_distance_y + drop),        # Dot 1
        (shift+0, cell_height - 2 * dot_distance_y + drop),    # Dot 2
        (shift+0, cell_height - 3 * dot_distance_y + drop),    # Dot 3
        (shift+dot_distance_x, cell_height - dot_distance_y + drop),    # Dot 4
        (shift+dot_distance_x, cell_height - 2 * dot_distance_y + drop),# Dot 5
        (shift+dot_distance_x, cell_height - 3 * dot_distance_y + drop),# Dot 6
        (shift+0, cell_height - 4 * dot_distance_y + drop),    # Dot 7
        (shift+dot_distance_x, cell_height - 4 * dot_distance_y + drop) # Dot 8
    ]
    
    for i, position in enumerate(dot_positions):
        if dots & (1 << i):
            x, y = position
            draw_circle(pen, x, y-1*dot_distance_y, dot_radius)

# Create Braille glyphs and overlay them
for ascii_code, dots in enumerate(ascii_to_brl):
    print(f"Processing ASCII code: {ascii_code}")
    glyph = font.createChar(ascii_code)
    glyph.width = cell_width

    # Draw the Braille cell
    pen = glyph.glyphPen()
    draw_braille_cell(pen, dots)
    
    # Overlay the existing glyph if it exists
    if 32 <= ascii_code < 127:
        existing_glyph = existing_font[ascii_code]
        if existing_glyph is not None and existing_glyph.isWorthOutputting():
            temp_svg = f"temp_{ascii_code}.svg"
            existing_glyph.export(temp_svg)
            glyph.importOutlines(temp_svg)
            glyph.transform(psMat.translate(0, 0*cell_height))  # Move up the glyph

# Ensure consistent widths for all glyphs
for glyph in font.glyphs():
    glyph.width = cell_width

# Save the new font in various formats
try:
    #font.os2_panose = (2, 0, 9, 3, 0, 0, 0, 0, 0, 0)
    font.descent = 3000
    font.generate("asciibraille.ttf")
    font.generate("asciibraille.woff")
    font.generate("asciibraille.otf")
    print("Font files generated: asciibraille.ttf, asciibraille.woff, asciibraille.otf")
except Exception as e:
    print(f"Error generating font files: {e}")

