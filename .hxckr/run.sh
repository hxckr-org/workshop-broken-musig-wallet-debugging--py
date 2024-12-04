#!/bin/sh
set -e

exec pytest .hxckr/test.py "$@"
