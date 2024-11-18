#!/bin/sh
cd pox
sudo ./pox.py log.color log.level --DEBUG --config_file=ext/rules.json firewall
