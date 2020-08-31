#! /usr/bin/env python3
# https://avleonov.com/2018/03/11/converting-nmap-xml-scan-reports-to-json/

import json
import xmltodict
import sys

f = open(sys.argv[1])
xml_content = f.read()
f.close()
print((json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True)))
