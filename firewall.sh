#!/bin/sh

cd pox

sudo ./pox.py log.color log.level --DEBUG firewall --config_file=ext/rules.json
