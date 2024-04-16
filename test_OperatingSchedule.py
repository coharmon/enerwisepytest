import requests
import json
from settings.token_settings import *
from settings.generate_token import *
from utils.header import url_header

def test_GetBidTransaction():
    response = url_header.get_response("/DerApi/Optimization/GetBidTransaction?siteScheduleId=41377", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['productType'] == "DAE"
    assert d[0]['bidStatus'] == "Acknowledged"
    assert d[1]['productType'] == "RTE"
    assert d[1]['bidStatus'] == "Acknowledged"   

def test_GetSiteMarketPrograms():  
    response = url_header.get_response("/DerApi/Optimization/GetSiteMarketPrograms?siteId=19", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['marketProgramName'] == "DAE"
    assert d[0]['derResourceType'] == 1
    assert d[1]['marketProgramName'] == "DAE"
    assert d[1]['derResourceType'] == 3

def test_GetAwardedHourlyData():
    response = url_header.get_response("/DerApi/Optimization/GetAwardedHourlyData?siteScheduleId=21631", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['10be8b3e-c4b5-4459-8efe-060ff36ac1f6'] == {'DAE': '', 'SR': '', 'DCM': '', 'EBS': '', 'PDM': ''}

def test_GetSiteOptimizationParameters():
    response = url_header.get_response("/DerApi/Optimization/GetSiteOptimizationParameters?siteScheduleId=21631&hasHourlyData=false&UserLoginId=8026"
    , path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['bgConfigurations'][0]['marketPrograms'] == ['DAE', 'SR', 'DCM', 'EBS', 'PDM']

def test_GetSiteOptimizationParameters():
    response = url_header.get_response("/DerApi/Optimization/GetSiteOptimizationParameters?siteScheduleId=21631&hasHourlyData=false&UserLoginId=8026"
    , path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['bgConfigurations'][0]['marketPrograms'] == ['DAE', 'SR', 'DCM', 'EBS', 'PDM']
    
def test_Get_Dispatch_Trigger_Threshold_Config():
    response = url_header.get_response("/DerApi/site/GetDispatchTriggerThresholdConfig?siteId=2", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['noPerformanceThresholdPerc'] == 10
    assert d[0]['lowPerformanceThresholdPerc'] == 90   

def test_Get_Site_Asset_MarketPrograms():
    response = url_header.get_response("/DerApi/site/GetSiteAssetMarketPrograms?siteId=2", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['loadAssignments'][0]['marketProgramsOnOff']['DAE'] == True 
    assert d['loadAssignments'][0]['marketProgramsOnOff']['EBS'] == True   

def test_GetBpaRerunThreshold():
    response = url_header.get_response("/DerApi/site/GetBpaRerunThreshold?siteId=17", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert response.text == '10'

def test_GetSiteOutageHours():
    response = url_header.get_response("/DerApi/site/GetSiteOutageHours?siteId=3", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['outageHours'] == "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24"

def test_GetSiteSchedule():
    response = url_header.get_response("/DerApi/Optimization/GetSiteSchedule?id=41284", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['siteId'] == 54

def test_GetMarketScheduleStatus():
    response = url_header.get_response("/DerApi/Optimization/GetMarketScheduleStatus?siteId=54&siteScheduleId=41284", path2, headers)
    print(response.status_code)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['name'] == "Closed"


def test_UpdateUtilityRateManager():

    payload = json.dumps({
    "electricRateId": 53,
    "siteId": 19,
    "rateClassId": 1,
    "supplyTypeId": 1,
    "supplyStructureId": 7,
    "billingPeriod": "2020-11-18T00:00:00-04:00",
    "daysinBp": 30,
    "tariffName": "www",
    "effectiveDate": "2024-05-31T00:00:00-04:00",
    "expirationDate": "2021-09-01T11:00:00-04:00",
    "summerStartMonth": 6,
    "summerEndMonth": 9,
    "winterStartMonth": 10,
    "winterEndMonth": 5,
    "isComplete": False
    })

    response = url_header.post_response("/DerApi/Site/AddUpdateDerElectricRate", path2, headers, payload)
    assert response.status_code == 200
    #assert response.text == 0