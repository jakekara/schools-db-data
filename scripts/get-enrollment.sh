# May need to update this periodically
COOKIE="1fc2dae290ceccd1789c0e0db17caeed_Cluster1=F9C520C1C059A7C1FF99D249AC1CC168.1fc2dae290ceccd1789c0e0db17caeed_SASServer1_1; _ga=GA1.2.673144756.1485291994; 1fc2dae290ceccd1789c0e0db17caeed_Cluster1=DCE4A0DFF7CA0734E4B5B10307082FDB.1fc2dae290ceccd1789c0e0db17caeed_SASServer1_1"

#
# args: year (YYYY-YY format)
#       subgroup
#
get_enrollment()
{
    URL="http://edsight.ct.gov/SASStoredProcess/do?_program=/CTDOE/EdSight/Release/Reporting/Public/Reports/StoredProcesses//EnrollmentYearExport&_year=$1&_district=All+Districts&_school=All+Schools&_subgroup=$2&display=1"
    curl $URL --cookie $COOKIE > scraped/enrollment$1-$2.csv
}


get_enrollment 2016-17 "All+Students"
get_enrollment 2016-17 Race
get_enrollment 2016-17 Gender
get_enrollment 2016-17 "Special+Education"
get_enrollment 2016-17 "Lunch"
get_enrollment 2016-17 "ELL"
get_enrollment 2016-17 "Grade"











