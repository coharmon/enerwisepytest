import requests
import json
from settings.token_settings import *
from settings.generate_token import *
from utils.header import url_header
import pytest

@pytest.mark.tag('int','stage','prod')
def test_Get_SiteData():
    response = url_header.get_response("/DerApi/site/getSite?siteId=2", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['siteId'] == 2
    assert d['siteName'] == "Bowery Farms"

@pytest.mark.tag('int','stage','prod')
def test_Get_BG_Assets():  
    response = url_header.get_response("/DerApi/site/getBgAssets?siteId=12", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['bgName'] == "Chanel008_Generator"

@pytest.mark.tag('int','stage','prod')
def test_Get_Load_Assets():
    response = url_header.get_response("/DerApi/site/getLoadAssets?siteId=2", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['ldName'] == "LD_Cooler"

@pytest.mark.tag('int','stage','prod')
def test_Get_SG_Assets():
    response = url_header.get_response("/DerApi/site/getSGAssets?siteId=19", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['sgName'] == "SLR - 0000000002"

@pytest.mark.tag('int','stage','prod')
def test_Get_Dispatch_Trigger_Threshold_Config():
    response = url_header.get_response("/DerApi/site/GetDispatchTriggerThresholdConfig?siteId=2", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['noPerformanceThresholdPerc'] == 10
    assert d[0]['lowPerformanceThresholdPerc'] == 90   

@pytest.mark.tag('int','stage','prod')
def test_Get_Site_Asset_MarketPrograms():
    response = url_header.get_response("/DerApi/site/GetSiteAssetMarketPrograms?siteId=2", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['loadAssignments'][0]['marketProgramsOnOff']['DAE'] == True 
    assert d['loadAssignments'][0]['marketProgramsOnOff']['EBS'] == True   

@pytest.mark.tag('int','stage','prod')
def test_GetBpaRerunThreshold():
    response = url_header.get_response("/DerApi/site/GetBpaRerunThreshold?siteId=17", path2, headers)
    assert response.status_code == 200
    assert response.text == 10

@pytest.mark.tag('int','stage','prod')
def test_GetBgRolling12Months():
    response = url_header.get_response("/DerApi/site/GetBgRolling12Months?siteId=2&isRolling12=false&isReadonly=true", path2, headers)
    assert response.status_code == 200
    assert response.text == "true"


def test_GetBpaRerunThreshold():
    response = url_header.get_response("/DerApi/site/GetBpaRerunThreshold?siteId=17", path2, headers)
    assert response.status_code == 200
    assert response.text == '10'

def test_GetEmailConfig():
    response = url_header.get_response("/DerApi/Site/GetEmailConfig?siteId=2", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['name'] == "Hourly Load Forecast Deviance"

def test_GetSiteExportPermissionFlag():
    response = url_header.get_response("/DerApi/Site/GetSiteExportPermissionFlag?siteId=2", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['numericValue'] == 1.0

def test_SetEmailConfig():
    payload = json.dumps([
    {
        "id": 3,
        "name": "Hourly Load Forecast Deviance",
        "enabled": False
    }
    ])
    response = url_header.post_response("/DerApi/Site/SetEmailConfig", path2, headers, payload)
    assert response.status_code == 200
    d = json.loads(response.text)
    assert d[0]['name'] == 'Hourly Load Forecast Deviance'
    assert d[0]['enabled'] == False
    
def test_AddUpdateTag():
    
    payload = json.dumps({
        "siteId": 1,
        "assetGuid": "58f91e07-6948-46df-aca4-db5459e45609",
        "assetTagList": [
            {
            "id": 2,
            "name": "cpc.a7810.001EC60128FF.2",
            "category": "Generator Output"
            }
        ]
        })

    response = url_header.post_response("/DerApi/Site/AddUpdateMeterTags", path2, headers, payload)
    assert response.status_code == 200
    #assert response.text == 0