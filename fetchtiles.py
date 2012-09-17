import os
import urllib2
import time

NUM_ROWS = 14
TILES_PER_ROW = 14
BASE_URL = "http://www.mta.info/weekender/images/subwaytiles/15_%s"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TILES_DIRNAME = "tiles"
TILES_DIR = os.path.join(ROOT_DIR, TILES_DIRNAME)
APPCACHE_FILENAME = os.path.join(ROOT_DIR, "map.appcache")

if not os.path.exists(TILES_DIR):
    os.mkdir(TILES_DIR)

appcache = open(APPCACHE_FILENAME, "w")
appcache.write('CACHE MANIFEST\n')
appcache.write('# %s\n' % time.asctime())
appcache.write('index.html\n')

for y in range(NUM_ROWS):
    for x in range(TILES_PER_ROW):
        filename = "%s_%s.png" % (x, y)
        dest_filename = os.path.join(TILES_DIR, filename)
        appcache.write('%s/%s\n' % (TILES_DIRNAME, filename))
        if os.path.exists(dest_filename):
            print "skipping %s" % filename
        else:
            print "fetching %s" % filename
            src = urllib2.urlopen(BASE_URL % filename)
            dest = open(dest_filename, "wb")
            dest.write(src.read())

appcache.close()
