import subprocess
import os
import time
import glob
import json

photoshop_path = r"C:\Program Files\Adobe\Adobe Photoshop 2025\Photoshop.exe"
arw_files = glob.glob(r"D:\photos\sony_a6000\raw_test\*.ARW")

with open("queue.json", "w") as f:
    json.dump({"files": arw_files}, f)

try:
    process = subprocess.Popen([photoshop_path])
    print('Opening Photoshop...')

except FileNotFoundError:
    print(f'Error: Could not find Photoshop at {photoshop_path}')
    print('Please check the path and try again.')


