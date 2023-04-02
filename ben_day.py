from PIL import Image, ImageDraw

# Load the input image
input_image = Image.open("lenna.png")

# Define the dot size and spacing
dot_size = 1
dot_spacing = 6

# Convert the input image to grayscale
input_image = input_image.convert("L")

# Create a new image for the Ben Day dots
output_image = Image.new("RGB", input_image.size, (255, 255, 255))

# Create a drawing object for the output image
draw = ImageDraw.Draw(output_image)

# Loop over each pixel in the input image
for x in range(0, input_image.width, dot_spacing):
    for y in range(0, input_image.height, dot_spacing):
        # Get the pixel value at the current location
        pixel_value = input_image.getpixel((x, y))

        # Determine if a black dot should be drawn based on the pixel value
        if pixel_value < 128:
            # Draw a filled circle at the current location
            draw.ellipse([(x - dot_size, y - dot_size), (x + dot_size, y + dot_size)], fill=(0, 0, 0))

# Save the output image
output_image.save("output_image.png")
