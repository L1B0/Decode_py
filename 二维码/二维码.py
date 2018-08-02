from PIL import Image
im = Image.new('RGB',(256,256))
pix = im.load()
with open('flag.bmp','r') as f:
         txt = f.read()
         print len(txt)
         for x in xrange(len(txt)):
                  if txt[x] == 0xff:
                           pix[x/29,x%29] = (255,255,255)
                  else:
                           pix[x/29,x%29] = (0,0,0)
im.show()
im.save('flag.png')
                  
