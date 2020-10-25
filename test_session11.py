import pytest
import os
import inspect
import re
from Image_editor import jpg_to_png
from Image_editor import png_to_jpg
from Image_editor import resizer
from Image_editor import cropper


all_modules = [jpg_to_png, png_to_jpg, resizer, cropper]

README_CONTENT_CHECK_FOR = [
                'j2p',
                'p2j',
                'res_w',
                'res_h',
                'res_p',
                'crp_p',
                'crp_px',
            ]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
   
    assert len(readme_words) >= 350, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5

def test_function_name_had_cap_letter():
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert function[1].__doc__


image_folder_path = os.path.abspath('Images')
images_target_path = os.path.abspath('target')

def test_jpg_to_png_converter():

    command = f'python Image_editor/jpg_to_png.py --source {image_folder_path} --target {images_target_path}'
    execute_command =  os.system(command)
    assert not execute_command, "JPG Conversion failed"

def test_png_to_jpg_converter():

    command = f'python Image_editor/png_to_jpg.py --source {image_folder_path} --target {images_target_path}'
    execute_command = os.system(command)
    assert not execute_command, "PNG Conversion failed"

def test_resize_by_percent():

    command = f'python Image_editor/resizer.py --source {image_folder_path} --target {images_target_path} --choice res_p --value 50'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Percent failed"

def test_resize_by_width():

    command = f'python Image_editor/resizer.py --source {image_folder_path} --target {images_target_path} --choice res_w --value 80'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Width failed"

def test_resize_by_height():

    command = f'python Image_editor/resizer.py  --source {image_folder_path} --target {images_target_path} --choice res_h --value 80'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Height failed"


def test_crop_by_pixel():

    command = f'python Image_editor/cropper.py --source {image_folder_path} --target {images_target_path} --choice crp_p --value 50,50'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Pixel failed"

def test_crop_by_percent():

    command = f'python Image_editor/cropper.py --source {image_folder_path} --target {images_target_path} --choice crp_px --value 224,224'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Percent failed"

def test_zip_convert_to_png():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice j2p'
    execute_command =  os.system(command)
    assert not execute_command, "JPG/JPEG Conversion failed"

def test_zip_convert_to_jpg():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice p2j'
    execute_command = os.system(command)
    assert not execute_command, "PNG Conversion failed"

def test_zip_resize_to_percent():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice res_p --resizer_value 80'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Percent failed"

def test_zip_resize_to_width():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice res_w --resizer_value 500'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Width failed"

def test_zip_resize_height():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice res_h --resizer_value 500'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Height failed"


def test_zip_center_crop_pixel():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice crp_px --cropper_value 224,224'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Pixel failed"

def test_zip_center_crop_pixel():

    command = f'python image_editor --input_path {image_folder_path} --output_path {images_target_path} --choice crp_p --cropper_value 50,50'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Percentage failed"

def test_error():
    with pytest.raises(ValueError):
        jpg_to_png.convert_to_png(path = "./different_director", output_path = "./different_director")

    with pytest.raises(ValueError):
        png_to_jpg.convert_to_jpg(input_path = "./different_director", output_path = "./different_director")



    


