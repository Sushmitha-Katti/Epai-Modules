import os
import argparse
from PIL import Image
def resize_single_image(path,feature_func, value, output_path, file):
    """
    Single Image resizer. Actual Resizing happens here
    """
      
    if os.path.isfile(path) and path.endswith(('jpg', 'png', 'jpeg')):
            
            full_path = os.path.abspath(path)
            image = Image.open(full_path)
            size = image.size
            new_size = feature_func(size,value)
            resize_image = image.resize(new_size)
         
            resize_image.save(output_path +'/' + file )
            del image
            del resize_image
    else :
            raise ValueError("Expected images of format .jpg, jpeg or png!!")

def resizer(path, feature, value, output_path):
    """
    Resizes bulk images with a given feature 
    percentange : res_p
    determined_width : res_w
    determined_height : res_h
    
    """
    
    feature_dict = {
        'res_p' : lambda size, val : ((val*size[0])//100, (val*size[0])//100),
        'res_w' : lambda size, val : (val, size[1] * val //size[0]),
        'res_h' : lambda size, val : (size[0] * val //size[1], val)
        
    }
    if not(os.path.isdir(path) or os.path.isfile(path)):
        raise ValueError(f'The location "{path}" does not exist')
        
    if(value <= 0) :
        raise ValueError("The resolution value must be greater than 0")
        
    
    if os.path.isfile(path):
      
        resize_single_image(path,feature_dict[feature],value, output_path, path.split('\\')[-1])
            
    elif os.path.isdir(path):
        for file in os.listdir(path):
            
            full_img_path = os.path.join(path, file)
            resize_single_image(full_img_path, feature_dict[feature],value, output_path, file)
            
    print("Images are resizied successfully")

if __name__ == '__main__':
    """The main segment runs when this file is invoked independently"""
    print('\n\nRunning command line tool for Image resizer.')

    parser = argparse.ArgumentParser(prog='resizer.py',
                                     description='\nA command line tool for Image resizer.')

    parser.add_argument('--source', type=str, help='The source file or directory where images are located')
    parser.add_argument('--target', type=str, help='The target file or directory where images should be dumped')
    parser.add_argument('--choice', type=str, help='Choice for type of resizing res_p for pixel or res_w for width res_h for height. In all cases aspect ratio is maintained')
    parser.add_argument('--value', type=int, help='value for Resizing. It should be "," It should be int')

    args = parser.parse_args()
    
    
    resizer(args.source,args.choice, args.value,args.target) 