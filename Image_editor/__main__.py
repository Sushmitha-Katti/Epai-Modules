import argparse
from cropper import center_cropper
from resizer import resizer
from jpg_to_png import  convert_to_png
from png_to_jpg import convert_to_jpg


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-i','--input_path', type = str, help = "Input Image Location")
    parser.add_argument('-o','--output_path', type = str, help = "Output Image Location")
    parser.add_argument('--choice', type = str , help ="option")
    parser.add_argument('--resizer_value', type = int, help = "Value for  resizer. ")
    parser.add_argument('--cropper_value', type = str, help = "Value for  cropper. It should be (width,height) ")

    args = parser.parse_args()

  

    if args.choice ==  'p2j':
   
        convert_to_jpg(args.input_path,args.output_path)
    
    elif args.choice == 'j2p':
      
        convert_to_png(args.input_path,args.output_path)
    
    elif args.choice in  ['res_p','res_w','res_h']:
        
        resizer(args.input_path, args.choice, args.resizer_value,args.output_path)

    elif args.choice  in ['crp_px', 'crp_p']:
        center_cropper(args.input_path, args.choice, args.cropper_value,args.output_path)
    else : 
        raise ValueError('Choice choosed is not available, choose from the choice j2p, p2j, res_p, res_w, res_h, crp_px, crp_p')