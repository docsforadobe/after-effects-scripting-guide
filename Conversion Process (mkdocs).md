# Conversion Process (mkdocs)

- `pip install mkdocs`
- Copy `./mkdocs.yml` from AE repo into root
- In terminal, `mkdocs serve`


## Deploy

- From the repo:
  - `Settings` > `Pages` > Enable Pages
  - `Deploy from a Branch` > Choose "gh-pages"
- Use `mkdocs gh-deploy` in your terminal to deploy to that ^ branch
