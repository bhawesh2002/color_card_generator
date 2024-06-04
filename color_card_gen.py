def load_svg(file_path):
    """Load an SVG file and return its content as a string."""
    with open(file_path, 'r') as f:
        return f.read()


def save_svg(file_path, svg):
    """Save an SVG string to a file."""
    with open(file_path, 'w') as f:
        f.write(svg)

color_codes = {'malachite': {
        '50': '#effef3',
        '100': '#d8ffe5',
        '200': '#b4fecd',
        '300': '#7afba7',
        '400': '#39ef79',
        '500': '#10da57',
        '600': '#06b343',
        '700': '#098c38',
        '800': '#0d6e30',
        '900': '#0d5a2b',
        '950': '#003314',
    },
}

def modify_color(svg,color_codes):
    """Modify the color of an SVG file based on the provided color codes."""
    for color_name, shades in color_codes.items():
        for shade, code in shades.items():
            modified_svg = svg.replace(f'fill="#000000"',f'fill="{code}"')
            save_svg(f'{color_name}_{shade}.svg', modified_svg)

print('Loading SVG file...')
svg = load_svg('color_card.svg')
print('Modifying colors...')
modify_color(svg,color_codes)
print('Done!')