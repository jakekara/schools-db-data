#!/bin/sh
#
# Make absenteeism data 
#
# Requires file:
# chronic_absenteeism_ell.csv
# chronic_absenteeism_frpl.csv
# chronic_absenteeism_gender.csv
# chronic_absenteeism_grade.csv
# chronic_absenteeism_race_ethnicity.csv
# chronic_absenteeism_special_ed.csv
#

try_kilgore()
{
    kilgore --skiprows $2 -i $1 --pretty\
	    --load clean_code_columns\
	    --load airtables > $3
}

mkdir -p brute/csv/
clean_abs()
{
    echo "cleaning $1"
    bn=$(basename $1)
    justname=$(echo $bn | cut -f 1 -d '.')

    try_kilgore $1 4 brute/csv/$justname.csv

    # kilgore --skiprows 4 -i $1 --pretty\
    # 	    --load clean_code_columns\
    # 	    --load airtables > brute/csv/$justname.csv

    # If it's empty, try it with 5 skip rows
    if [ -s brute/csv/$justname.csv ]
    then
	echo ""
    else
	try_kilgore $1 5 brute/csv/$justname.csv
	# kilgore --skiprows 5 -i $1 --pretty\
	# 	--load clean_code_columns\
	# 	--load airtables > brute/csv/$justname.csv
    fi

    # If it's empty, try it with 6 skip rows
    if [ -s brute/csv/$justname.csv ]
    then
	echo ""
    else
	try_kilgore $1 6 brute/csv/$justname.csv
	# 	kilgore --skiprows 6 -i $1 --pretty\
	# 		--load clean_code_columns\
	# 		--load airtables > brute/csv/$justname.csv
	# fi

	# If it's empty, try it with 7 skip rows
	if [ -s brute/csv/$justname.csv ]
	then
	    echo ""
	else
	    try_kilgore $1 7 brute/csv/$justname.csv
	    kilgore --skiprows 7 -i $1 --pretty\
		    --load clean_code_columns\
		    --load airtables > brute/csv/$justname.csv
	fi



	# If it's empty, try it with delete it
	if [ -s brute/csv/$justname.csv ]
	then
	    echo ""
	else
	    rm brute/csv/$justname.csv
	fi
   fi
}

for fname in noequals/*.csv
do
    # echo $bn $justname
    clean_abs $fname
done

