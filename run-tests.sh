#!/bin/bash

set -e

OAREPO_VERSION=${OAREPO_VERSION:-11}

if [ -d .venv-builder ] ; then
    rm -rf .venv-builder
fi

python3 -m venv .venv-builder
.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install oarepo-model-builder oarepo-model-builder-drafts
.venv-builder/bin/pip install pytest-invenio

BUILDER=.venv-builder/bin/oarepo-compile-model

if [ -d built_tests ] ; then
    rm -rf built_tests
fi

mkdir built_tests

if true ; then
    test -d model && rm -rf model
    ${BUILDER} tests/model_record.yaml --output-directory built_tests/model -vvv --profile record,draft
fi

if [ -d .venv-tests ] ; then
    rm -rf .venv-tests
fi

python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install "oarepo[tests]==$OAREPO_VERSION.*"
pip install -e "built_tests/model[tests]"

pytest tests