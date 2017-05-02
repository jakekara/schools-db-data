import requests
COOKIE="1fc2dae290ceccd1789c0e0db17caeed_Cluster1=B3DA455308B0ECA2E999FB0D23C4A769.1fc2dae290ceccd1789c0e0db17caeed_SASServer1_1; _ga=GA1.2.673144756.1485291994; 1fc2dae290ceccd1789c0e0db17caeed_Cluster1=DCE4A0DFF7CA0734E4B5B10307082FDB.1fc2dae290ceccd1789c0e0db17caeed_SASServer1_1"

def year(yint):
    return "20" + str(yint).zfill(2) + "-" + str(yint + 1).zfill(2)

def url(year, subg):
    return "http://edsight.ct.gov/SASStoredProcess/do?_program=/CTDOE/EdSight/Release/Reporting/Public/Reports/StoredProcesses/SmarterBalancedAssessmentExport&_year="+year+"&_district=All+Districts&_subgroup="+subg+"&_school=All+Schools&_subject=ELA+and+Math&_grade=All+Grades+Combined"


subgroups=["All+Students","Race","Gender","Special Education","Free/Reduced Price Meal Eligibility (2-level)","Free/Reduced Price Meal Eligibility (3-level)",
           "ELL","High Needs (F, R, ELL or SWD)"]

for y in range(14,16):
    for g in subgroups:
        print url(year(y), g)
        open("scraped/sbac-" + year(y) + "-" + g.replace("/","-") + ".csv","w").write(requests.get(url(year(y), g),headers={"Cookie":COOKIE}).content)
        print year(y), g
    
