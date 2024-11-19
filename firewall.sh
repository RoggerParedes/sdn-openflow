#!/bin/sh
cd pox
RULES_FILE="ext/rules.json"
sudo python3.8 ./pox.py log.color log.level --DEBUG samples.pretty_log log forwarding.l2_learning firewall --config_file=$RULES_FILE
