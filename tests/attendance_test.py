import os
from datetime import date
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/chu-ise/assignment-template/main/assets/seed'

def test_attendance():
    today = date.today().strftime("%Y%m%d")
    attendance_file = f"./attendance/{today}.txt"
    if os.path.exists(attendance_file):
        with open(attendance_file) as f:
            your_seed = f.readline().strip()
        seed = urlopen(url).read().decode('utf-8').strip()
        
        assert your_seed == seed