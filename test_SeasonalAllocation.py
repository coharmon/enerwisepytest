import requests
import json
from settings.token_settings import *
from settings.generate_token import *
from utils.header import url_header

def test_GetCPPrice():
    response = url_header.get_response("/DerApi/SeasonalAllocation/GetCPPrice?studyCaseId=80", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['summerPLC'] == 428.3000

def test_GetSaStudyCases():  
    response = url_header.get_response("/DerApi/SeasonalAllocation/GetSaStudyCases?siteId=19", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['studyYear'] == 2023
    
def test_PostCreateStudyCase():

    payload = json.dumps({
        "siteId": 5,
        "studyYear": 2025,
        "name": "AutoTest 2025"
    })

    response = url_header.post_response("/DerApi/SeasonalAllocation/CreateStudyCase", path2, headers, payload)
    assert response.status_code == 200
    #assert response.text == 0


def test_PostCalculateAssetsSettlement():

    payload = json.dumps({
        "capLimitSummer": 400.95487736378954,
        "capLimitWinter": 400.95487736378954,
        "assets": [
            {
            "id": "51f7f3a6-851f-45ac-abd8-288b21862cd6",
            "maxSummerCapability": 100,
            "maxWinterCapability": 100,
            "isAdjustable": False,
            "summerBenefitPerKw": 108,
            "winterBenefitPerKw": 100
            }
        ]
        })
            
    response = url_header.post_response("/DerApi/SeasonalAllocation/CalculateAssetsSettlement", path2, headers, payload)
    assert response.status_code == 200
    d = json.loads(response.text)
    assert d['assets'][0]['winterBenefit'] == 10000