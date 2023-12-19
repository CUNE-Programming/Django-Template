""" Post generation hook for cookiecutter template. """ ""

# Imports
from pathlib import Path
from os import system
from json import load
from shutil import which
from platform import system as platform

# Cookiecutter variables
stack = "{{ cookiecutter.stack }}"
css = "{{ cookiecutter.css }}"
init_git: bool = {{cookiecutter.init_git}}
install_packages: bool = {{cookiecutter.install_packages}}
install_extensions: bool = {{cookiecutter.install_extensions}}

# Create .env file
Path(".env").write_text(
    "DEBUG=on\n" 'SECRET_KEY="secret"\n' "DATABASE_URL=sqlite:///dev.sqlite\n"
)

# Handle stack updates
match stack:
    case "THAD":
        Path("resources/js").mkdir()
    case "DIRT":
        Path("resources/pages").mkdir()
        Path("resources/components").mkdir()
        Path("resources/hooks").mkdir()

# Handle CSS updates
match css:
    case "tailwind":
        Path("resources/scss/index.scss").unlink()
        Path("resources/scss").rmdir()
    case _:
        Path("tailwind.config.mjs").unlink()
        Path("postcss.config.cjs").unlink()
        Path("resources/css/tailwind.css").unlink()
        Path("resources/css").rmdir()

# Install things if chosen
if install_packages:
    if which("npm") is None:
        print("NPM not found. Skipping package installation.")
    else:
        system("npm install")
        system("npx biome format package.json")
    system("poetry install --no-root")

if install_extensions:
    if which("code") is None:
        print("VSCode not found. Skipping extension installation.")
    else:
        extensions = load(Path(".vscode/extensions.json").open())["recommendations"]
        for recommendation in extensions:
            system(f"code --install-extension {recommendation} --force")

if init_git:
    system("git init")
    system("git branch -m main")

    if platform() != "Windows":
        system("./.venv/bin/pre-commit install")

    else:
        system("./.venv/Scripts/pre-commit.exe install")

    system("git add .")

    while (first_commit := input("Create first commit? [y/n] ").lower()) not in [
        "y",
        "n",
    ]:
        print("Please enter 'y' or 'n'")
    if first_commit == "y":
        system('git commit -m ":rocket: Initial commit"')

else:
    Path(".gitignore").unlink()
    Path(".gitattributes").unlink()
    Path(".pre-commit-config.yaml").unlink()
