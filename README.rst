**impytool**
============

|Downloads|

|image1|

|image2|

**contact: impytool.package@gmail.com**

**“impytool is an opencv based tool that facilitates some image processing operations”**
----------------------------------------------------------------------------------------

`GitHub README for More Detailed User Manual`_

+-------------------------+-------------------------+------------------+
| FUNCTION                | OPERATION               | USAGE            |
+=========================+=========================+==================+
| grayscale               | Converts the image in   | impytool.grays   |
|                         | grayscale form          | cale(image,save) |
+-------------------------+-------------------------+------------------+
| negative                | Converts the image in   | impytool.nega    |
|                         | negative form           | tive(image,save) |
+-------------------------+-------------------------+------------------+
| color_change            | Replaces one color in   | impytool.color_  |
|                         | the image with another  | change(image,col |
|                         | color                   | or1,color2,save) |
+-------------------------+-------------------------+------------------+
| color_filter            | The image filtered by   | impytoo          |
|                         | choosen color           | l.color_filter(i |
|                         |                         | mage,color,save) |
+-------------------------+-------------------------+------------------+
| blur                    | Converts the image      | impytool.        |
|                         | blurred form            | blur(image,save) |
+-------------------------+-------------------------+------------------+
| resize                  | Adjusts the image to    | impytool.resize  |
|                         | the desired dimensions  | (image,w,h,save) |
+-------------------------+-------------------------+------------------+
| brightness              | Adjusts the brightness  | impy             |
|                         | of the image            | tool.brightness( |
|                         |                         | image,rate,save) |
+-------------------------+-------------------------+------------------+
| contrast                | Adjusts the contrast of | imp              |
|                         | the image               | ytool.contrast(i |
|                         |                         | mage,alpha,save) |
+-------------------------+-------------------------+------------------+
| only_color              | Shows only the selected | impyt            |
|                         | color on the image      | ool.only_color(i |
|                         |                         | mage,color,save) |
+-------------------------+-------------------------+------------------+
| rotate                  | Rotates the image       | impyt            |
|                         |                         | ool.rotate(image |
|                         |                         | ,direction,save) |
+-------------------------+-------------------------+------------------+
| flip                    | Flips the image         | impytool.flip(i  |
|                         |                         | mage,angle,save) |
+-------------------------+-------------------------+------------------+
| histogram               | Creates a histogram for | imp              |
|                         | the image               | ytool.histogram( |
|                         |                         | image,hist_type) |
+-------------------------+-------------------------+------------------+
| black_white             | Converts the image      | impytool.black_w |
|                         | black & white form      | hite(image,save) |
+-------------------------+-------------------------+------------------+

+-----------------------+-----------------------+-----------------------+
| PARAMETER             | EXPLANATION           | EXAMPLE               |
+=======================+=======================+=======================+
| image                 | working image         | ‘example.jpg’         |
+-----------------------+-----------------------+-----------------------+
| save                  | 1 to save result or 0 | 1 (or 0)              |
|                       | to not                |                       |
+-----------------------+-----------------------+-----------------------+
| color, color1, color2 | color name            | ‘red’, ‘blue’         |
+-----------------------+-----------------------+-----------------------+
| w, h                  | width, height         | 1280, 720             |
+-----------------------+-----------------------+-----------------------+
| rate                  | change rate (for      | 50                    |
|                       | brightness)           |                       |
+-----------------------+-----------------------+-----------------------+
| alpha                 | contrast change       | 1.5                   |
|                       | quantity (in range    |                       |
|                       | 0-3.0) **0-1.0 to     |                       |
|                       | lower, 1.0-3.0 to     |                       |
|                       | higher**              |                       |
+-----------------------+-----------------------+-----------------------+
| direction             | flip direction        | ‘vertical’            |
|                       |                       | ‘horizontal’ ‘both’   |
+-----------------------+-----------------------+-----------------------+
| angle                 | rotation angle        | 90, 180, 270          |
+-----------------------+-----------------------+-----------------------+
| hist_type             | determines the        | ‘hist’, ‘rgb_hist’    |
|                       | histogram type,       |                       |
|                       | **‘hist’ for          |                       |
|                       | grayscale images and  |                       |
|                       | ‘rgb_hist’ for        |                       |
|                       | colored images**      |                       |
+-----------------------+-----------------------+-----------------------+

.. _GitHub README for More Detailed User Manual: https://github.com/nyahmet/impytool/blob/main/README.md

.. |Downloads| image:: https://static.pepy.tech/personalized-badge/impytool?period=total&units=international_system&left_color=black&right_color=blue&left_text=Total-Downloads
   :target: https://pepy.tech/project/impytool
.. |image1| image:: https://static.pepy.tech/personalized-badge/impytool?period=month&units=international_system&left_color=black&right_color=blue&left_text=Month-Downloads
   :target: https://pepy.tech/project/impytool
.. |image2| image:: https://static.pepy.tech/personalized-badge/impytool?period=week&units=international_system&left_color=black&right_color=blue&left_text=Week-Downloads
   :target: https://pepy.tech/project/impytool