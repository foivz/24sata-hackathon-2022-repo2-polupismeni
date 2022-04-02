import pytesseract
import cv2
import re
import PIL.Image as Image

# IMPORTANT, if this returns an error treba
# TESSDATA_PREFIX env var settat na /home/$USER/snap/tesseract/common/
def get_text_from_image(image):
    # convert it into text
    image = Image.open(image)
    text = (pytesseract.image_to_string(image, lang="hrv")).lower()

    # identify the date
    match = re.findall(r'\d+[/.-]\d+[/.-]\d+', text)
    matches = " "
    matches = matches.join(match)
    date = matches.split(" ")[0]

    # identify the ammount
    match = re.findall(r'\d+,\d+', text)
    matches = " "
    matches = matches.join(match)
    ammount = matches.split(" ")[0]

    # identify the name
    match = re.findall(r'badminton', text)
    matches = " "
    matches = matches.join(match)
    name = matches.split(" ")[0]
    return name, ammount, date


if __name__ == '__main__':
    image = cv2.imread('bill.png', 0)
    get_text_from_image(image)
