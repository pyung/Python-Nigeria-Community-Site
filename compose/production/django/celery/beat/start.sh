#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A python_nigeria_site.taskapp beat -l INFO
