#!/bin/bash
set -e -o xtrace

pip install --upgrade hypothesis-extra/hypothesis-datetime/
pip install --upgrade hypothesis-extra/hypothesis-fakefactory/
pip install --upgrade hypothesis-extra/hypothesis-pytest/
pip install --upgrade hypothesis-extra/hypothesis-django/
python -m pytest --capture=no --strict tests/
python -m pytest --capture=no --strict hypothesis-extra/*/tests/
for f in hypothesis-extra/*/manage.py; do
    d=$(dirname $f)
    pushd $d
        python manage.py test
    popd
done
