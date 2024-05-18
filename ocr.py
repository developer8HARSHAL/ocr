import pytesseract
from pytesseract import Output
import cv2

myconfig = r"--psm 11 --oem 3"

img = cv2.imread("text3.jpeg")
height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
amount_boxes = len(data['text'])

for i in range(amount_boxes):
    if int(data['conf'][i]) > 80:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
