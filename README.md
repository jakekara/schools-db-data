# CT Mirror | Your School data sets

In order to combine all of these data sets from different sources into one
profile page for Your School, we had to match schools based on the school’s
name, the district, and special numeric codes the state uses whenever the
data sets had them. We rely on automated techniques to match these
different data sets, and sometimes a small number of schools can’t be
matched up.

This repository contains the raw data used for each and the code we wrote
to restructure and transform the data to work with our database.

Here are notes on each data set in the order the data appear in the school
profile page:

#### Who goes here?

These sparkline tables show student enrollment by race over time.

* The raw files came from [EdSight](http://edsight.ct.gov). They are in the [raw](raw) folder, titled
"EnrollmentYearExport-YYYY-YY-Race.csv" where YYYY-YY is the school year.

* The Jupyter notebook [Enrollment subgroup
trendsheets](pandas/Enrollment%20subgroup%20trendsheets.ipynb) contains the
code to combine all of these years of data and export them to:

* The file [clean/for_db/enrollment_trend_race.csv](clean/for_db/enrollment_trend_race.csv)

#### Who teaches here?

Student race data is based on above, while teacher race data comes from
EdSight as well.

* The raw data files are in the [raw](raw) folder, named
  StaffingRace-yy-yy.csv, where yy-yy is the school year.
  
* The Jupyter notebook [pandas/Staff%20race.ipynb](pandas/Staff%20race.ipynb)
  combines these files into
  [clean/csv/staff_race.csv](clean/csv/staff_race.csv)

#### English language learners

ELL enrollment is also from EdSight.

* Single year files are in the [raw](raw) folder, named
  EnrollmentYearExport-YYYY-YY-ELL.csv where YYYY-YY is the school year.

* The [same notebook used to create the race trend
  sheets](pandas/Enrollment%20subgroup%20trendsheets.ipynb), meaning
  multi-year spreadsheets, is also used to create the ELL trend sheet,
  which is in
  [clean/csv/enrollment-trend-ell.csv](clean/csv/enrollment-trend-ell.csv]

