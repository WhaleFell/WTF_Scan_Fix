from pathlib import Path

ROOTPATH: Path = Path(__file__).resolve().parent


def remove_pycache() -> None:
    for pycache in ROOTPATH.rglob("__pycache__"):
        for file in pycache.iterdir():
            file.unlink()
            print(f"Removed: {file}")
        pycache.rmdir()

    # remove .pyc files
    for pyc in ROOTPATH.rglob("*.pyc"):
        pyc.unlink()
        print(f"Removed: {pyc}")


if __name__ == "__main__":
    remove_pycache()
