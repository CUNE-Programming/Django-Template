from pathlib import Path
from os import system
from json import load
from shutil import which
from platform import system as platform

stack = "{{ cookiecutter.stack }}"
css = "{{ cookiecutter.css }}"
init_git: bool = {{cookiecutter.init_git}}
install_packages: bool = {{cookiecutter.install_packages}}
install_extensions: bool = {{cookiecutter.install_extensions}}

Path(".env").write_text(
    "DEBUG=on\n" 'SECRET_KEY="secret"\n' "DATABASE_URL=sqlite:///dev.sqlite\n"
)

match stack:
    case "THAD":
        Path("resources/js").mkdir()
    case "DIRT":
        Path("resources/pages").mkdir()
        Path("resources/components").mkdir()
        Path("resources/hooks").mkdir()

match css:
    case "tailwind":
        Path("resources/scss/index.scss").unlink()
        Path("resources/scss").rmdir()
    case _:
        Path("tailwind.config.mjs").unlink()
        Path("postcss.config.cjs").unlink()
        Path("resources/css/tailwind.css").unlink()
        Path("resources/css").rmdir()

if install_packages:
    if which("npm") is None:
        print("NPM not found. Skipping package installation.")
    else:
        system("npm install")
    system("poetry install --no-root")

if install_extensions:
    if which("code") is None:
        print("VSCode not found. Skipping extension installation.")
    else:
        extensions = load(Path(".vscode/extensions.json").read_text())[
            "recommendations"
        ]
        for recommendation in extensions:
            system(f"code --install-extension {recommendation} --force")

if init_git:
    system("git init")
    system("git branch -m main")
    if platform() != "Windows":
        system("./.venv/bin/pre-commit install")
    else:
        system("./.venv/Scripts/pre-commit.exe install")
else:
    Path(".gitignore").unlink()
    Path(".pre-commit-config.yaml").unlink()
