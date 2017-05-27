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
* The Jupyter notebook [Enrollment subgroup trendsheets](pandas/Enrollment%20subgroup%20trendsheets.ipynb) contains the code to combine all of these years of data and export them to:
* The file [clean/for_db/enrollment_trend_race.csv](clean/for_db/enrollment_trend_race.csv)


