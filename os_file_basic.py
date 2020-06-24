import os

dir ='D:\\tools'
for f in os.listdir(dir):
        fpath = os.path.join(dir, f)
        if os.path.isfile(fpath):
           print ('Found file %s' %fpath)
        elif os.path.isdir(fpath):
           print ('Found dir %s' %fpath)
