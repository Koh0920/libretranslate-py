# libretranslate-py

Slim **Ato capsule wrapper** around [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate).
Not a fork — this repo only contains a `capsule.toml` manifest, a `start.py`
entrypoint shim, and `pyproject.toml` / `uv.lock` pinning the upstream package
as a Python dependency. The upstream code is fetched from PyPI at install time.

## Run

```sh
ato run github.com/Koh0920/libretranslate-py
```

Or, if you have **Ato Desktop**, just open:

> <https://ato.run/github.com/Koh0920/libretranslate-py>

The desktop fetches this repository, materializes the uv-managed virtual
environment from `pyproject.toml` + `uv.lock`, and launches LibreTranslate on
`http://127.0.0.1:5001/` inside a sandboxed pane.

By default `start.py` boots with `--load-only ja,en --update-models`. Edit
`start.py` if you want different language pairs.

## Layout

| File | Purpose |
|---|---|
| `capsule.toml` | Ato manifest (runtime=source/python, port=5001) |
| `pyproject.toml` | `libretranslate==1.9.5` pin |
| `uv.lock` | Reproducible deps lockfile |
| `start.py` | Adds `.venv` to `sys.path`, sets argv, calls `libretranslate.main:main()` |

## License

The wrapper files in this repo are MIT. The upstream LibreTranslate package
itself is **AGPL-3.0**; running this capsule pulls and executes that AGPL code.
See [LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) for the upstream license terms.
