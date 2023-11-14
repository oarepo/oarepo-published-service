#!/bin/bash

set -e

if [ -d .venv-builder ] ; then
    rm -rf .venv-builder
fi

python3 -m venv .venv-builder
.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install oarepo-model-builder oarepo-model-builder-drafts
.venv-builder/bin/pip install pytest-invenio

BUILDER=.venv-builder/bin/oarepo-compile-model
MODEL_NAME=model_record

if true ; then
    test -d model && rm -rf model
    ${BUILDER} tests/${MODEL_NAME}.yaml --output-directory model -vvv --profile record,draft
fi

if [ -d .venv-tests ] ; then
    rm -rf .venv-tests
fi

python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install -e model
pip install -e ".[tests]"


pytest tests