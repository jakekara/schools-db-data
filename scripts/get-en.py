import requests, json
# May need to update this periodically
COOKIE="1fc2dae290ceccd1789c0e0db17caeed_Cluster1=1074512B20713BBA007194AD0E3C3084.1fc2dae290ceccd1789c0e0db17caeed_SASServer1_1; _ga=GA1.2.673144756.1485291994; 1fc2dae290ceccd1789c0e0db17caeed_Cluster1=DCE4A0DFF7CA0734E4B5B10307082FDB.1fc2dae290ceccd1789c0e0db17caeed_SASServer1_1"

OUTDIR="scraped"
LOGFILE = "log.json"

log = {}

def load_log():
    global log

    try:
        log = json.loads(open(LOGFILE,"r").read())
    except:
        printf("Could not load ", LOGFILE)

    print log

def save_log():
    global log
    try:
        open(LOGFILE, "w").write(json.dumps(log))
    except:
        printf("Could not save ", logfile)
    

#
# args: year (YYYY-YY format)
#       subgroup
#
def get_enrollment(report, ystr, subg):

    global log
    
    if report + ":" + ystr + ":" + subg in log:
        return
    
    url="http://edsight.ct.gov/SASStoredProcess/do?_program=/CTDOE/EdSight/Release/Reporting/Public/Reports/StoredProcesses//"+report+"&_year="+ystr+"&_district=All+Districts&_school=All+Schools&_subgroup="+subg+"&display=1"

    resp = requests.get(url, headers={"Cookie":COOKIE})

    if resp.status_code == 200:
        if "The query you have run did not contain any results" in resp.content:
            print "Dud: " + report + "-" + ystr + "-" + subg 
        else:
            pass
            # open(OUTDIR + "/" + report + "-" + ystr + "-" + subg + ".csv".replace(" ",""),"w").write(resp.content)
    else:
        print "Error downloading" , ystr, subg
        print resp.status_code

    log[report + ":" + ystr + ":" + subg] = resp.status_code
    save_log()

    return resp.content

    

# get_enrollment ("2016-17", "All+Students")
# get_enrollmednt 2016-17 Race
# get_enrollment 2016-17 Gender
# get_enrollment 2016-17 "Special+Education"
# get_enrollment 2016-17 "Lunch"
# get_enrollment 2016-17 "ELL"
# get_enrollment 2016-17 "Grade"


reports =  ["EnrollmentYearExport"]# "SuspensionRateExport",

subgroups = ["Race","Gender","Special+Education+","Lunch", "ELL","Grade", " ", "SpEd" ]

report_list = {
    # "EnrollmentYearExport":{
    "SuspensionRateExport":{
        "subgroups":{
            "all":" ",
            "race":"Race ",
            "ell":"ELL ",
            "gender":"Gender ",
            "frpl":"Lunch ",
            "sped":"SpEd "
        },
        "years":["Trend"]
    }
}

for r in report_list:
    report = report_list[r]
    # for yint in [0]: # + range(07,17):
    for ystr in report["years"]:
        for s in report["subgroups"]:
            subg = report["subgroups"][s]
            print r, ystr, subg
            open("scraped/" + r + "-" + ystr + "-" + s + ".csv",
                 "w")\
                 .write(get_enrollment(r, ystr, subg))

