#!/bin/sh
#
# remove duds from scrape results
#

dudstr="'The query you have run did not contain any results.'"

for fname in scraped/*.csv
do
    result=$(egrep "The query" $fname > /dev/null)
    if $match
    then
	echo $? $fname
    fi
done
