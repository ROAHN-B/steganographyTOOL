import cv2
import numpy as np
from PIL import Image

# Convert data to binary format
def data2binary(data):
    if isinstance(data, str):
        return ''.join(format(ord(i), '08b') for i in data)
    elif isinstance(data, (bytes, np.ndarray)):
        return [format(i, '08b') for i in data]
    return None

# Hide data in the given image
def hidedata(img, data):
    data += "$$"  # Secret key
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

    # Iterate pixels from image and update pixel values
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index], 2)  # Update red channel
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index], 2)  # Update green channel
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index], 2)  # Update blue channel
                d_index += 1
            if d_index >= len_data:
                break
    return img

def encode():
    img_name = input("\nEnter image name: ")
    image = cv2.imread(img_name)
    if image is None:
        print("Error: Image not found.")
        return
    data = input("\nEnter message: ")
    if len(data) == 0:
        raise ValueError("Empty data")
    enc_img = input("\nEnter encoded image name: ")
    enc_data = hidedata(image, data)
    cv2.imwrite(enc_img, enc_data)

# Decoding
def find_data(img):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break
    return readable_data[:-2]

def decode():
    img_name = input("\nEnter image name: ")
    image = cv2.imread(img_name)
    if image is None:
        print("Error: Image not found.")
        return
    msg = find_data(image)
    return msg

def steganography():
    while True:
        print('''\nImage Steganography
        1. Encode
        2. Decode''')
        u_in = int(input("\nEnter your choice: "))
        if u_in == 1:
            encode()
        elif u_in == 2:
            ans = decode()
            print("\nYour message: " + ans)
        else:
            print("Invalid choice. Please select 1 or 2.")
        
        cont = int(input("\nEnter 1 to continue, otherwise 0: "))
        if cont == 0:
            break

steganography()