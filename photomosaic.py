#!/usr/bin/env python3
def getImages(imageDir):
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir,file))
        try:
            fp = open(filePath,'rb')
            im = Image.open(fp)
            images.append(im)
            im.load()
            fp.close()
        except:
            print("Invalid image:%s" % (filepath,))

    return images

def getAverageRGB(image):
    npixels = image.size[0]*image.size[1]
    cols = image.getcolors(npixels)
    sumRGB = [(x[0] * x[1][0], x[0] * x[1][1], x[0] * x[1][2]) for x in cols]
    avg = tuple([int(sum(x) / npixels) for x in zip(*sumRGB)])
    return avg

def splitImage(image,size):
    W,H = image.size[0], image.size[1]
    m,n = size
    w,h = int(W / n), int(H / m)
    imgs = []
    for j in range(m):
        for i in range(n):
            imgs.append(image.crop((i * w, j * h, (i +1) * w,(j+1) * h)))

    return imgs

