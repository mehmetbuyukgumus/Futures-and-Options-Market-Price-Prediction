#/bin/bash
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

source myenv/bin/activate
pip install -r requirements.txt