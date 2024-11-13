import cv2 as cv
import numpy as np
import requests
import pytesseract

# img_url = "https://res.cloudinary.com/dllbos3cg/image/upload/v1731459930/image_to_text/bhrucuhc3zflf9ueoixl.png"
# response = requests.get(img_url)


# if response.status_code == 200:
#     # get img from url
#     img_arr = np.frombuffer(response.content, np.uint8)
#     img = cv.imdecode(img_arr, cv.IMREAD_COLOR)

#     # convert img to gray scale
#     gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

#     # # blur img
#     # blur = cv.GaussianBlur(gray, (7, 7), 0)

#     # threshold img
#     _, result = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV)
#     adaptive_result = cv.adaptiveThreshold(
#         gray,
#         255,
#         cv.ADAPTIVE_THRESH_GAUSSIAN_C,
#         cv.THRESH_BINARY,
#         41,
#         5,
#     )

#     # # kernal
#     # kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 13))

#     # # dilate img
#     # dilate = cv.dilate(adaptive_result, kernel, iterations=2)

#     # # contours
#     # contours = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     # contours = contours[0] if len(contours) == 2 else contours[1]
#     # contours = sorted(contours, key=lambda x: cv.boundingRect(x)[0])

#     # for c in contours:
#     #     x, y, w, h = cv.boundingRect(c)
#     #     bnd_img = cv.rectangle(
#     #         adaptive_result, (x, y), (x + w, y + h), (36, 255, 12), 2
#     #     )

#     # display img
#     # cv.imshow("adaptive img", adaptive_result)
#     # cv.waitKey(0)

#     # pytesseract
#     text = pytesseract.image_to_string(adaptive_result)


def img_response(img):
    # get img from cloudinary url
    response = requests.get(img)

    # confirm valid get request
    if response.status_code == 200:
        # read img that opencv can use
        img_arr = np.frombuffer(response.content, np.uint8)
        img = cv.imdecode(img_arr, cv.IMREAD_COLOR)

        # convert to gray
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

        # adaptive threshold
        adaptive_result = cv.adaptiveThreshold(
            img,
            255,
            cv.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv.THRESH_BINARY,
            41,
            5,
        )

        # pytesseract text
        text = pytesseract.image_to_string(adaptive_result)

    return text
