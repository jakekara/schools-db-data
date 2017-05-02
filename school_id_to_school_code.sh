#
# rename school_id column with school_code
#

outdir=pdf_scraped_school_code
mkdir -p $outdir

for fname in pdf_scraped/*.csv
do
    echo $fname
    cat $fname | sed '1 s/school_id/school_code/' > $outdir/$( basename $fname)
done
