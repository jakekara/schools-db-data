#!/bin/sh

rmequals()
{
    cat $1 | sed 's/=//g'
}
