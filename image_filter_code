'''
Takes the image of Gulliver travel. Edits it depending on what the user wants.
By: Syed Ali
'''

from image import Image

def negate_pixel(img, x, y):
    '''Inverts the color of pixel
        img (image) = image we are changing
        x (int) = the pixel in the right and left
        y (int) = the pixel up and down
    return the inverted color of (x,y) in img'''
    c = img.getPixel(x, y)
    nc = [255 - c[0], 255 - c[1], 255 - c[2]]
    return nc

def negate(img):
    '''negate the img 
        img (Image) = image we are changing
    return fimg (new img)'''
    yrang= img.getHeight()
    xrang= img.getWidth()
    fimg = Image(xrang, yrang)

    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            fimg.setPixel(x, y, negate_pixel(img, x, y))
    return fimg

def rgb2gray(c):
    '''given a color (list of RGB), return the gray scale color 
        c (ints)= rgb
    return [gray, gray, gray] (int) = gray colors'''
    r = c[0]
    g = c[1]
    b = c[2]
    gray = int((r + g + b) / 3)
    return [gray, gray, gray]

def grayscale(img):
    '''gray the img
        img (Image) = image we are changing
    return eimg (new img)''' 
    yrang= img.getHeight()
    xrang= img.getWidth()
    eimg = Image(xrang, yrang)
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            c= img.getPixel(x,y)
            eimg.setPixel(x, y, rgb2gray(c))
    return eimg

def binary(img):
    '''sets the image to binary
        img (Image) = image we are changing
    return eimg (new img)'''
    yrang= img.getHeight()
    xrang= img.getWidth()
    dimg = Image(xrang, yrang)
    cimg2= grayscale(img)
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            s= cimg2.getPixel(x,y)
            if s > [128,128,128]:
                cimg2.setPixel(x, y, [255,255,255])
            else: 
                cimg2.setPixel(x, y, [0,0,0])
    return cimg2

def sepia(img, sepia_amount):
    '''makes the image sepia
        img (Image) = image we are changing
    return cimg (new img)'''
    yrang= img.getHeight()
    xrang= img.getWidth()
    cimg = Image(xrang, yrang)
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            c = img.getPixel(x, y)
            c[0]= c[0] + 2*sepia_amount
            c[1]= c[2] + sepia_amount
            c[2]= c[2]- sepia_amount
            while c[0] > 255:
                c[0]= c[0]-1
            while c[1] > 255:
                c[1]= c[1]-1
            while c[2] > 255:
                c[2]= c[2]-1
            cimg.setPixel(x,y,c)
    return cimg

def fairey(img):
    '''makes the image fairey
        img (Image) = image we are changing
    return bimg (new img)'''
    yrang= img.getHeight()
    xrang= img.getWidth()
    bimg = Image(xrang, yrang)
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            c = img.getPixel(x, y)
            sum = c[0] + c[1] + c[2]
            if 0 < sum and sum <= 181:
                bimg.setPixel(x,y,[0, 51, 76])
            elif 181 < sum and sum <= 363:
                bimg.setPixel(x,y,[217, 26, 33])
            elif 364 < sum and sum <= 545:
                bimg.setPixel(x,y,[112, 150, 158])
            elif 546 < sum and sum <=  765:
                bimg.setPixel(x,y,[252, 227, 166])
    return bimg

def mirror(img):
    '''mirrors the image
        img (Image) = image we are changing
    return aimg (new img)'''
    yrang= img.getHeight()
    xrang= img.getWidth()
    aimg = Image(xrang, yrang)
    for y in range(yrang):
        for x in range(xrang):
            c= img.getPixel(x,y)
            aimg.setPixel((xrang-1)-x, y, c)
    return aimg

def flip(img):
    '''OPTIONAL LAB: flips the image
    img (Image) = image we are changing
    return nimg (new img)'''
    yrang= img.getHeight()
    xrang= img.getWidth()
    nimg = Image(xrang, yrang)
    for y in range(yrang):
        for x in range(xrang):
            c= img.getPixel(x,y)
            nimg.setPixel((xrang-1)-x, (yrang-1)-y, c)
    return nimg
            
def main():
    img_i = Image("/data/cs21/gulliver/poster.png")
    img_i.save("ori_gull.png")

    img1= negate(img_i)
    img1.save("negate.png")

    img2 = grayscale(img_i)
    img2.save("gray.png")

    img3 = binary(img_i)
    img3.save("binary.png")

    img4 = sepia(grayscale(img_i), 20)
    img4.save("sepia.png")

    img5 = fairey(img_i)
    img5.save("fairey.png")

    img6 = mirror(img_i)
    img6= img6.save("mirror.png")

    img7 = flip(img_i)
    img7.save("flip.png")
main()
