from rembg import remove
from PIL import Image

input_path = 'avatar-before.png'
output_path = 'avatar-after.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)

print(f"Done! The processed image has been saved as '{output_path}'.")

Image.open(output_path).show()