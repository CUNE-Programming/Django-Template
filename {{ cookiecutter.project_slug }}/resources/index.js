import 'vite/modulepreload-polyfill'
{% if cookiecutter.css != "tailwind" %}import "./scss/index.scss"{% endif %}
{% if cookiecutter.stack == "THAD" -%}
Promise.all([
    import("htmx.org"),
    import("alpinejs"),
    {% if cookiecutter.css == "bootstrap" %}import("bootstrap"){% endif %}
]).then(
    ([{ default: htmx }, { default: Alpine }{% if cookiecutter.css == "bootstrap" %}, _ {% endif %}]) => {
        window.htmx = htmx;
        window.Alpine = Alpine
        Alpine.start()
    }
)
{%- endif -%}
{% if cookiecutter.stack == "DIRT" -%}
import { createInertiaApp } from "@inertiajs/react"
import { createRoot } from "react-dom/client"
import axios from "axios";
{% if cookiecutter.css == "bootstrap" -%}import * as bootstrap from "bootstrap"{%- endif %}

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = "csrftoken"

createInertiaApp({
    resolve: name => {
        const pages = import.meta.glob("./pages/**/*.jsx", { eager: true });
        return pages[`./pages/${name}.jsx`]
    },
    setup: ({ el, App, props }) => {
        createRoot(el).render(<App {...props} />)
    }
})
{%- endif -%}