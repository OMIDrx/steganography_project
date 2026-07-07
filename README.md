# Steganography App

A lightweight web application built with **Streamlit** that allows users to hide secret messages inside images and reveal them later using **LSB (Least Significant Bit) steganography**.

## Features

- Hide text inside PNG or JPG images
- Reveal hidden messages from PNG images
- Simple and intuitive interface
- Random output filename generation
- Built with Streamlit for quick deployment

## Technologies

- Python
- Streamlit
- Stegano
- Pillow (PIL)

## Project Structure

```
steganography-app/
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/steganography-app.git
```

Move into the project directory:

```bash
cd steganography-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

### Hide Text

1. Upload an image (.png or .jpg)
2. Enter your secret message
3. Click **Save Final Image**
4. A new image containing the hidden message will be generated.

### Reveal Text

1. Upload the encoded PNG image.
2. Click **Reveal**.
3. The hidden message will be displayed.

## Preview

Add screenshots of:

- Home page
- Hide Text page
- Reveal Text page

## Future Improvements

- Download button for generated images
- Password-protected encryption
- Drag & Drop image upload
- Better error handling
- Support for larger files

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
