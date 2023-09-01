#!/usr/bin/python3
"""
requests model
"""

if _name_ == '_main_':
        import requests
            html = requests.get('https://alx-intranet.hbtn.io/status')
                print("Body response:")
                    print("\t- type: {}".format(html.text._class_))
                        print("\t- content: {}".format(html.text))
