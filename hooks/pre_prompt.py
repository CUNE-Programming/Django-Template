from os import system, exit
from platform import system as platform
from shutil import which

if which("poetry") is None:
    while (install := input("Poetry not found. Install Poetry.").lower()) not in [
        "y",
        "n",
    ]:
        print("Please enter y or n.")
    if install == "y":
        user_platform = platform()
        match user_platform:
            case "Windows":
                system(
                    "(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -"
                )
                print("Please restart your computer, and retry the command")
                exit(0)
            case _:
                system(
                    "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -"
                )
                print("Please restart your computer, and retry the command")
                exit(0)

system("poetry config virtualenvs.in-project true")
