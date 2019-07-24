## REAL CLEAN CODE##
from PIL import Image
import random
import math

def 보로노이_다이어그램_생성(폭, 높이, 셀_숫자): 
  image = Image.new("RGB", (폭, 높이))
  putpixel = image.putpixel
  imgx,imgy = image.size
  nx = [135 , 260, 260, 260, 260, 390, 390, 390, 390, 450, 450, 570, 570, 630, 630, 630, 630,  730, 730, 730, 730, 850 ]
  ny = [250, 420, 300, 190, 80 , 420, 300, 190, 80 , 300, 190, 300, 190, 420, 300, 190, 80 ,  420, 300, 190, 80 ,  250]
  nr = [102, 153,  204, 255, 153, 102, 255,  51, 153, 255, 153, 51,  000, 0,     0, 0, 0,0,  0,  0,  51,   0 ]
  ng = [0  , 0  ,  0 ,  0 ,  0  , 0  , 0  ,  0 , 51 , 102,  0,  51,  000, 0,     0, 0, 0,0,  0,  0,  51,   0 ]
  nb = [0  , 0  ,  0 ,  0 ,  0  , 51 , 0  ,  0 , 51 , 102,  0,  255, 255, 102, 153, 102,0,0,102,255,255, 153 ]
  
  #num_cells = len(nx)
  '''
  for i in range(셀_숫자):
    nx.append(random.randrange(imgx))
    ny.append(random.randrange(imgy))
    nr.append(random.randrange(256))
    ng.append(random.randrange(256))
    nb.append(random.randrange(256))'''

  print(nx,"\n",ny)
  print(imgx, imgy)
  

          
  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx, imgy)
      j = -1
      for i in range(셀_숫자):
        d = math.hypot(nx[i]-x, ny[i]-y)
        if d < dmin:
          dmin = d
          j = i
      if (x, y) == (nx[j], ny[j]):
        putpixel((x, y), (255, 255, 255))
      else:
        putpixel((x, y), (nr[j], ng[j], nb[j] ))
    
  image.save("VoronoiDiagram.png", "PNG")
  image.show()


if __name__== "__main__":
  보로노이_다이어그램_생성(1000, 500,22)
