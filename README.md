# impytool

**"impytool is an opencv based tool that facilitates some image processing operations"**

**USAGE:**

**impytool.grayscale(image,save)**

    image: Image file to be processed.
    save: 1 or not. The 1 is will save the file in new form.

**impytool.color_filter(image,color,save)**

    color: "blue","green","red" . The image filtered by choosen color.

**impytool.blur(image,save)**

    Converts the image blurred form.

**impytool.resize(image,w,h,save)**

    w: Width of the desired new sizes.
    h: Height of the desired new sizes.

**impytool.brightness(image,rate,save)**

    rate: Desired change rate of the brightness.

**impytool.contrast(image,alpha,save)**

    alpha: Contrast change quantity.

            alpha should be in the range of 0-3.0
            the 0-1.0 range is the lower contrast
            the 1.0-3.0 is the higher contrast

**impytool.only_color(image,color,save)**

    color: "blue" "green" "red" "yellow" "orange" "purple"

            shows only the selected color

**impytool.rotate(image,angle,save)**

    angle: The desired rotation angle, it may be 90-180-270

**impytool.histogram(image,hist_type)**

    hist_type: Determines the histogram type.

            it may be hist : for the grayscale images
            it may be rgb_hist : for the colored images

**impytool.black_white(image,save)**

    Converts the image black & white form.
