from PIL import Image

def encode_image(img, secret_msg):
    binary_secret_msg = ''.join(format(ord(char), '08b') for char in secret_msg) + '00000000'
    data_index = 0
    width, height = img.size

    encoded_img = img.copy()

    for y in range(height):
        for x in range(width):
            pixel = list(encoded_img.getpixel((x, y)))
            for i in range(3):
                if data_index < len(binary_secret_msg):
                    pixel[i] = pixel[i] & 254 | int(binary_secret_msg[data_index])
                    data_index += 1
            encoded_img.putpixel((x, y), tuple(pixel))

            if data_index >= len(binary_secret_msg):
                return encoded_img
            
    return encoded_img

image = Image.open("image.png")
secret_message = "Hello, this is a secret message"
encoded_image = encode_image(image, secret_message)

encoded_image.save("encoded_image.png")

print("Message successfully embedded in the image.")