from django.test import TestCase

# Create your tests here.

# load library
import urllib.request
import os

# image url to download
url = "https://cafefiles.pstatic.net/MjAxOTEwMjNfMjAw/MDAxNTcxODE3ODkzNzIw.ICg4MFN0pKxB-V1rOSRN924QGalUixqO_43DFfPCjDAg.vaAjwII25RsrIxZ_lMhqZTa6MtSvux47hR96Skpzt8Ig.JPEG/SE-d88b3a07-f226-4d61-abb3-3c4b6e3d31d4.jpg"

# file path and file name to download
outpath = "../media/"
outfile = "test.png"

# Create when directory does not exist
if not os.path.isdir(outpath):
    os.makedirs(outpath)

# download
urllib.request.urlretrieve(url, outpath+outfile)
print("complete!")
