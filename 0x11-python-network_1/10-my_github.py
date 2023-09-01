#!/usr/bin/python3
"""A script that:
    - takes your GitHub credentials (username and password)
    - uses the GitHub API to display your id
    """
    import sys
    import requests
    from requests.auth import HTTPBasicAuth


    if _name_ == "_main_":
            auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
                r = requests.get("https://api.github.com/user", auth=auth)
                    print(r.json().get("id"))
