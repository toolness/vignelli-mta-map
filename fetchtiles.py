import os
import urllib2

NUM_ROWS = 14
TILES_PER_ROW = 14
BASE_URL = "http://www.mta.info/weekender/images/subwaytiles/15_%s"
TILES_DIR = os.path.join(os.path.dirname(__file__), "tiles")

if not os.path.exists(TILES_DIR):
    os.mkdir(TILES_DIR)

for y in range(NUM_ROWS):
    for x in range(TILES_PER_ROW):
        filename = "%s_%s.png" % (x, y)
        dest_filename = os.path.join(TILES_DIR, filename)
        if os.path.exists(dest_filename):
            print "skipping %s" % filename
        else:
            print "fetching %s" % filename
            src = urllib2.urlopen(BASE_URL % filename)
            dest = open(dest_filename, "wb")
            dest.write(src.read())
