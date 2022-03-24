import os
import subprocess
from datetime import date
from urllib.request import urlopen
from pathlib import Path


base_url = "https://raw.githubusercontent.com/chu-ise/assignment-template/main/assets"


def test_homework():
    repo = get_reponame()
    url = f"{base_url}/{repo}.hw"
    homeworks = urlopen(url).read().decode("utf-8").strip().split()
    if len(homeworks) > 0:
        for homework in homeworks:
            if not find_homework(homework):
                assert False, f"{homework} not found"


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
