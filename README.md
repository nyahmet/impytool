# **impytool**

***contact: impytool.package@gmail.com***

[![Downloads](https://static.pepy.tech/personalized-badge/impytool?period=total&units=international_system&left_color=black&right_color=blue&left_text=Total-Downloads)](https://pepy.tech/project/impytool)
[![Downloads](https://static.pepy.tech/personalized-badge/impytool?period=month&units=international_system&left_color=black&right_color=blue&left_text=Monthly-Downloads)](https://pepy.tech/project/impytool)
[![Downloads](https://static.pepy.tech/personalized-badge/impytool?period=week&units=international_system&left_color=black&right_color=blue&left_text=Weekly-Downloads)](https://pepy.tech/project/impytool)


## ***"impytool is an opencv based tool that facilitates some image processing operations"***

### **USAGE:**
 
**Mandatory Parameters:**
*    image: Image file to be processed
*    save: 1 or not. The 1 is will save the file in new form


#### impytool.grayscale(image,save)
>>Converts the image in grayscale form

#### impytool.negative(image,save)
>>Converts the image in negative form

#### impytool.color_change(image,color1,color2,save)
>>Replaces one color in the image with another color.
* color1: the color that will change
* color2: the color that will replace color1
color: "blue" "green" "red" "yellow" "orange" "purple" "brown" "white" "black"

for example: **impytool.color_change('a.jpg','red','color2',0)** -> change red color to blue color on the "a.jpg"

 
#### impytool.color_filter(image,color,save)
>> The image filtered by choosen color
*    color: "blue","green","red" . 

#### impytool.blur(image,save)

>>    Converts the image blurred form


#### impytool.resize(image,w,h,save)
>> Adjusts the image to the desired dimensions
*    w: Width of the new sizes.
*    h: Height of the new sizes.


#### impytool.brightness(image,rate,save)
>> Adjusts the brightness of the image
*    rate: Change rate of the brightness.

#### impytool.contrast(image,alpha,save)
>> Adjusts the contrast of the image
*    alpha: Contrast change quantity
alpha should be in the range of 0-3.0
the 0-1.0 range is the lower contrast
the 1.0-3.0 is the higher contrast


#### impytool.only_color(image,color,save)
>> Shows only the selected color on the image
*    color: "blue" "green" "red" "yellow" "orange" "purple"



#### impytool.rotate(image,direction,save)
>> Flips the image
*    direction: The desired flip direction, it may be 'vertical' 'horizontal' 'both'

#### impytool.flip(image,angle,save)
>> Rotates the image
*    angle: The desired rotation angle, it may be 90-180-270

#### impytool.histogram(image,hist_type)
>> Creates a histogram for the image
*    hist_type: Determines the histogram type.
it may be 'hist' : for the grayscale images
it may be 'rgb_hist' : for the colored images

#### impytool.black_white(image,save)
>>  Converts the image black & white form.

