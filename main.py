import cv2
import numpy as np

# conversion data to binary format
def data2binary(data):
    if isinstance(data, str):
        return ''.join(format(ord(i), '08b') for i in data)
    elif isinstance(data, (bytes, np.ndarray)):
        return [format(i, '08b') for i in data]
    return None

# data hiding
def hidedata(img, data):
    data += "$$"  # Secret key to indicate end of message
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

    # Iterate pixels from image and update pixel values
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index], 2)  # red channel
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index], 2)  # green channel
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index], 2)  # blue channel
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
    print(f"Encoded image saved as: {enc_img}")

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
        if readable_data[-2:] == "$$":  # Check for end of message
            break
    return readable_data[:-2]  # Remove the delimiter

def decode():
    img_name = input("\nEnter image name: ")
    image = cv2.imread(img_name)
    if image is None:
        print("Error: Image not found.")
        return None  # Return None if the image is not found
    msg = find_data(image)
    return msg  # Return the decoded message

def steganography():
    while True:
        print('''\nImage Steganography
        1. Encode
        2. Decode''')
        try:
            u_in = int(input("\nEnter your choice: "))
            if u_in == 1:
                encode()
            elif u_in == 2:
                ans = decode()
                if ans is not None:  # Check if a message was returned
                    print("\nYour message: " + ans)
                else:
                    print("\nNo message found or an error occurred.")
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        cont = input("\nEnter 1 to continue, otherwise 0: ")
        if cont != '1':
            break


if __name__ == "__main__":
    steganography()
