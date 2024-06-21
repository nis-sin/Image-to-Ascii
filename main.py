def pixelToAscii(pixelBrightness: int) -> str:
    ascii = ["@", "#", "%", "?", "*", "+", ";", "."]
    # greyscale value will be used as pixel brightness, values range from 0 to 255
    return ascii[pixelBrightness // 35]

def loopThroughImage(imagePath: str, scale: int) -> list[str]:
    asciiImage = []     # List to store ascii characters from the corresponding pixel brightness
    image = Image.open(imagePath)
    image = image.resize((image.width//scale, image.height//scale))     # Downscale the image
    for i in range(image.height):
        for j in range(image.width):
            pixelBrightness = image.convert("L").getpixel((j,i))      # Convert to greyscale and get pixel greyscale value, https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
            asciiChar = pixelToAscii(pixelBrightness)
            asciiImage.append(asciiChar)
        asciiImage.append("\n")         # Add a newline character to the end of each row of ascii characters
    return asciiImage


def saveAsciiImage(asciiImage: list[str]) -> None:
    with open("ascii_image.txt", "w") as file:
        file.write("".join(asciiImage))             # write the ascii image (the list of ascii characters) to a file. First join the list of ascii characters in the list to a string


def main():
    asciiImage = loopThroughImage("mona_lisa.jpg", 40)
    saveAsciiImage(asciiImage)
            

if __name__ == "__main__":
    from PIL import Image
    main()