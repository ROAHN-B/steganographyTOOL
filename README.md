Image Steganography
This project implements a simple image steganography tool using Python. It allows users to hide messages within images and retrieve them later. The hidden messages are encoded in the least significant bits of the image pixels, making it a discreet way to transmit information.

Features
Encode Messages: Hide a text message within an image.
Decode Messages: Retrieve the hidden message from the image.
User -Friendly Interface: Simple command-line interface for easy interaction.
Requirements
Python 3.x
OpenCV (cv2)
NumPy
Pillow (PIL)
You can install the required packages using pip:

bash
Run
Copy code
pip install opencv-python numpy pillow
Usage
Clone the Repository:

bash
Run
Copy code
git clone https://github.com/yourusername/repository-name.git
cd repository-name
Run the Script:

bash
Run
Copy code
python MultipleFiles/main.py
Follow the Prompts:

Choose to encode or decode a message.
For encoding, provide the image name, the message to hide, and the name for the encoded image.
For decoding, provide the image name to retrieve the hidden message.
Example
Encoding:

Input image: input_image.png
Message: Hello, World!
Output image: encoded_image.png
Decoding:

Input image: encoded_image.png
Output: Hello, World!
Code Overview
data2binary(data): Converts data into binary format.
hidedata(img, data): Hides the provided data in the image.
find_data(img): Extracts hidden data from the image.
encode(): Handles the encoding process.
decode(): Handles the decoding process.
steganography(): Main function to run the application.
Contributing
Feel free to contribute to this project by submitting issues or pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
OpenCV for image processing.
NumPy for numerical operations.
Pillow for image handling.
