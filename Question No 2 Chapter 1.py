import time
from PIL import Image

# Generate a number
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# Ensure the generated number is odd
if generated_number % 2 == 0:
    generated_number += 10

# Load the original image
original_image = Image.open("/chapter1.jpg")
pixels = original_image.load()

# Create a new image with converted pixels
new_image = Image.new("RGB", original_image.size)
new_pixels = new_image.load()

# Iterate through each pixel in the original image
for i in range(original_image.width):
    for j in range(original_image.height):
        # Extract original pixel values
        r, g, b = pixels[i, j]

        # Add the generated number to each color channel
        r_new = min(255, r + generated_number)
        g_new = min(255, g + generated_number)
        b_new = min(255, b + generated_number)

        # Update the pixel in the new image
        new_pixels[i, j] = (r_new, g_new, b_new)

# Save the new image
new_image.save("chapter1out.png")

# Calculate the sum of red pixel values in the new image
red_sum = sum(p[0] for p in new_image.getdata())
print(red_sum)