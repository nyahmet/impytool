import cv2
import numpy as np
from matplotlib import pyplot as plt

def grayscale(image:str,save:bool=True):
    try:
        img = cv2.imread(image,0)
    except:
        img = image
    gray_display = cv2.resize(img, (1280, 720))
    cv2.imshow("grayscale", gray_display)
    if save:
        cv2.imwrite("grayscale " + image,img)
    return img

def color_filter(image:str,color:str,save:bool=True):
    try:
        res = cv2.imread(image)
    except:
        res = image
    hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
    if color in ['blue', 'rgb']:
        b = res.copy()
        b[:, :, 1] = 0
        b[:, :, 2] = 0
        b_resize = cv2.resize(b, (960, 540))
        cv2.imshow("blue channel",b_resize)
        if save:
            cv2.imwrite("blue channel " + image,b)
        return b
    if color in ['green', 'rgb']:
        g = res.copy()
        g[:, :, 0] = 0
        g[:, :, 2] = 0
        g_resize = cv2.resize(g, (960, 540))
        cv2.imshow("green channel",g_resize)
        if save:
            cv2.imwrite("green channel " + image,g)
        return g
    if color in ['red', 'rgb']:
        r = res.copy()
        r[:, :, 0] = 0
        r[:, :, 1] = 0
        r_resize = cv2.resize(r, (960, 540))
        cv2.imshow("red channel",r_resize)
        if save:
            cv2.imwrite("red channel " + image,r)
        return r
    original_resize = cv2.resize(res,(960,540))
    cv2.imshow("original",original_resize)
    
def blur(image:str,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    blurred_image = cv2.blur(img,(10,10))
    blur_display = cv2.resize(blurred_image,(1280,720))
    cv2.imshow("blur",blur_display)
    if save:
        cv2.imwrite("blurred " + image, blurred_image)
    return blurred_image

def resize(image:str,w,h,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    resized = cv2.resize(img,(w,h))
    cv2.imshow("resized image", resized)
    if save:
        cv2.imwrite(str(w) + "," + str(h) + " resized " + image, resized)
    return resized
    
def brightness(image:str,rate,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    img= cv2.add(img,np.array([float(rate)]))
    img_display = cv2.resize(img,(1280,720))
    if(rate!=0):
        cv2.imshow("brightness changed image", img_display )
    else:
        cv2.imshow("original image", img_display )
    if save:
        if(rate>0):
            cv2.imwrite(str(rate) + " brightened " + image, img)
        if(rate<0):
            cv2.imwrite(str(rate) + " darkened " + image, img)
    return img

def contrast(image:str,alpha,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    img_contrast = cv2.convertScaleAbs(img, alpha=alpha,beta = 0)
    img_display = cv2.resize(img_contrast,(1280,720))
    if save:
        cv2.imwrite(str(alpha) + " contrast value " + image, img_contrast)
    cv2.imshow("asd",img_display)
    return img_contrast

def only_color(image:str,color:str,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if color == 'blue':
        low_blue = np.array([94,80,2])
        high_blue = np.array([126,255,255])
        mask = cv2.inRange(hsv,low_blue,high_blue)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only blue color",display)
        if save:
            cv2.imwrite("only blue color " + image, output)
    elif color == 'green':
        low_green=np.array([50,50,50])
        high_green=np.array([80,255,255])
        mask = cv2.inRange(hsv,low_green,high_green)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only green color",display)
        if save:
            cv2.imwrite("only green color " + image, output)
    elif color == 'orange':
        low_orange=np.array([10, 100, 20])
        high_orange=np.array([20, 255, 255])
        mask = cv2.inRange(hsv,low_orange,high_orange)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only orange color",display)
        if save:
            cv2.imwrite("only orange color " + image, output)
    elif color == 'purple':
        low_purple=np.array([120, 10, 150])
        high_purple=np.array([150, 255, 255])
        mask = cv2.inRange(hsv,low_purple,high_purple)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only purple color",display)
        if save:
            cv2.imwrite("only purple color " + image, output)
    elif color == 'red':
        low_red = np.array([0,120,70])
        high_red = np.array([10,255,255])
        red_mask1 = cv2.inRange(hsv, low_red, high_red)
        low_red = np.array([170,120,70])
        high_red = np.array([180,255,255])
        red_mask2 = cv2.inRange(hsv,low_red,high_red)
        mask = red_mask1+red_mask2
        output = cv2.bitwise_and(hsv, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only red color",display)
        if save:
            cv2.imwrite("only red color " + image, output)
    elif color == 'yellow':
        low_yellow=np.array([20,100,100])
        high_yellow=np.array([30,255,255])
        mask = cv2.inRange(hsv,low_yellow,high_yellow)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only yellow color",display)
        if save:
            cv2.imwrite("only yellow color " + image, output)
    return output

def rotate(image:str,angle,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    if angle == 180:
        img_r = cv2.rotate(img, cv2.ROTATE_180)
    elif angle == 270:
        img_r = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif angle == 90:
        img_r = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    display = cv2.resize(img_r , (960,540))
    if save:
            cv2.imwrite(str(angle) + " rotated " + image, img_r)
    cv2.imshow("rotated " + image, display )
    return img_r

def histogram(image:str,hist_type):
    try:
        img = cv2.imread(image)
    except:
        img = image
    if hist_type == "2d":
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
        plt.imshow(hist,interpolation = 'nearest')
        plt.show()
    elif hist_type == "hist":
        plt.hist(img.ravel(),256,[0,256])
        plt.show()
    elif hist_type == "rgb_hist":
        color = ('b','g','r')
        for i,col in enumerate(color):
            hist = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(hist,color = col)
            plt.xlim([0,256])
        plt.show()
       
def black_white(image:str,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, bw) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    display = cv2.resize(bw, (960,540))
    if save:
        cv2.imwrite('black and white' + image, bw)
    cv2.imshow('black and white' + image, display)
    return bw

def negative(image:str,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    negative_image = cv2.bitwise_not(img)
    negative_display = cv2.resize(negative_image,(1280,720))
    if save:
        cv2.imwrite("negative " + image, negative_image)
    cv2.imshow("negative",negative_display)
    return negative_image

def flip(image:str,direction,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    if direction == 'both':
        img_f = cv2.flip(img, -1)
    elif direction == 'horizontal':
        img_f = cv2.flip(img, 1)
    elif direction == 'vertical':
        img_f = cv2.flip(img, 0)
    display = cv2.resize(img_f , (960,540))
    if save:
            cv2.imwrite("flipped " + image, img_f)
    cv2.imshow("flipped " + image, display )
    return img_f

def color_change(image:str,color1,color2,save:bool=True):
    try:
        img = cv2.imread(image)
    except:
        img = image
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if(color1=="red"):
        low_red = np.array([0,120,70])
        high_red = np.array([10,255,255])
        red_mask1 = cv2.inRange(hsv, low_red, high_red)
        low_red = np.array([170,120,70])
        high_red = np.array([180,255,255])
        red_mask2 = cv2.inRange(hsv,low_red,high_red)
        red = red_mask1+red_mask2
        mask = red
    if(color2=="red"):
        to = (0,0,255)
    if(color1=="blue"):
        low_blue = np.array([94,80,2])
        high_blue = np.array([126,255,255])
        blue = cv2.inRange(hsv,low_blue,high_blue)
        mask = blue
    if(color2=="blue"):
        to = (255,0,0)
    if(color1=="green"):
        low_green=np.array([50,50,50])             
        high_green=np.array([80,255,255])
        green = cv2.inRange(hsv,low_green,high_green)
        mask = green
    if(color2=="green"):
        to = (0,255,0)
    if(color1=="yellow"):
        low_yellow=np.array([20,100,100])             
        high_yellow=np.array([30,255,255])
        yellow = cv2.inRange(hsv,low_yellow,high_yellow)
        mask = yellow
    if(color2=="yellow"):
        to = (0,255,255)
    if(color1=="orange"):
        low_orange=np.array([10, 100, 20])             
        high_orange=np.array([20, 255, 255])
        orange = cv2.inRange(hsv,low_orange,high_orange)
        mask = orange
    if(color2=="orange"):
        to = 	(0,165,255)
    if(color1=="purple"):
        low_purple=np.array([120, 10, 150])             
        high_purple=np.array([150, 255, 255])
        purple = cv2.inRange(hsv,low_purple,high_purple)
        mask = purple
    if(color2=="purple"):
        to = (255,0,255)
    if(color1=="brown"):
        low_brown=np.array([10, 0, 0])
        high_brown=np.array([20, 255, 255])
        brown = cv2.inRange(hsv,low_brown,high_brown)
        mask = brown
    if(color2=="brown"):
        to = 	(0,75,150)
    if(color1=="white"):
        low_white = np.array([0, 0, 240])
        high_white = np.array([255, 15, 255])
        white = cv2.inRange(hsv,low_white,high_white)
        mask = white
    if(color2=="white"):
        to = (255,255,255)
    if(color1=="black"):
        low_black = np.array([0, 0, 0])
        high_black = np.array([0, 0, 0])
        black = cv2.inRange(hsv,low_black,high_black)
        mask = black
    if(color2=="black"):
        to = (0,0,0)
    img[mask>0] = to
    display = cv2.resize(img, (960,540))
    if save:
        cv2.imwrite(color1 + " changed to " + color2 + image, img)
    cv2.imshow("changed " + image, display)
    return img
