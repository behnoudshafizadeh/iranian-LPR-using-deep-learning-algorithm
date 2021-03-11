# LP-Recognition-using-deep-learning-algorithm
License-plate(LP) recognition using YOLO-V3

## Discription
> in this project,in summary,we use two end-end deep neural netwroksin the first phase we use and YOLO-V3 for detecting possible license-plates and after detecting them and getting their boundingbox coordinates ,we croped them (each LP) as single image and was forwarded to seconde YOLO-V3 for detecting possible Characters,in first phase for detecting LP,we achieved 0.96 accuracy in training,and in Character Recognition phase we get 0.86 accuracy.

> ![Capture1](https://user-images.githubusercontent.com/53394692/110437818-05442300-80cb-11eb-82e2-2c9efeaffc5f.PNG)

## DATASET
> in this project,fist I captured images dataset using mobile phone cameras with different resolution quality such as (Samsung A5/A50,LG,Apple iphone5) in different conditions such as (illumination,contrast,angle,distance from camera,weather condition such as(rainy,snowy,foggy,...)) by walking in road,highway or high speed cars in fereydounkenar and tehran city.i approximately provided ~7000 images for this project the summary of our result is documented in this github repo.in below you see our compact model architecture:

|                         dataset                                       | 
| --------------------------------------------------------------------- | 
| ![capture3](https://user-images.githubusercontent.com/53394692/110442347-fca21b80-80cf-11eb-80e4-a4447fe526e4.PNG) | 


## Preprocess
> for preparing image dataset for training phase,i labeled my images helping by [Make Sense](https://www.makesense.ai/) online website,with easy tools i labeled my `Vehicle`  and saved their bounding box coordinates in `.txt` files,i downloaded them from website,so each image in my dataset had one `.txt` label.with compelet detailes,we will explain this procedure in another `repo` in my github.furthermore,i augmented my orginal dataset in 5 conditions (foggy,rainy,snowy,darken,brighten) because of getting better accuracy in training phase and better learning in different weather conditions.all of all,my data set was increased to ~40000 images approximately.in below you can see this process:

|                         augmented-dataset                                       | 
| --------------------------------------------------------------------- | 
| ![capture2](https://user-images.githubusercontent.com/53394692/110441840-738ae480-80cf-11eb-8ffb-cbdc2ef007a7.PNG) | 


 
## training procedure
* for LP recognition phase,you must set a few files,so follow below instructions:

  * 1. put `.cfg` files related to YOLO-V3 of LP Recognition `yolov3-1cls.cfg` and Character Recognition `yolov3-1clstochar.cfg` in `cfg` directory,for getting more information about `.cfg` file,follow this [link](https://medium.com/analytics-vidhya/custom-object-detection-with-yolov3-8f72fe8ced79) about configuring YOLOV3 for your object detection task.
  
  * 2. put your dataset images and labels in `training/images` directory `training/labels` directory.
  
  * 3. set label names in files `object.names` and `objecttochar.names`  in `training` directory.
  
  * 4. set splitted dataset of train and test iamges in format of `.txt` as `train.txt` and `test.txt` in `training` directory.for splitting data set run to codes as `train_test.py` and  `train_testtochar.py`,for getting better information go to this [link](https://medium.com/analytics-vidhya/custom-object-detection-with-yolov3-8f72fe8ced79)
  
  * 5. set pathes of `train.txt`,`test.txt` ,`object.names` and `objecttochar.names` for  YOLO-V3 as `trainer.data` and `trainertochar.data` in `training` directory. 
   
  * 6. put pretrained of YOLO-V3 weights as `yolov3.weights` in `weights` directory.due to large size of weight,i dont put it in github directory,if you would like to get it ,please contact with me via my email address. 

* after confuiguring,then you run `train.py` below command for training in `YoloV3-Custom-Object-Detection-master` directory:
```
for LP Recognition training:
python3 train.py --epochs 110 --data training/trainer.data --cfg training/yolov3-1cls.cfg --batch 8 --accum 1

for Character Recognition training:
python3 train.py --epochs 110 --data training/trainertochar.data --cfg training/yolov3-1clstochar.cfg --batch 8 --accum 1
```
* after ending programs,you must run these instructions for converting `pytorch` format to `darknet` format,after that the `converted.weights` is build in root directory.due to large size of weight,i dont put it in github directory,if you would like to get it ,please contact with me via my email address. 

```
for LP:
python3  -c "from models import *; convert('training/yolov3-1cls.cfg', 'weights/best.pt')"

for Character:
python3  -c "from models import *; convert('training/yolov3-1clstochar.cfg', 'weights/best.pt')"

```

## Graph Results
> after running `train.py`,you can see the different measures for obeject detection in diiferent graphs as `results.png` in root directory.

| Train.py (for LP) |
| ------------- |
| ![newcapture1](https://user-images.githubusercontent.com/53394692/110774811-7292b800-8273-11eb-8103-bfb5e660e042.PNG) |

| Train.py (for Character) |
| ------------- |
| ![newcapture](https://user-images.githubusercontent.com/53394692/110774582-352e2a80-8273-11eb-9a21-f0ee58a248d2.PNG) |

## testing models
> in the last step for testing our models,must run below instruction:
```
python3 detect.py --source test.png --weights converted.weights --cfg training/yolov3-123clstomodels.cfg --names training/objecttomodels.names --img-size 416
```
> after running that your output was set in `output` directory in root path.see instances of outputs below:

|    output (Vehicle Recognition)  |                   
| -------------------------------- |  
| ![Capture6](https://user-images.githubusercontent.com/53394692/110754827-7ca9bc00-825d-11eb-8bd1-118ef8f97733.PNG) |
 


## LICENSE
> this project was done by me `behnoud shafizadeh` and my co-worker `navid pourhadi` in the kharazmi university lab,supervised by `DR.Farshad Eshghi` and `DR.Manoochehr KelarEstaghi`,so the full source of code and dataset in this project are out authority and relatede to `kharazmi university of tehran`,so if you would like to contiribute with our group and access to out document,please contact with our emails : `behnud.shafizadeh@gmail.com` and `npourhadi1998@gmail.com`,thanks for your consideration.
