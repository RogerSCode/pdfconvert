import sys
from PIL import Image
from os import path



if len(sys.argv)<2:

    print("error not enough args")
    sys.exit()        


first_file=1

if not path.exists(sys.argv[1]): # to determine if the first argument is a file or just the outputname
    first_file = 2

pdflist=[]
for arg in sys.argv[first_file:]:
        img = Image.open( arg)
        imgc = img.convert('RGB')
        pdflist.append(imgc)


pdflist[0].save( sys.argv[1]+".pdf",save_all=True, append_images=pdflist[1:])






