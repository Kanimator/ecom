# Ark Computing Django Site

## Install
```bash
git clone https://github.com/darthnall/arkcomputing-site
cd arkcomputing-site/
```

### MacOS
`source ./install-macos.zsh`

### Linux
`source ./install-linux.sh`


## Run local server
```bash
source .venv/bin/activate # If you aren't already in the virtual environment
python manage.py runserver
```

## Run tailwindcss
```bash
npx tailwindcss -i ./global_static/css/input.css -o ./global_static/css/main.css --watch
```
