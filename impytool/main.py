import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def grayscale(image,save):
    try:
        img = cv2.imread(image,0)
    except:
        img = image
    gray_display = cv2.resize(img, (1280, 720))
    cv2.imshow("grayscale", gray_display)
    return img
    if(save==1):
        cv2.imwrite("grayscale " + image,img)

def color_filter(image,color,save):
    try:
        res = cv2.imread(image)
    except:
        res = image
    hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
    if(color=='blue' or color=='rgb'):
        b = res.copy()
        b[:, :, 1] = 0
        b[:, :, 2] = 0
        b_resize = cv2.resize(b, (960, 540))
        cv2.imshow("blue channel",b_resize)
        return b
        if(save==1):
            cv2.imwrite("blue channel " + image,b)
    if(color=='green' or color=='rgb'):
        g = res.copy()
        g[:, :, 0] = 0
        g[:, :, 2] = 0
        g_resize = cv2.resize(g, (960, 540))
        cv2.imshow("green channel",g_resize)
        return g
        if(save==1):
            cv2.imwrite("blue channel " + image,g)
    if(color=='red' or color=='rgb'):
        r = res.copy()
        r[:, :, 0] = 0
        r[:, :, 1] = 0
        r_resize = cv2.resize(r, (960, 540))
        cv2.imshow("red channel",r_resize)
        return r
        if(save==1):
            cv2.imwrite("blue channel " + image,r)
    original_resize = cv2.resize(res,(960,540))  
    cv2.imshow("original",original_resize)
    
def blur(image,save):
    try:
        img = cv2.imread(image)
    except:
        img = image
    blurred_image = cv2.blur(img,(10,10))
    blur_display = cv2.resize(blurred_image,(1280,720))
    cv2.imshow("blur",blur_display)
    return blurred_image
    if(save==1):
        cv2.imwrite("blurred " + image, blurred_image)

def resize(image,w,h,save):
    try:
        img = cv2.imread(image)
    except:
        img = image
    resized = cv2.resize(img,(w,h))
    cv2.imshow("resized image", resized)
    return resized
    if(save==1):
        cv2.imwrite(str(w) + "," + str(h) + " resized " + image, resized)
    
def brightness(image,rate,save):
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
    return img
    if(save==1):
        if(rate>0):
            cv2.imwrite(str(rate) + " brightened " + image, img)
        if(rate<0):
            cv2.imwrite(str(rate) + " darkened " + image, img)

def contrast(image,alpha,save):
    try:
        img = cv2.imread(image)
    except:
        img = image
    img_contrast = cv2.convertScaleAbs(img, alpha=alpha,beta = 0)
    img_display = cv2.resize(img_contrast,(1280,720))
    cv2.imshow("asd",img_display)
    return img_contrast
    if(save==1):
        cv2.imwrite(str(alpha) + " contrast value " + image, img_contrast)

def only_color(image,color,save):
    try:
        img = cv2.imread(image)
    except:
        img = image
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if(color=='red'):
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
        if(save==1):
            cv2.imwrite("only red color " + image, output)
    if(color=='blue'):
        low_blue = np.array([94,80,2])
        high_blue = np.array([126,255,255])
        mask = cv2.inRange(hsv,low_blue,high_blue)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only blue color",display)
        if(save==1):
            cv2.imwrite("only blue color " + image, output)
    if(color=='green'):
        low_green=np.array([50,50,50])             
        high_green=np.array([80,255,255])
        mask = cv2.inRange(hsv,low_green,high_green)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only green color",display)
        if(save==1):
            cv2.imwrite("only green color " + image, output)
    if(color=='yellow'):
        low_yellow=np.array([20,100,100])             
        high_yellow=np.array([30,255,255])
        mask = cv2.inRange(hsv,low_yellow,high_yellow)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only yellow color",display)
        if(save==1):
            cv2.imwrite("only yellow color " + image, output)
    if(color=='orange'):
        low_orange=np.array([10, 100, 20])             
        high_orange=np.array([20, 255, 255])
        mask = cv2.inRange(hsv,low_orange,high_orange)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only orange color",display)
        if(save==1):
            cv2.imwrite("only orange color " + image, output)
    if(color=='purple'):
        low_purple=np.array([120, 10, 150])             
        high_purple=np.array([150, 255, 255])
        mask = cv2.inRange(hsv,low_purple,high_purple)
        output = cv2.bitwise_and(img, img, mask = mask)
        display = cv2.resize(output,(1280,720))
        cv2.imshow("only purple color",display)
        if(save==1):
            cv2.imwrite("only purple color " + image, output)
    return output

def rotate(image,angle,save):
    try:
        img = cv2.imread(image)
    except:
        img = image
    if(angle==90):
        img_r = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    if(angle==180):
        img_r = cv2.rotate(img, cv2.ROTATE_180)
    if(angle==270):
        img_r = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) 
    display = cv2.resize(img_r , (960,540))
    cv2.imshow("rotated " + image, display )
    return img_r
    if(save==1):
            cv2.imwrite(angle + " rotated " + image, img_r)

def histogram(image,hist_type):
    try:
        img = cv2.imread(image)
    except:
        img = image
    if(hist_type=="rgb_hist"):
        color = ('b','g','r')
        for i,col in enumerate(color):
            hist = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(hist,color = col)
            plt.xlim([0,256])
        plt.show()
    if(hist_type=="hist"):
        plt.hist(img.ravel(),256,[0,256]); plt.show()
    if(hist_type=="2d"):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
        plt.imshow(hist,interpolation = 'nearest')
        plt.show()
       
def black_white(image,save):
    try:
        img = cv2.imread(image)
    except:
        img = image
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, bw) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    display = cv2.resize(bw, (960,540))
    cv2.imshow('black and white' + image, display)
    return bw
    if(save==1):
        cv2.imwrite('black and white' + image, bw)
           
    






























    
    
    
    
