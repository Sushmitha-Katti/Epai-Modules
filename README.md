# Modules

## **Assignment**
Create these modules:
1. jpg/jpeg to png conversion (use PIL library) j2p
2. png to jpg conversion (use PIL library) p2j
3. image resizer that can resize bulk images with these features:
    * resize by user determined percentage (say 50% for height and width) (proportional) res_p
    * resize by user determined width (proportional) res_w
    * resize by user determined height (proportional) res_h
4. image cropper that can crop bulk images with these features:
    * center square/rectangle crop by user-determined pixels crp_px
    * centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
    * it let's user know which all images were not cropped due to size mismatches
5. a __main__ module that exposes all these features (using argparse)
6. finally create an zipped app, that exposes all of these features

## **Usage**

    python image_editor --input_path <source_image_folder/file_path> --output_path <dest_image_folder/file_path> --choice <option to choose> --resizer_value --cropper_value

1. image_path : Path for input folder/file
2. output_path : Path for output folder/file
3. choice :
    * p2j : converts png images to jpeg 
    * j2p : converts jpg images to png
    * res_p : resize the images according to pixel
    * res_w : resize the images by given width
    * res_h : resize the images by given height
    * crp_p : crops the image by percentage 
    * crp_px : crops the image according to pixel
4. resizer_value : This is used for resizing. It expects int value. Eg 40,40
5. cropper_value : This is used for cropping. It expects a comma seperated  value. Eg 224,224

## **Module Implementation**

1. ### jpg_to_png
It converts png images to jpeg

        usage : python jpg_to_png.py --source <path> --target <path>

2. ### png_to_jpg
converts jpg images to png

        usage : python png_to_jpg.py --source <path> --target <path>

3. ### cropper
    * crops the image by percentage/pixel
    * It prints the image names which are not cropped because of size mismatch 

        usage : python cropper.py --source <path> --target <path> --choice <crop_p/crop_px> --value <width>, <height>

4. ### resizer : 
    * resizes the images by percentage/width/height
    * In all the cases aspect ratio is maintained

        usage : python resizer.py --source <path> --target <path> --choice <res_p/res_w/res_h> --value <value>        



