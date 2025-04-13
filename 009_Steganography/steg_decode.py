# =============================================
#  Entry Level ID
# =============================================

from PIL import Image

def decode_image(img):
    binary_secret_msg = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):
                binary_secret_msg += str(pixel[i] & 1)

    chars = [binary_secret_msg[i:i+8] for i in range(0, len(binary_secret_msg), 8)]

    secret_msg = ""
    for char in chars:
        if char == "00000000":
            break
        secret_msg += chr(int(char, 2))

    return secret_msg

encoded_image = Image.open("encoded_image.png")
decoded_message = decode_image(encoded_image)

print("Decoded message:", decoded_message)