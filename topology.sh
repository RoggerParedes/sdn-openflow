#!/bin/sh
if [ -z "$1" ]; then
    echo "Uso: ./topology.sh <CANTIDAD DE SWITCHES>"
    exit 1
fi
SWITCHES=$1
sudo mn --custom topology.py --topo chain,$1 --controller remote
