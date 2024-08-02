'''
Visulaizing digital images in different ways with the end goal 
of culminating an mosaic image. Functions span from
computing the average rgb, to modifying pixels,
finding nearest colors and distance, and more in hopes
to make a mosaic of an image. Primarily, we will be focusing on 
our favorite image, Gulliver's Travel.

By: Syed Ali on 23/10/2022
'''

from random import seed, randrange
from image import Image, Point, Rectangle

def pixelize(img, w, h, colors):
    '''
    Pixelize an image, img, with each block being w pixels wide
    and h pixels high. Color is determined by the finding the
    closest color in the palette to the average pixel in the block.

    Parameters:
        img:Image - the image to pixelize
        w:int - the width of each block
        h:int - the height of each block
        palette:list - a list of colors

    Returns:
        i = image= a new pixelized image
    '''
    i = Image(img.getWidth(), img.getHeight())
    xrang = img.getWidth()
    yrang = img.getHeight()
    for x in range(0, xrang, w):
        for y in range(0, yrang, h):
            p1= Point(x, y)
            p2= Point(x+w, y+h)
            c = compute_avg(img, Rectangle(p1, p2))
            c_i = nearest_color(colors, c)
            fin= colors[c_i]
            r = Rectangle(Point(x, y), Point(x + w, y + h))
            r.setFill(fin)
            r.setOutline(fin)
            r.draw(i)
    return i


def compute_avg(image, rectangle):
    '''
    computes the avg color of an image by looking at all pixels

    Parameters:
        image= Image- an image
        rectangle= Rectangle- takes in a rectangle of defined size
    
    Returns:
        [int(ravg), int(gavg), int(bavg)]: list- the average color
    '''
    r= 0 
    g= 0
    b= 0
    i= 0
    p2= rectangle.getP2()
    p1= rectangle.getP1()
    xmin= min(p1.getX(), image.getWidth())
    xmax= p2.getX()
    ymin= min(p1.getY(), image.getHeight())
    ymax= p2.getY()
    if xmin < 0:
        xmin = 0
    if ymin < 0:
        ymin=0
    if xmax > image.getWidth():
        xmax = image.getWidth()
    if ymax > image.getHeight():
        ymax = image.getHeight()
    for x in range(xmin, xmax):
        for y in range (ymin, ymax):
            c= image.getPixel(x,y)
            r = c[0] + r
            g = c[1] + g
            b = c[2] + b
            i = i+1
    ravg= r/i
    gavg= g/i
    bavg= b/i
    return [int(ravg), int(gavg), int(bavg)]


def sample_image(img,n):
    '''
    returns the pallette of colors after looking at n random images

    Parameters: 
        img= Image- an image
        n= int- number

    Returns: 
        list= list- returns a list of colors
    '''
    list = []
    for i in range(n):
        y = img.getHeight()
        x = img.getWidth()
        xpix= randrange(0, x)
        ypix= randrange(0, y)
        pixxx= img.getPixel(xpix, ypix)
        list.append(pixxx)
    return list


def rgbdist(first, second):
    '''
    Returns the distance between 2 colors.
    Paramters:
        first= list- rgb of a color
        second= list- rgb of another color
    Return
        finalrgb= int- distance between 2 colors
    '''
    redsqrd= (first[0] - second[0])**2
    greensqrd= (first[1] - second[1])**2
    bluesqrd= (first[2] - second[2])**2
    finalrgb = (redsqrd + greensqrd + bluesqrd)**0.5
    return finalrgb


'''def distance(x,y): #FUNCTION WAS USED TO BUILD THE DISTANCE1 FUNCTION
                        USED AS REFERENCE
    return abs(x-y)'''


'''def nearest_number(lst, n): #FUNCTION WAS USED TO BUILD THE nearest_color 
                                FUNCTION USED AS REFERENCE
    min_i = 0
    min_dist = distance(n, lst[0])
    for i in range(1, len(lst)):
        v = lst[i]
        d = distance(v, n)
        if d < min_dist:
            min_dist = d
       	    min_i = i
    return min_i '''


def distance1(othercolor, color):
    '''
    Essentially just calls the rgbdist function.
    But I used to to help me keep track of things better.
    Parameters:
        othercolor= list- rgb of a color
        color= list- rgb of another color
    Return:
        x= int- distance between 2 colors
    '''
    x = rgbdist(othercolor, color)
    return x


def nearest_color(colorslist, othercolor):
    ''' 
    Compare the list of colors and the color in question and returns 
    the distance between the closest color in the color list
    Parameters: 
        othercolor: list- rgb of the color in question
        colorslist: list- rgb of the color pallette
    Returns:
        min_i= the distance between othercolor and the nearest
                color in the pallete
    '''
    min_i = 0
    min_dist = distance1(othercolor, colorslist[0])

    for i in range(1, len(colorslist)):
        v = colorslist[i]
        d = distance1(v, othercolor)
        if d < min_dist:
            min_dist = d
            min_i = i
    
    return min_i


def load_images(base, max_imgs):
    '''
    Return a list of images from files named BASE/output_0001.png,
    BASE/output_0002.png, ...BASE/output_[max_imgs].png

    Parameters:
        base:str - the directory and prefix of the files to load
        max_imgs:int - the highest numbered image in the directory
    Returns:
        a list of Images
    WARNING: Takes about 6 seconds to load all 2294 gulliver images
    '''
    imgs = []
    for i in range(1, max_imgs):
        img = Image("%s/output_%04d.png" % (base, i))
        imgs.append(img)
    return imgs


def image_averages(image_list):
    '''
    Return a list of the average color of each image in a list of images.

    Parameters:
        image_list:list - a list of Images
    Returns:
        a list of colors (list of [r, g, b])
    WARNING: Takes about a minute to compute the average of all
             2294 gulliver images
    '''
    avglist= []
    for i in range(len(image_list)):
        pic = image_list[i]
        xrang = pic.getWidth()
        yrang = pic.getHeight()
        '''for xx in range(xrang):
            for yy in range(yrang):'''
        x=compute_avg(image_list[i], Rectangle(Point(0,0),Point(xrang,yrang)))
        avglist.append(x)

    return avglist


def mosaic(img, frames, img_width, img_height):
    """
    Pixelize an image, img, with each block being img_width pixels
    wide and img_height pixels high. Blocks are images from the list
    of images based on the image that most closely matches the color
    of the pasted image.
    Parameters:
        img:Image - the image to pixelize
        frames:list - a list of images
        image_width:int - the width of each block
        image_height:int - the height of each block
    Returns:
        new_img= Image- a new pixelized image
    """
    new_img = Image(img.getWidth(), img.getHeight())
    avgs = image_averages(frames)
    for x in range(0, img.getWidth(), img_width):
        for y in range(0, img.getHeight(), img_height):
            # create a rectangle object to describe the patch
            r = Rectangle(Point(x, y), Point(x + img_width, y + img_height))

            # compute the average color of the patch
            c = compute_avg(img, r)

            # find the nearest (in terms of color) frame to this patch
            nearest_i = nearest_color(avgs, c)
            smallImage = frames[nearest_i]

            # draw the small frame into the poster
            smallImage.pasteInto(new_img, r)
    return new_img


def main():
    '''
    Makes the Mosaic with the first 50 images
    Professor Rich in edstem said having this as the final main code is ok.
    '''
    img = Image("/data/cs21/gulliver/poster_full.png")
    # Change from 2294 to 50 makes it run faster (with worse results)
    frames = load_images("/data/cs21/gulliver", 50)
    o_img = mosaic(img, frames, 18, 12)
    o_img.save("mosaic_50.png")
main()
