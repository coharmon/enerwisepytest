import requests
import json
from settings.token_settings import *
from settings.generate_token import *
from utils.header import url_header

def test_GetMaStudyCasesPJM():
    response = url_header.get_response("/DerApi/MonthlyAllocation/GetMaStudyCases?siteId=36", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['studyYear'] == 2024
 
def test_GetMaStudyCasesISO():
    response = url_header.get_response("/DerApi/MonthlyAllocation/GetMaStudyCases?siteId=54", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['studyYear'] == 2023
    

def test_CreateMACase():

    payload = json.dumps({
        "siteId": 4,
        "periodType": 0,
        "studyYear": 2022,
        "periodLength": 30,
        "isUploadDataUsed": False,
        "siteCommissionStart": "2024-06-01T00:00:00-04:00",
        "siteCommissionEnd": "2025-05-31T00:00:00-04:00",
        "name": "chtest092123a",
        "useBaseDateAlgo": True,
        "basePeriodStart": "2022-09-21T11:39:13-04:00",
        "basePeriodEnd": "2023-09-20T11:39:13-04:00",
        "start": "2022-09-21T11:39:13-04:00"
        })

    response = url_header.post_response("/DerApi/MonthlyAllocation/CreateStudyCase", path2, headers, payload)
    assert response.status_code == 200
    #assert response.text == 0
   
def test_GetAutoBasePeriods():

    payload = json.dumps({
        "siteId": 36,
        "periodType": 0,
        "studyYear": 2022,
        "periodLength": 30,
        "isUploadDataUsed": False,
        "siteCommissionStart": "2024-06-01T00:00:00-04:00",
        "siteCommissionEnd": "2025-05-31T00:00:00-04:00",
        "name": "chtest092123a",
        "useBaseDateAlgo": True
        })

    response = url_header.post_response("/DerApi/MonthlyAllocation/GetAutoBasePeriods", path2, headers, payload)
    assert response.status_code == 200
    #assert response.text == 0