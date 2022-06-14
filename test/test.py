import math
import os
import sys
import requests


print(sys.version)
# print(sys.executable)
def greet(person):
    greeting = f"Hello {person}"
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
