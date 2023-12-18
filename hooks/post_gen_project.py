
from pathlib import Path
from os import system

stack = "{{ cookiecutter.stack }}"
css = "{{ cookiecutter.css }}"
init_git = {{ cookiecutter.init_git }}

match stack:
    case 'THAD':
        Path("resources/js").mkdir()
    case 'DIRT':
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

if init_git:
    system("git init")
    system("git branch -m main")