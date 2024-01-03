""" Post generation hook for cookiecutter template. """ ""

# Imports
from pathlib import Path
from os import system
from json import load
from shutil import which
from platform import system as platform
from typing import Literal

# Cookiecutter variables
stack: Literal["THAD", "DIRT"] = "{{ cookiecutter.stack }}"
css: Literal["tailwind", "spruce", "bootstrap"] = "{{ cookiecutter.css }}"
init_git: bool = {{cookiecutter.init_git}}
install_packages: bool = {{cookiecutter.install_packages}}
install_extensions: bool = {{cookiecutter.install_extensions}}

# Create .env file
Path(".env").write_text(
    "DEBUG=on\n"
    'SECRET_KEY="secret"\n'
    "DATABASE_URL=sqlite:///dev.sqlite\n"
)

# Handle stack updates
if stack == "THAD":
    Path("resources/js").mkdir()
else:
    Path("resources/pages").mkdir()
    Path("resources/components").mkdir()
    Path("resources/hooks").mkdir()
    Path("apps/cpt/management/commands/createview.py").unlink()
    Path("apps/cpt/templates/cpt/view.html.template").unlink()

# Handle CSS updates
if css == "tailwind":
    Path("resources/scss/index.scss").unlink()
    Path("resources/scss").rmdir()
else:
    Path("tailwind.config.mjs").unlink()
    Path("postcss.config.cjs").unlink()
    Path("resources/css/tailwind.css").unlink()
    Path("resources/css").rmdir()

if install_extensions:
    if which("code") is None:
        print("VSCode not found. Skipping extension installation.")
    else:
        try:
            [
                system(f"code --install-extension {recommendation} --force")
                for recommendation in
                load(Path(".vscode/extensions.json").open())["recommendations"]
             ]
        except Exception:
            print("Error on Reading Recommendations. Please Install Manually.")

# Install things if chosen
if install_packages:
    if which("npm") is None:
        print("NPM not found. Skipping package installation.")
    else:
        system("npm install")
    system("poetry install --no-root")
    system("poetry run playwright install")


if init_git:
    system("git init")
    system("git branch -m main")

    if install_packages:
        if platform() != "Windows":
            system("./.venv/bin/pre-commit install")

        else:
            system("./.venv/Scripts/pre-commit.exe install")

    system("git add -A")

    while (first_commit := input("Create first commit? [y/n] ").lower()) not in ("y", "n",):
        print("Please enter 'y' or 'n'")
    if first_commit == "y":
        system('git commit -m ":rocket: Initial commit"')

else:
    Path(".gitignore").unlink()
    Path(".gitattributes").unlink()
    Path(".pre-commit-config.yaml").unlink()

print("Finished Initializing Project!")
