
BASE_DIR="$(dirname $0)"
cd ${BASE_DIR}

if [[ ! -d "venv" ]]; then
    virtualenv -p python3
fi

source ./venv/bin/activate
pip install -r requirements.txt
