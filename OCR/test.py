import pytesseract
import cv2

import re

image = cv2.imread('bill.png', 0)

# convert it into text
text = (pytesseract.image_to_string(image)).lower()
print(text)

# identify the date

match = re.findall(r'\d+[/.-]\d+[/.-]\d+', text)

st = " "
st = st.join(match)
print(st.split(" ")[0])
