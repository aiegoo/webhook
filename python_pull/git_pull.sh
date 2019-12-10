#!/bin/bash

cd /root/repos/$1 && git fetch --all && git checkout --force "origin/master"
