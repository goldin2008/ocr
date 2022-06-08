import sys
from paddleocr import PaddleOCR, draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
# img_path = './ppocr_img/imgs_en/img_12.jpg'
img_path = './w9.png'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)


# draw result
from PIL import Image
from PIL import ImageFont
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
font = ImageFont.load_default()

# print('boxes: \n', boxes)
# print('txts: \n', txts)
# print('scores: \n', scores)

sys.exit()
im_show = draw_ocr(image, boxes, txts, scores, font_path='./ppocr_img/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('w9-result.jpg')
