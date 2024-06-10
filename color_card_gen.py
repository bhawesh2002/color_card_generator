import os

def load_template():
    """Load an SVG file and return its content as a string."""
    while True:
        template_index = int(input("Choose a Tempelate(1-3): "))
        if template_index > 0 and template_index <= 3:
            break
    templates = ["card_template_1.svg","card_template_2.svg","card_template_3.svg"]
    template_path = templates[template_index - 1]
    with open(template_path, 'r') as f:
        return f.read()


def save_svg(file_path, svg):
    """Save an SVG string to a file."""
    color_name = file_path.split('_')[0]
    folder_path = os.path.join("extracted", color_name)
    if not os.path.exists(folder_path): # Create the folder if it doesn't exist
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, file_path)
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
    for color_name, shades in color_codes.items(): # Loop through each color
        for shade, code in shades.items(): # Loop through each shade of the color
            modified_svg = svg # Make a copy of the original SVG 
            modified_svg = modified_svg.replace(f'shade',f'{shade}') # Replace the placeholder with the shade
            modified_svg = modified_svg.replace(f'hex_code',f'{code}') # Replace the placeholder with the color code
            save_svg(f'{color_name}_{shade}.svg', modified_svg) # Save the modified SVG to a file


def main():
    print('Loading SVG file...')
    svg = load_template() # Load the SVG file
    print('Creating Color Cards...')
    modify_color(svg,color_codes) # Modify the color of the SVG file
    print('Done!') # Print a message to indicate that the process is complete 

if __name__ == '__main__':
    main()