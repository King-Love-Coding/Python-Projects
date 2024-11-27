import qrcode
from PIL import Image


data = "https://Youtube.com"  # put the data you want to make QRCode for


qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box
    border=4,  # Thickness of the border
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')   # Image Create

img.show()        # Image Display


save_option = input("Do you want to save the QR code? (yes/no): ").lower()

if save_option == 'yes':
    # Ask for the desired file name
    file_name = input("Enter the file name (without extension): ") + ".png"

    # Save the image with the given file name
    img.save(file_name)
    print(f"QR code saved as {file_name}")
else:
    print("QR code was not saved.")
