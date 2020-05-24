import os
import json
from os.path import join, exists


def read(path):
    with open(path, 'r') as f:
        return json.load(f)['data']


def write(path, val):
    with open(path, 'w') as f:
        json.dump({'data': val}, f)
