#!/bin/sh

. rmequals.sh

DST=noequals

for fname in ../raw/*
do
    echo $(basename "$fname") $DST/$(basename "$fname")
    rmequals "$fname" > "$DST/$(basename $fname)"
done

