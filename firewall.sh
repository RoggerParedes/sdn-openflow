#!/bin/sh

cd pox

sudo ./pox.py log.level --DEBUG log.color openflow.of_01 forwarding.l2_learning
