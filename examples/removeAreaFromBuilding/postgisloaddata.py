#!/usr/bin/python

# Jason Remillard - This file is in the public domain.

import os
import sys

outputFile = "osmdata/massachusetts-latest.osm.bz2"

if ( os.path.isdir("temp") == False) :
  os.mkdir("temp")

os.system("rm temp/*")

# if you are not using debian, these files are probably not at this path.
if (os.system("psql gis -f /usr/share/doc/osmosis/examples/pgsnapshot_schema_0.6.sql")):
  print("Error loading pgsnapshot_schema_0.6.sql into into postGIS gis database.")
  sys.exit(1)

if (os.system("psql gis -f /usr/share/doc/osmosis/examples/pgsnapshot_schema_0.6_linestring.sql")):
  print("Error loading pgsnapshot_schema_0.6_linestring.sql into postGIS gis database.")
  sys.exit(1)

# load osm file into postGIS
if ( os.system("bzcat " + outputFile + " | osmosis --read-xml - --wp user=\"mapping\" database=\"gis\""  ) ) :
  print("Error loading " + outputFile + " into postGIS gis database.")
  sys.exit(1)

print("Success!!")






