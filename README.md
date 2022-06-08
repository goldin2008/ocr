# ocr
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