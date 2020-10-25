import os
import argparse
from PIL import Image

def single_image_cropper(path, feature_func, value, output_path, file):
    """
    Single Image center_cropper. Actual cropping  happens here
    """
    
    if os.path.isfile(path) and path.endswith(('jpg', 'png', 'jpeg')):
            
            full_path = os.path.abspath(path)
            image = Image.open(full_path)
            w, h = feature_func(image.size, value)
            img_width, img_height = image.size
            left, right = (img_width - w) //2 , (img_width + w) // 2
            top, bottom = (img_height - h) // 2, (img_height + h) // 2
       
            if(left < 0 or right < 0 or top < 0 or bottom < 0 ):
                print(f"Image in location {full_path} cannot be cropped")
                return
            else :
                new_image = image.crop((left, top, right, bottom))
            new_image.save(output_path + '/' + file)
            del new_image
        

            
    else:
            raise ValueError("Expected images of format .jpg, jpeg or png!!")

def center_cropper(path, feature, value, output_path):
    """
    Crop bulk images with a given feature 
    percentange : crop_p
    pixel : crop_px

    
    """
    
    value = eval(value)
    
    
    feature_dict = {
        'crp_px' : lambda old_size, new_size : (new_size[0], new_size[1]),
        'crp_p' : lambda old_size, new_size : (new_size[0]*old_size[0]//100, new_size[1]*old_size[1]//100),
      
        
    }
    if not(os.path.isdir(path) or os.path.isfile(path)):
        raise ValueError(f'The location "{path}" does not exist')
        
    if(int(value[0]) <= 0 or int(value[1]) <= 0) :
        raise ValueError("The resolution value must be greater than 0")
        
        
    if os.path.isfile(path):
       
        single_image_cropper(path,feature_dict[feature],value, output_path, path.split('\\')[-1])
            
    elif os.path.isdir(path):
        for file in os.listdir(path):
            full_img_path = os.path.join(path, file)
            single_image_cropper(full_img_path, feature_dict[feature],value, output_path, file)

    print("All images cropped successfully")

if __name__ == '__main__':
    """The main segment runs when this file is invoked independently"""
    print('\n\nRunning command line tool for Image Cropper.')

    parser = argparse.ArgumentParser(prog='center_cropper.py',
                                     description='\nA command line tool for Image Cropper.')

    parser.add_argument('--source', type=str, help='The source file or directory where images are located')
    parser.add_argument('--target', type=str, help='The target file or directory where images should be dumped')
    parser.add_argument('--choice', type=str, help='Choice for type of cropping crp_px for pixel or crp_p for percentage')
    parser.add_argument('--value', type=str, help='value for cropping. It should be "," seperated value width, height. Eg: 100,100')

    args = parser.parse_args()
    value = eval(args.value)
    
    center_cropper(args.source,args.choice, args.value,args.target) 
    