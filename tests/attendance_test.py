import os
import subprocess
from datetime import date
from urllib.request import urlopen
from pathlib import Path


base_url = "https://raw.githubusercontent.com/chu-ise/assignment-template/main/assets"


def test_attendance():
    today = date.today().strftime("%Y%m%d")
    attendance_file = f"./attendance/{today}.txt"
    repo = get_reponame()
    url = f"{base_url}/{repo}.seed"
    seed = urlopen(url).read().decode("utf-8").strip()
    if len(seed) > 0:
        with open(attendance_file) as f:
            your_seed = f.readline().strip()

        assert your_seed == seed


def find_homework(filename):
    for path in Path("homework").rglob(filename):
        if Path(filename).name == path.name:
            print(f"found {filename} at {path}")
            return True
    return False


def get_reponame():
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE
    )
    repo = result.stdout.decode("utf-8").strip()
    repo = os.path.basename(repo)
    repo = "-".join(repo.split("-")[:2])
    return repo


if __name__ == "__main__":
    repo = get_reponame()
    print(repo)
    print(find_homework("dummy/dummy"))
