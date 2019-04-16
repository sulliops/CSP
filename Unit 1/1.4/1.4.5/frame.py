import PIL
import matplotlib.pyplot as plt
import os.path
import PIL.ImageDraw

def round_corners(original_image, percent_of_side):
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height))
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    drawing_layer.polygon([(radius,0),(width-radius,0),
    (width-radius,height),(radius,height)],
    fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
    (width,height-radius),(0,height-radius)],
    fill=(127,0,127,255))
    drawing_layer.ellipse((0,0, 2*radius, 2*radius),
    fill=(0,127,127,255))
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius),
    fill=(0,127,127,255))
    drawing_layer.ellipse((0,height-2*radius, 2*radius,height),
     fill=(0,127,127,255))
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height),
    fill=(0,127,127,255))
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
def round_corners_of_all_images(directory=None):
    if directory == None:
        directory = os.getcwd()
        new_directory = os.path.join(directory, 'modified')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass
        image_list, file_list = get_images(directory)
    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.')
        new_image = round_corners(image_list[n],.30)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
def get_images(directory=None):
    if directory == None:
        directory = os.getcwd()
    image_list = []
    file_list = []
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass
    return image_list, file_list
def frame_image(image,division,r,g,b):
    width,height = image.size
    frame = PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(frame)
    drawing_layer.rectangle([(width/division,height/division), ((width/division)*(division-1),(height/division)*(division-1))],fill=(127,0,127,255))
    result = PIL.Image.new('RGBA', image.size, (r,g,b,255))
    result.paste(image,(0,0),mask=frame)
    return result
def frame_all_images():
    directory = os.getcwd()
    new_directory = os.path.join(directory, "modified")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for x in range(len(images)):
        fname,ftype = files[x].split('.')
        new_image = frame_image(images[x],10,255,0,0)
        newName = os.path.join(new_directory,fname + ".png")
        new_image.save(newName)