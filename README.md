#  **impytool**

[![Downloads](https://static.pepy.tech/personalized-badge/impytool?period=total&units=international_system&left_color=black&right_color=blue&left_text=Total-Downloads)](https://pepy.tech/project/impytool)

[![Downloads](https://static.pepy.tech/personalized-badge/impytool?period=month&units=international_system&left_color=black&right_color=blue&left_text=Month-Downloads)](https://pepy.tech/project/impytool)

[![Downloads](https://static.pepy.tech/personalized-badge/impytool?period=week&units=international_system&left_color=black&right_color=blue&left_text=Week-Downloads)](https://pepy.tech/project/impytool)

**contact: impytool.package@gmail.com**

## ***"impytool is an opencv based tool that facilitates some image processing operations"***




| FUNCTION | OPERATION | 
| -------- | -------- | 
| grayscale     | Converts the image in grayscale form | 
| negative      | Converts the image in negative form |
| color_change  | Replaces one color in the image with another color |
| color_filter  | The image filtered by choosen color |
| blur          | Converts the image blurred form |
| resize        | Adjusts the image to the desired dimensions |
| brightness    | Adjusts the brightness of the image |
| contrast      | Adjusts the contrast of the image |
| only_color    | Shows only the selected color on the image |
| rotate        | Rotates the image |
| flip          | Flips the image |
| histogram     | Creates a histogram for the image |
| black_white   | Converts the image black & white form |




## **USAGE:**
 
### **Mandatory Parameters:**
*    image: Image file to be processed
*    save: 1 or not. The 1 is will save the file in new form

### **impytool.grayscale(image:str,save:bool=True)**
   
> **Converts the image in grayscale form**

### **impytool.negative(image:str,save:bool=True)**

> **Converts the image in negative form**

### **impytool.color_change(image:str,color1,color2,save:bool=True)**

> **Replaces one color in the image with another color**

* color1: the color that will change
* color2: the color that will replace color1
 
> **color: "blue" "green" "red" "yellow" "orange" "purple" "brown" "white" "black"**

>> for example: **impytool.color_change('a.jpg','red','color2',0)** 

>>> **change red color to blue color on the "a.jpg"**


### **impytool.color_filter(image:str,color:str,save:bool=True)**

> **The image filtered by choosen color**

*    color: "blue","green","red" . 

### **impytool.blur(image:str,save:bool=True)**

> **Converts the image blurred form**

### **impytool.resize(image:str,w,h,save:bool=True)**

> **Adjusts the image to the desired dimensions**

*    w: Width of the new sizes.
*    h: Height of the new sizes.


### **impytool.brightness(image:str,rate,save:bool=True)**

> **Adjusts the brightness of the image**

*   rate: Change rate of the brightness.

### **impytool.contrast(image:str,alpha,save:bool=True)**

> **Adjusts the contrast of the image**

*    alpha: Contrast change quantity 
>**alpha should be in the range of 0-3.0**
>>**the 0-1.0 range is the lower contrast**
>>>**the 1.0-3.0 is the higher contrast**

### **impytool.only_color(image:str,color:str,save:bool=True)**

> **Shows only the selected color on the image**

*  color: "blue" "green" "red" "yellow" "orange" "purple"


### **impytool.rotate(image:str,direction,save:bool=True)**

> **Flips the image**

*    direction: The desired flip direction, it may be 'vertical' 'horizontal' 'both'

### **impytool.flip(image:str,angle,save:bool=True)**

> **Rotates the image**

*    angle: The desired rotation angle, it may be 90-180-270

### **impytool.histogram(image:str,hist_type)**

> **Creates a histogram for the image**

*    hist_type: Determines the histogram type.
>**it may be 'hist' : for the grayscale images**
>>**it may be 'rgb_hist' : for the colored images**

### **impytool.black_white(image:str,save:bool=True)**

> **Converts the image black & white form**