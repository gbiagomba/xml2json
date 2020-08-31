# xml2json
Quick script to convert xml to json, was originally writen to convert nmap xml files to json (think -oJ)


## Installation
```
pip3 install -r requirements.txt
```

## Usage
```
xml2json.py /path/to/nmap/xml/file.xml
```

### Sample Output
```
{
    "nmaprun": {
        "@args": "nmap -sSUV -F -T4 -oX nmap_output example.com",
        "@scanner": "nmap",
        "@start": "1598903536",
        "@startstr": "Mon Aug 31 19:52:16 2020",
        "@version": "7.80",
        "@xmloutputversion": "1.04",
        "debugging": {
            "@level": "0"
        },
        "host": {
            "@endtime": "1598903944",
            "@starttime": "1598903536",
            "address": {
                "@addr": "93.184.216.34",
                "@addrtype": "ipv4"
            },
            "hostnames": {
                "hostname": {
                    "@name": "example.com",
                    "@type": "user"
                }
            },
            "ports": {
                "extraports": [
                    {
                        "@count": "99",
                        "@state": "open|filtered",
                        "extrareasons": {
                            "@count": "99",
                            "@reason": "no-responses"
                        }
                    },
                    {
                        "@count": "98",
                        "@state": "filtered",
                        "extrareasons": {
                            "@count": "98",
                            "@reason": "no-responses"
                        }
                    }
                ],
                "port": [
                    {
                        "@portid": "80",
                        "@protocol": "tcp",
                        "service": {
                            "@conf": "10",
                            "@extrainfo": "sec/9717",
                            "@method": "probed",
                            "@name": "http",
                            "@product": "Edgecast CDN httpd"
                        },
                        "state": {
                            "@reason": "syn-ack",
                            "@reason_ttl": "57",
                            "@state": "open"
                        }
                    },
                    {
                        "@portid": "443",
                        "@protocol": "tcp",
                        "service": {
                            "@conf": "10",
                            "@extrainfo": "sec/9704",
                            "@method": "probed",
                            "@name": "http",
                            "@product": "Edgecast CDN httpd",
                            "@tunnel": "ssl"
                        },
                        "state": {
                            "@reason": "syn-ack",
                            "@reason_ttl": "57",
                            "@state": "open"
                        }
                    },
                    {
                        "@portid": "443",
                        "@protocol": "udp",
                        "service": {
                            "@conf": "3",
                            "@method": "table",
                            "@name": "https",
                            "@servicefp": "SF-Port443-UDP:V=7.80%I=7%D=8/31%Time=5F4D54FE%P=x86_64-pc-linux-gnu%r(DTLSSessionReq,29,\"pWT:\\x83\\xdd=\\xb4\\xedc\\xab\\xb2\\xec\\xfb\\x15\\xf7\\x84\\xe6!\\x1a{\\x1b\\x11\\x86\\xe7ZJv%\\x11\\x83\\x0b7\\xd3\\x98e\\xd7Y\\xf7/\\0\")%r(RPCCheck,29,\"p2W\\x9a4\\x92u\\x8c\\x04\\xc5\\xfc\\x87\\x9c\\x0cI\\xa0\\x90\\x0e9\\xf6Vq\\xd5\\xcb\\xf2\\x9f\\xc79\\xe2\\xa4\\xfe\\xfc\\xb6\\xd3\\x98e\\xdf\\x80@\\xeb\\x97\")%r(DNSVersionBindReq,29,\"pk,\\xdfM\\+M>V\\$\\xcdnq\\xe5\\xef#\\xeaJ\\xd4\\x8b\\x1a\\x8a>\\xeds\\t\\xb4\\xf8\\xa2\\xf6\\xe9\\xb5\\]Q\\x99e\\xa1\\xf6\\|\\n\\x80\")%r(SIPOptions,29,\"p\\xb9\\xaan\\xf3=r\\xa2\\xac!fO\\xd9\\xbe\\xb8!\\xd7\\xe7\\xe4\\xbf\\xb8\\xed\\xa27\\x8e\\x03\\xb7\\x20\\x17\\xfdc\\x93k\\xff\\x9ae\\xb3\\x20w\\xf9\\xd1\")%r(SNMPv1public,29,\"p\\xc9\\xff\\xe7\\x888\\xcf\\x9alH/\\xe0\\xe7\\xdf\\x10\\xben3\\xb8\\x1d\\xe83X\\xb2H\\x1d\\xb4\\x03\\x19\\xc2\\.\\xeb\\xc5\\xc5\\x96eZ\\x9a\\x7fE\\xd9\")%r(SNMPv3GetRequest,29,\"p\\x15\\xdds\\xce\\|p\\*L\\\\\\x85\\n\\x9fH\\xbe\\xf2\\xcd\\x9c\\x06S\\xba\\xbfe\\xdf\\xfd\\x84\\x13\\xb6\\xae\\x1d\\xb0\\xbc\\xa18\\x9aeDbC\\xe6\\x10\")%r(AFSVersionRequest,29,\"p\\xcf\\x93\\xeb\\xd0\\xa6\\?}\\x97d\\x91\\xc1\\x87}\\x15\\x9d\\x1aF\\xecN\\r\\x04\\xa3\\xe0G\\x8b\\xfe\\+2<u;\\xd7\\[\\x99e\\xc5T\\xd9'\\\\\")%r(DNS-SD,29,\"p_\\x01o\\xb4@\\x1f\\\"<\\xbe\\xbb%\\x02P\\xb0\\xb6\\x18A\\xa0\\x82;\\xccu\\xc8\\]\\|\\x86v\\x03\\\\\\xda}\\xe4\\[\\x99exBN\\)\\x9d\")%r(Citrix,31,\"\\x0e\\0\\x010\\x02\\xfd\\xa8\\xe3\\0PRST\\x02\\0\\0\\0RNON\\x08\\0\\0\\0CADR\\x10\\0\\0\\0\\xb5i\\x0f\\0\\0\\0\\0\\0\\x02\\0`v\\xf1\\+\\xc8\\x86\")%r(Kerberos,29,\"p\\xafB\\xc7\\xc3x5J\\x96\\xbb\\xf3F\\x8du\\xe7\\xae\\xb2\\xcf\\xd4\\x82\\x80\\xbb\\xc1\\x92\\x8d\\(\\x83\\xb3\\x11\\xaccP\\x93\\xb5\\x96e\\xa6\\(\\x97F\\xe3\")%r(NetMotionMobility,29,\"pT\\xda\\xa1\\xf0\\x0e,4\\x92\\x8e\\xb4tP!\\xcd\\xd0\\x07\\x99\\xcf>;\\x1f\\xe2s\\xc7/r\\x98\\x05\\$~\\xd0\\x01\\xad\\x9ae\\xe39\\x95\\x9d\\xa6\");"
                        },
                        "state": {
                            "@reason": "udp-response",
                            "@reason_ttl": "54",
                            "@state": "open"
                        }
                    }
                ]
            },
            "status": {
                "@reason": "echo-reply",
                "@reason_ttl": "54",
                "@state": "up"
            },
            "times": {
                "@rttvar": "5969",
                "@srtt": "6579",
                "@to": "100000"
            }
        },
        "runstats": {
            "finished": {
                "@elapsed": "407.82",
                "@exit": "success",
                "@summary": "Nmap done at Mon Aug 31 19:59:04 2020; 1 IP address (1 host up) scanned in 407.82 seconds",
                "@time": "1598903944",
                "@timestr": "Mon Aug 31 19:59:04 2020"
            },
            "hosts": {
                "@down": "0",
                "@total": "1",
                "@up": "1"
            }
        },
        "scaninfo": [
            {
                "@numservices": "100",
                "@protocol": "tcp",
                "@services": "7,9,13,21-23,25-26,37,53,79-81,88,106,110-111,113,119,135,139,143-144,179,199,389,427,443-445,465,513-515,543-544,548,554,587,631,646,873,990,993,995,1025-1029,1110,1433,1720,1723,1755,1900,2000-2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000-6001,6646,7070,8000,8008-8009,8080-8081,8443,8888,9100,9999-10000,32768,49152-49157",
                "@type": "syn"
            },
            {
                "@numservices": "100",
                "@protocol": "udp",
                "@services": "7,9,17,19,49,53,67-69,80,88,111,120,123,135-139,158,161-162,177,427,443,445,497,500,514-515,518,520,593,623,626,631,996-999,1022-1023,1025-1030,1433-1434,1645-1646,1701,1718-1719,1812-1813,1900,2000,2048-2049,2222-2223,3283,3456,3703,4444,4500,5000,5060,5353,5632,9200,10000,17185,20031,30718,31337,32768-32769,32771,32815,33281,49152-49154,49156,49181-49182,49185-49186,49188,49190-49194,49200-49201,65024",
                "@type": "udp"
            }
        ],
        "taskprogress": [
            {
                "@etc": "1598907263",
                "@percent": "1.96",
                "@remaining": "3650",
                "@task": "Service scan",
                "@time": "1598903613"
            },
            {
                "@etc": "1598904143",
                "@percent": "32.35",
                "@remaining": "408",
                "@task": "Service scan",
                "@time": "1598903735"
            },
            {
                "@etc": "1598903900",
                "@percent": "90.20",
                "@remaining": "36",
                "@task": "Service scan",
                "@time": "1598903865"
            },
            {
                "@etc": "1598903950",
                "@percent": "90.20",
                "@remaining": "41",
                "@task": "Service scan",
                "@time": "1598903910"
            }
        ],
        "verbose": {
            "@level": "0"
        }
    }
}
```