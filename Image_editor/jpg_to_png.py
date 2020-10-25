import os
import argparse
from PIL import Image


def convert_single_file(path,output_path, filename):
    """
    Single Image converter. Actual converting happens here
    """
    if os.path.isfile(path):
        full_path = os.path.abspath(path)
     

        if not any(full_path.lower().endswith(x) for x in ['.jpg', '.jpeg']):
            raise TypeError("\nPlease check the format of the file passed.")

        image = Image.open(full_path)
       
        image.save(output_path + "\\" + filename.rsplit('.')[0] + '.png')
    
        del image


def convert_to_png(path,output_path):
    """
    Converts all the files in the passed directory from `jpg` to `png`, if a single file is passed, it's converted.
    :param path: the absolute path of the directory from where JPG format needs to be converted into PNG format
    """
    if not (os.path.isdir(path) or os.path.isfile(path)):
        raise ValueError(f'The passed location `{path}` does not exist or is invalid! Please check.')

    if os.path.isfile(path):
       
        convert_single_file(path, output_path, path)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            full_img_path = os.path.join(path, file)
            if os.path.isfile(full_img_path) and any(full_img_path.lower().endswith(x) for x in ['.jpg', '.jpeg']):
               
                convert_single_file(full_img_path, output_path, file)
    print('All files are converted to jpg Successfully')


if __name__ == '__main__':
    """The main segment runs when this file is invoked independently"""
    print('\n\nRunning command line tool for JPG to PNG convertor.')

    parser = argparse.ArgumentParser(prog='jpg_to_png.py',
                                     description='\nA command line utility to convert single file or bulk of images from a given directory from jpg to png format.')

    parser.add_argument('--source', type=str, help='The source file or directory where images are located')
    parser.add_argument('--target', type=str, help='The target file or directory where images should be dumped')

    args = parser.parse_args()
    convert_to_png(args.source, args.target)
    