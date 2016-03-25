
BASE_DIR="$(dirname $0)"
cd ${BASE_DIR}

if [[ ! -d "$PWD/venv" ]]; then
    virtualenv -p python3 ./venv
fi

source ./venv/bin/activate
pip install -r requirements.txt
