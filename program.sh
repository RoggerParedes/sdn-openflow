#!/bin/sh

echo "Ejecutando firewall..."
./firewall.sh & > /dev/null 2>&1

echo "Ejecutando topologia con 3 switches..."
./topology.sh 3 > /dev/null 2>&1
