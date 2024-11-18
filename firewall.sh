#!/bin/sh
cd pox
RULES_FILE="./ext/rules.json"
sudo ./pox.py log.color log.level --DEBUG firewall --config_file=$RULES_FILE