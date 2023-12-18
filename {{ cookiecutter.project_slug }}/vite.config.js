import { defineConfig } from "vite"
import { resolve } from "node:path"

export default  defineConfig({
    plugins: [],
    root: resolve("./resources"),
    base: "/static/",
    server: {
        host: "localhost",
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false
        }
    },
    resolve: {
        extensions: [".js", ".ts", {% if cookiecutter.stack == "THAD" %}".jsx", ".tsx",{% endif %}".css",{% if cookiecutter.css != "tailwind" %}".scss", ".sass"{% endif %}]
    },
    build: {
        outDir: resolve("./static"),
        assetDir: "",
        manifest: true,
        emptyOutDir: true,
        rollupOptions: {
            input: {
                main: resolve("./resources/index.js")
            },
            output: {
                chunkFileNames: undefined
            }
        }
    }
})