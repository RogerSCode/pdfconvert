import sys
from PIL import Image



if len(sys.argv)<2:
    print("error not enough args")
    sys.exit()        

pdflist=[]
for arg in sys.argv[1:]:
        img = Image.open( arg)
        imgc = img.convert('RGB')
        pdflist.append(imgc)


pdflist[0].save( sys.argv[1]+".pdf",save_all=True, append_images=pdflist[1:])






