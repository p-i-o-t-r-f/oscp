#!/bin/bash
for ip in $(seq 200 210); do
ping -c 1 10.22.210.$ip
done
