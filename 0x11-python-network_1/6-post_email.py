#!/usr/bin/python3
"""A  script that:
    - takes in a URL and an email address
    - sends a POST request to the passed URL with the email as a parameter
    - displays the body of the response.
    """
    import sys
    import requests


    if _name_ == "_main_":
            url = sys.argv[1]
                value = {"email": sys.argv[2]}

                    r = requests.post(url, data=value)
                        print(r.text)
