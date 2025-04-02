import qrcode
import qrcode.constants

def generate_qr(text, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__== "__main__":
    text = input("Masukkan teks untuk dikonversi ke QR Code: ")
    generate_qr(text)