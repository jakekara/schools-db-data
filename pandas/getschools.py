#
#
#

import pandas as pd

import requests
import re

apiurl = "http://localhost:8000/cdata"
cached = None
cached_drg = None
caches = {}

def get_recordset(rs):

    global cached
    if rs not in caches:
        caches[rs]  = requests.get( apiurl + "/dataset/" + rs).json()

    return caches

def get_schools():

    global cached
    if cached == None:
        cached = requests.get( apiurl + "/dataset/schools").json()

    return cached

def get_drgs():

    global cached_drg
    if cached_drg == None:
        cached_drg = requests.get( apiurl + "/dataset/drg").json()

    return cached_drg


def test_match ( record, k, val ):

    if record is None:
        return False

    if k not in record:
        return False
    
    return record[k].upper().strip() == val.upper().strip()

def test_contains ( record, k, val ):

    if record is None:
        return False

    if k not in record:
        return False
    
    return val.upper() in record[k].upper()

def lookup_exact( key, val, rset=get_schools() ):
    return filter( lambda x: test_match(x, key, val), rset)

def lookup_contains( key, val, rset=get_schools() ):
    return filter( lambda x: test_contains(x, key, val), rset)

def lookup_both( dist, sch ):
    in_district = lookup_exact( "district", dist )

    return lookup_exact( "school", sch, rset=in_district)

def merge_01( df ):

    ret = df.copy()

    row0 = ret.iloc[0].fillna(method="ffill")
    row1 = ret.iloc[1].fillna("")

    cols = []
    for i in range(len(row0)):
        if row0[i] is None:
            cols.append(str(row1[i]))
        else:
            cols.append(str(row0[i]) + "_" + str(row1[i]))
            
            cols = map(lambda x: x.replace("nan_",""), cols)

    ret = ret.drop(0)
    ret = ret.drop(1)

    ret.columns = cols

    def remove_trail(s):
        s = s.strip()
        if (s[-1] == "_"):
            return s[:-1]
        return s
        
    ret.columns = map(remove_trail, ret.columns)
                                            
    return ret




def add_district_matches( df ):
    if "district" not in df.columns:
        raise Exception("Error: DF must have column'district'")

    ret = df.copy()

    dist_codes = []
    check_dist_col = []

    def distmatch ( obj ):
        if obj is None:
            return False

        if "type" not in obj:
            return False

        if obj["type"] is None:
            return False

        if "district" in obj["type"].lower():
            return True

        return False
        
    for i, r in ret.iterrows():
        dist = r["district"]
        matches = lookup_exact( "district", dist )
        if len(filter(lambda x: distmatch( x ),
                      matches)) == 1:
            dist_codes.append(matches[0]["district_code"])
            check_dist_col.append(matches[0]["district"])
        else:
            dist_codes.append(None)
            check_dist_col.append(None)

    ret["dist_code"] = dist_codes
    ret["check_dist_col"] = check_dist_col

    return ret

def add_exact_matches( df ):

    if "school" not in df.columns or "district" not in df.columns:
        raise Exception("Error: DF must have columns 'school' and 'district'")
    
    ret = df.copy()

    sch_codes = []
    check_sch_col = []
    check_dist_col = []

    for i, r in ret.iterrows():
        sch = r["school"]
        dist = r["district"]
        matches = lookup_both( dist, sch )
        if len(matches) == 1:
            sch_codes.append(matches[0]["school_code"])
            check_sch_col.append(matches[0]["school"])
            check_dist_col.append(matches[0]["district"])

        else:
            sch_codes.append(None)
            check_sch_col.append(None)
            check_dist_col.append(None)

    ret["school_code"] = sch_codes
    ret["check_sch_col"] = check_sch_col
    ret["check_dist_col"] = check_dist_col

    return ret
        

def filldown(df, col_name):
    ret = df.copy()

    ret[col_name] = ret[col_name].fillna(method='ffill')

    return ret

def clean_colnames(df):

    ret = df.copy()

    ret.columns = map(lambda x: re.sub(r'[^a-z0-9]+',
                                       '_',
                                       re.sub(r'%','pct',
                                              x.lower().strip())),
                      ret.columns)

    return ret

def get_district_drg( district_code ):

    return filter(lambda x: x["school_code"] == district_code, get_drgs())
    

def get_drg_or_none( district_code ):

    ret = get_district_drg( district_code )

    if len(ret) < 1 or len(ret) > 1:
        return None

    return ret[0]["drg"]

def get_district_code( school_code ):

    if school_code is None:
        return None

    schools = get_schools()

    # print schools
    matches = filter(lambda x:x["school_code"] == school_code, schools)

    if matches is None or len(matches) != 1:
        return None

    if "district_code" not in matches[0]:
        return None
    
    return matches[0]["district_code"]

def add_district_code(df, code_col="school_code"):
    schools = get_schools()

    ret = df.copy()

    ret["district_code"] = ret.apply(lambda x: get_district_code(x[code_col]), axis=1)

    return ret
    

def add_drg( df, code_col="district_code" ):

    ret = df.copy()
    ret["drg"] = ret.apply(lambda x: get_drg_or_none(x[code_col]), axis=1)

    return ret
