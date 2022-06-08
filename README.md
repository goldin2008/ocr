# ocr
# PaddleOCR Quick Start
> https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/environment_en.md

> https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/quickstart_en.md

## 1. Installation

<a name="11-install-paddlepaddle"></a>

### 1.1 Install PaddlePaddle

> If you do not have a Python environment, please refer to [Environment Preparation](./environment_en.md).

- If you have CUDA 9 or CUDA 10 installed on your machine, please run the following command to install

  ```bash
  python3 -m pip install paddlepaddle-gpu
  ```

- If you have no available GPU on your machine, please run the following command to install the CPU version

  ```bash
  python3 -m pip install paddlepaddle
  ```

For more software version requirements, please refer to the instructions in [Installation Document](https://www.paddlepaddle.org.cn/install/quick) for operation.

<a name="12-install-paddleocr-whl-package"></a>

### 1.2 Install PaddleOCR Whl Package

```bash
pip install "paddleocr>=2.0.1" # Recommend to use version 2.0.1+
```


## 2. Easy-to-Use

<a name="21-use-by-command-line"></a>

### 2.1 Use by Command Line

PaddleOCR provides a series of test images, click [here](https://paddleocr.bj.bcebos.com/dygraph_v2.1/ppocr_img.zip) to download, and then switch to the corresponding directory in the terminal

```bash
cd /path/to/ppocr_img
```

If you do not use the provided test image, you can replace the following `--image_dir` parameter with the corresponding test image path

<a name="211-english-and-chinese-model"></a>

#### 2.1.1 Chinese and English Model
* Detection, direction classification and recognition: set the parameter`--use_gpu false` to disable the gpu device

  ```bash
  paddleocr --image_dir ./imgs_en/img_12.jpg --use_angle_cls true --lang en --use_gpu false
  ```

  Output will be a list, each item contains bounding box, text and recognition confidence

```bash
[2022/06/07 20:59:20] ppocr INFO: ********** ./imgs_en/img_12.jpg **********
[2022/06/07 20:59:20] ppocr DEBUG: dt_boxes num : 11, elapse : 0.35411715507507324
[2022/06/07 20:59:20] ppocr DEBUG: cls num  : 11, elapse : 0.09706902503967285
[2022/06/07 20:59:23] ppocr DEBUG: rec_res num  : 11, elapse : 2.3295300006866455
[2022/06/07 20:59:23] ppocr INFO: [[[441.0, 174.0], [1166.0, 176.0], [1165.0, 222.0], [441.0, 221.0]], ('ACKNOWLEDGEMENTS', 0.9971134662628174)]
[2022/06/07 20:59:23] ppocr INFO: [[[403.0, 346.0], [1204.0, 348.0], [1204.0, 384.0], [402.0, 383.0]], ('We would like to thank all the designers and', 0.9761400818824768)]
[2022/06/07 20:59:23] ppocr INFO: [[[403.0, 396.0], [1204.0, 398.0], [1204.0, 434.0], [402.0, 433.0]], ('contributors who have been involved in the', 0.9791957139968872)]
[2022/06/07 20:59:23] ppocr INFO: [[[399.0, 446.0], [1207.0, 443.0], [1208.0, 484.0], [399.0, 488.0]], ('production of this book; their contributions', 0.9889591336250305)]
[2022/06/07 20:59:23] ppocr INFO: [[[401.0, 500.0], [1208.0, 500.0], [1208.0, 534.0], [401.0, 534.0]], ('have been indispensable to its creation. We', 0.9555092453956604)]
[2022/06/07 20:59:23] ppocr INFO: [[[399.0, 550.0], [1209.0, 548.0], [1209.0, 583.0], [399.0, 584.0]], ('would also like to express our gratitude to all', 0.9905332922935486)]
[2022/06/07 20:59:23] ppocr INFO: [[[399.0, 600.0], [1207.0, 598.0], [1208.0, 634.0], [399.0, 636.0]], ('the producers for their invaluable opinions', 0.9781714081764221)]
[2022/06/07 20:59:23] ppocr INFO: [[[399.0, 648.0], [1207.0, 646.0], [1208.0, 686.0], [399.0, 688.0]], ('and assistance throughout this project. And to', 0.9883645176887512)]
[2022/06/07 20:59:23] ppocr INFO: [[[399.0, 702.0], [1209.0, 698.0], [1209.0, 734.0], [399.0, 738.0]], ('the many others whose names are not credited', 0.9579494595527649)]
[2022/06/07 20:59:23] ppocr INFO: [[[399.0, 750.0], [1211.0, 750.0], [1211.0, 789.0], [399.0, 789.0]], ('but have made specific input in this book, we', 0.9702867865562439)]
[2022/06/07 20:59:23] ppocr INFO: [[[397.0, 802.0], [1090.0, 800.0], [1090.0, 839.0], [397.0, 841.0]], ('thank you for your continuous support.', 0.9978145956993103)]
```

* Only detection: set `--rec` to `false`

  ```bash
  paddleocr --image_dir ./imgs_en/img_12.jpg --rec false
  ```

  Output will be a list, each item only contains bounding box

```bash
[2022/06/07 21:00:50] ppocr INFO: **********./imgs_en/img_12.jpg**********
[2022/06/07 21:00:50] ppocr INFO: [[397.0, 802.0], [1092.0, 802.0], [1092.0, 841.0], [397.0, 841.0]]
[2022/06/07 21:00:50] ppocr INFO: [[397.0, 750.0], [1211.0, 750.0], [1211.0, 789.0], [397.0, 789.0]]
[2022/06/07 21:00:50] ppocr INFO: [[397.0, 702.0], [1209.0, 698.0], [1209.0, 734.0], [397.0, 738.0]]
[2022/06/07 21:00:50] ppocr INFO: [[399.0, 650.0], [1207.0, 646.0], [1208.0, 686.0], [399.0, 690.0]]
[2022/06/07 21:00:50] ppocr INFO: [[399.0, 600.0], [1207.0, 598.0], [1208.0, 634.0], [399.0, 636.0]]
[2022/06/07 21:00:50] ppocr INFO: [[401.0, 550.0], [1209.0, 550.0], [1209.0, 584.0], [401.0, 584.0]]
[2022/06/07 21:00:50] ppocr INFO: [[401.0, 500.0], [1208.0, 500.0], [1208.0, 534.0], [401.0, 534.0]]
[2022/06/07 21:00:50] ppocr INFO: [[399.0, 446.0], [1206.0, 443.0], [1206.0, 484.0], [399.0, 488.0]]
[2022/06/07 21:00:50] ppocr INFO: [[401.0, 396.0], [1206.0, 396.0], [1206.0, 436.0], [401.0, 436.0]]
[2022/06/07 21:00:50] ppocr INFO: [[401.0, 345.0], [1204.0, 346.0], [1204.0, 386.0], [401.0, 384.0]]
[2022/06/07 21:00:50] ppocr INFO: [[439.0, 172.0], [1166.0, 174.0], [1165.0, 222.0], [439.0, 221.0]]
```

* Only recognition: set `--det` to `false`

  ```bash
  paddleocr --image_dir ./imgs_words/en/word_1.png --det false --lang en
  ```

  Output will be a list, each item contains text and recognition confidence

  ```bash
  [2022/06/07 21:07:32] ppocr INFO: ********** ./imgs_words/en/word_1.png **********
  [2022/06/07 21:07:32] ppocr INFO: ('JOINT', 0.9981608390808105)
  ```

#### 2.1.2 Multi-language Model

PaddleOCR currently supports 80 languages, which can be switched by modifying the `--lang` parameter.

``` bash
paddleocr --image_dir ./imgs_en/254.jpg --lang=en
```

```text
[2022/06/07 21:20:25] ppocr INFO: **********./imgs_en/254.jpg**********
[2022/06/07 21:20:25] ppocr DEBUG: dt_boxes num : 28, elapse : 0.40782690048217773
[2022/06/07 21:20:28] ppocr DEBUG: rec_res num  : 28, elapse : 2.5506019592285156
[2022/06/07 21:20:28] ppocr INFO: [[[67.0, 51.0], [327.0, 46.0], [327.0, 74.0], [68.0, 80.0]], ('PHOCAPITAL', 0.9944714307785034)]
[2022/06/07 21:20:28] ppocr INFO: [[[72.0, 92.0], [453.0, 84.0], [454.0, 114.0], [73.0, 122.0]], ('107 State Street', 0.9744491577148438)]
[2022/06/07 21:20:28] ppocr INFO: [[[69.0, 135.0], [501.0, 125.0], [501.0, 156.0], [70.0, 165.0]], ('Montpelier Vermont', 0.9357033967971802)]
[2022/06/07 21:20:28] ppocr INFO: [[[71.0, 176.0], [364.0, 171.0], [364.0, 201.0], [72.0, 206.0]], ('802 225 6183', 0.9168080687522888)]
[2022/06/07 21:20:28] ppocr INFO: [[[74.0, 302.0], [150.0, 299.0], [151.0, 333.0], [75.0, 336.0]], ('REG', 0.9945926666259766)]
[2022/06/07 21:20:28] ppocr INFO: [[[198.0, 300.0], [651.0, 285.0], [652.0, 315.0], [199.0, 330.0]], ('07-24-2017 06:59 PM', 0.9437682628631592)]
[2022/06/07 21:20:28] ppocr INFO: [[[510.0, 331.0], [651.0, 325.0], [653.0, 357.0], [511.0, 362.0]], ('045555', 0.9959450364112854)]
[2022/06/07 21:20:28] ppocr INFO: [[[537.0, 370.0], [588.0, 370.0], [588.0, 402.0], [537.0, 402.0]], ('CT', 0.9880505800247192)]
[2022/06/07 21:20:28] ppocr INFO: [[[397.0, 457.0], [442.0, 457.0], [442.0, 491.0], [397.0, 491.0]], ('T1', 0.993397057056427)]
[2022/06/07 21:20:28] ppocr INFO: [[[539.0, 452.0], [655.0, 447.0], [657.0, 480.0], [540.0, 485.0]], ('$7.95', 0.9911705255508423)]
[2022/06/07 21:20:28] ppocr INFO: [[[111.0, 470.0], [252.0, 464.0], [253.0, 496.0], [112.0, 502.0]], ('1 F00D', 0.8825616836547852)]
[2022/06/07 21:20:28] ppocr INFO: [[[399.0, 498.0], [443.0, 498.0], [443.0, 532.0], [399.0, 532.0]], ('T1', 0.9917992353439331)]
[2022/06/07 21:20:28] ppocr INFO: [[[541.0, 494.0], [656.0, 489.0], [658.0, 521.0], [542.0, 526.0]], ('$3.95', 0.9907434582710266)]
[2022/06/07 21:20:28] ppocr INFO: [[[111.0, 511.0], [254.0, 505.0], [255.0, 536.0], [112.0, 542.0]], ('1F00D', 0.9695411920547485)]
[2022/06/07 21:20:28] ppocr INFO: [[[399.0, 539.0], [445.0, 539.0], [445.0, 572.0], [399.0, 572.0]], ('T1', 0.9911445379257202)]
[2022/06/07 21:20:28] ppocr INFO: [[[541.0, 534.0], [658.0, 529.0], [660.0, 562.0], [542.0, 566.0]], ('$9.50', 0.9681172370910645)]
[2022/06/07 21:20:28] ppocr INFO: [[[115.0, 551.0], [255.0, 546.0], [256.0, 578.0], [116.0, 583.0]], ('1F00D', 0.9725920557975769)]
[2022/06/07 21:20:28] ppocr INFO: [[[396.0, 577.0], [495.0, 575.0], [496.0, 614.0], [397.0, 617.0]], ('3 No', 0.9465218782424927)]
[2022/06/07 21:20:28] ppocr INFO: [[[521.0, 616.0], [662.0, 609.0], [664.0, 644.0], [522.0, 651.0]], ('$21.40', 0.9275484085083008)]
[2022/06/07 21:20:28] ppocr INFO: [[[165.0, 629.0], [235.0, 629.0], [235.0, 664.0], [165.0, 664.0]], ('TA1', 0.9969971776008606)]
[2022/06/07 21:20:28] ppocr INFO: [[[545.0, 657.0], [664.0, 653.0], [666.0, 688.0], [546.0, 692.0]], ('$1.92', 0.9926120042800903)]
[2022/06/07 21:20:28] ppocr INFO: [[[165.0, 672.0], [234.0, 669.0], [235.0, 704.0], [166.0, 707.0]], ('TX1', 0.9829854369163513)]
[2022/06/07 21:20:28] ppocr INFO: [[[167.0, 714.0], [216.0, 714.0], [216.0, 751.0], [167.0, 751.0]], ('TL', 0.9964312314987183)]
[2022/06/07 21:20:28] ppocr INFO: [[[383.0, 706.0], [660.0, 695.0], [662.0, 730.0], [385.0, 740.0]], ('$23.32', 0.9463890194892883)]
[2022/06/07 21:20:28] ppocr INFO: [[[527.0, 742.0], [667.0, 737.0], [669.0, 771.0], [528.0, 777.0]], ('$23.32', 0.9761694073677063)]
[2022/06/07 21:20:28] ppocr INFO: [[[165.0, 757.0], [265.0, 755.0], [266.0, 790.0], [166.0, 793.0]], ('CASH', 0.9979817867279053)]
[2022/06/07 21:20:28] ppocr INFO: [[[99.0, 848.0], [313.0, 837.0], [315.0, 868.0], [101.0, 879.0]], ('THANK YOU', 0.9712556004524231)]
[2022/06/07 21:20:28] ppocr INFO: [[[98.0, 889.0], [504.0, 867.0], [506.0, 897.0], [100.0, 919.0]], ('FOR YOUR BUSINESS', 0.9636691808700562)]
```

### 2.2 Use by Code
<a name="221-chinese---english-model-and-multilingual-model"></a>

#### 2.2.1 Chinese & English Model and Multilingual Model

* detection, angle classification and recognition:

```python
from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = './imgs_en/img_12.jpg'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)


# draw result
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
```

Output will be a list, each item contains bounding box, text and recognition confidence

```bash
[[[441.0, 174.0], [1166.0, 176.0], [1165.0, 222.0], [441.0, 221.0]], ('ACKNOWLEDGEMENTS', 0.9971134662628174)]
[[[403.0, 346.0], [1204.0, 348.0], [1204.0, 384.0], [402.0, 383.0]], ('We would like to thank all the designers and', 0.9761400818824768)]
[[[403.0, 396.0], [1204.0, 398.0], [1204.0, 434.0], [402.0, 433.0]], ('contributors who have been involved in the', 0.9791957139968872)]
```