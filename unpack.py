from datetime import datetime
import sys, glob, zipfile

year = datetime.today().year
month = datetime.today().month - 1
source = sys.argv[1] # get source e.g. Y:/
destination = sys.argv[2] # get destination

for name in glob.glob(f"{source}ezproxy-{year}{month:02d}*"):
    print(f"Extracting {name}")
    zip = zipfile.ZipFile(name, 'r')
    zip.extractall(destination)
    zip.close()