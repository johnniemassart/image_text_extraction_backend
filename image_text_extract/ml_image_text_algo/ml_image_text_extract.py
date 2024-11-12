import cv2 as cv
import numpy as np
import requests

# img_url = "https://res.cloudinary.com/dllbos3cg/image/upload/v1731359232/image_to_text/lyu9x223uvoxdnclsw2k.png"
# response = requests.get(img_url)
# print(response.content)


def display_img(img):
    return f"from the ml file: {img}"
    # response = requests.get(img)

    # if response.status_code == 200:
    #     img_arr = np.frombuffer(response.content, np.uint8)
    #     img = cv.imdecode(img_arr, cv.IMREAD_COLOR)

    #     cv.imshow("Image", img)
    #     cv.waitKey(0)
    #     cv.destroyAllWindows()
