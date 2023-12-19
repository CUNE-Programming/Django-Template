# Django Template

## Overview
An opinionated Django Starter Template for use in Concordia University's Programming Team.

The template includes 2 different stacks:
- PHAD (Python, HTMX, Alpine, Django)
- DRIP (Django, React, Inertia.js, Python)

The template also includes 3 different CSS Frameworks:
- TailwindCSS
- Bootstrap
- SpruceCSS

To initialize a project, run
```sh
$ cookiecutter https://github.com/cune-programming/django-template.git
```

## Project Structure

The project utilizes a modified Django project struture to enable faster development by removing decisions. In particular, the template chooses:
- Testing framework (Pytest and Playwright)
- Linting and Formatting (`djlint`, `biome`, `ruff`)

```
<project_name>
| .vscode
    | extensions.json <--- Recommended Extensions
    | settings.json <--- Settings for Project
| apps <--- Location of all Django Apps for the project
    | cpt <--- A helper application for template
| docs <---- A place for project documentation
| project <---- Django Project Settings
    | __init__.py
    | asgi.py
    | settings.py
    | urls.py
    | wsgi.py
| resources <---- Frontend Source Code
    | css <--- Initialized with Tailwind
        | tailwind.css
    | scss <----- Initialized with Bootstrap or Spruce
        | index.scss
    | pages <---- Initilized with DRIP Stack
    | index.js
| static <--- Frontend Build Target
| templates <---- Django Templates
    | application.html
| tests
    | e2e <----- End-to-End Testing with Playwright
        | __init__.py
        | test_example_e2e.py
    | integration <----- Integration testing with Pytest
        | __init__.py
        | test_example.py
    | __init__.py
    | conftest.py <------ Pytest Fixtures
.env
.env.example
.gitattributes
.gitignore
.pre-commit-config.yaml
biome.json
manage.py
package.json
pyproject.toml
readme.md
vite.config.js
```

## Stacks
### PHAD Stack

The default stack for students to use, this puts the focus entirely on backend
development with Django. By utilizing small, but powerful frontend libraries the complexity is far smaller. Students should prefer this stack unless there is a need for more complexity.

To enable interactive and responsive frontends, this templates makes use of
`HTMX` and `alpine.js`.
In addition, `django-htmx` and `django-template-partials` are included to enable better integration with the frontend.

For a real-world example of a similar stack, check out:
- [From React to htmx on a real-world SaaS product: we did it, and it's awesome!](https://youtu.be/3GObi93tjZI?si=kthoQ7ejt3G8aOiX) (They use `Stimulus` instead of `alpine.js`)

### DRIP Stack [Advanced]

The more advanced of the two stacks, its inclusion allows students to advance in knowledge while still staying within the bounds of the team's planning.
By utilizing `inertia.js`, Rich SPA frameworks can be integrated easier than ever before.

This stack initializes an Inertia-powered React frontend for a Django application.
Instead of writing templates, React components will be written.
To enable this, the project includes `inertia-django` as well as a `/pages` directory.

Inertia has been used to great effect in the Laravel and Rails ecosystem, and removes the need for a REST API.

## CSS Frameworks

### TailwindCSS
Tailwind is a powerful utility CSS framework.
With many companies adopting the technology, and its rich growth in the JS space, Tailwind is an important technology for students to be familiar with.
If chosen, the template will initialize tailwind to work within Vite.

This framework should be chosen by students who want to explore frontend design and a richer understanding of CSS.

### Bootstrap
Bootstrap is still the most popular CSS framework, and is simple to get started with.
Students who are not as familiar with good frontend design are encouraged to use this framework, and then build out.
If the DRIP stack is chosen, the template will also include `react-bootstrap`.

The template initializes with a `resources/scss/index.scss` which includes the bootstrap.
This is done intentionally to enable customization of bootstrap and an avenue to learn more about SASS.

### SpruceCSS [Advanced]
This is a powerful SASS-first, low-level CSS framework that only students with a passion for frontend styling should use.
Spruce's inclusion is for students who want to learn more about SASS and advanced web design concepts.

This is not recommended for most or any students, but for those who want to explore web design.

---
Copyright 2023 Ian A. Kollipara
