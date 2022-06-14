import math
import os
import sys
import requests


def greet(person):
    greeting = f"Hello {person}"
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
