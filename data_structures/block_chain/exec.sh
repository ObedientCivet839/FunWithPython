function run_app() {
    python3 app.py
}

function setup_venv() {
    python -m venv venv
}

## Virtual environments
# Needs to run manually in Terminal
function activate() {
    . venv/bin/activate
}
function deactivate() {
    deactivate
}

function reqs() {
    pip freeze > requirements.txt
}

function install_reqs() {
    pip install -r requirements.txt
}

function run() {
    flask run
}

# Run python app.py
# run_app

# Run flask app
python flask_app.py



