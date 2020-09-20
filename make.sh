#!/bin/bash
set -e

CMD=$1

case ${CMD} in
test)
  python -m pytest tests/**/*.py
  ;;
unit)
  python -m pytest tests/unit/*.py
  ;;
e2e)
  python -m pytest tests/e2e/*.py
  ;;
lint)
  python -m pylint ./app/*** tests/**/*
  ;;
help)
  @echo "Run test | unit | lint | e2e "
  ;;
esac
