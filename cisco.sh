#!/bin/bash

for url in $(cat cisco.txt);do
host $url |grep "has address" | cut -d" " -f4
done
