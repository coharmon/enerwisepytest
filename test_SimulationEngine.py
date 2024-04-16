import requests
import json
from settings.token_settings import *
from settings.generate_token import *
from utils.header import url_header

def test_GetProgramAssetRevenuePostCost():
    response = url_header.get_response("/DerApi/SimulationEngine/GetProgramAssetRevenuePostCost?caseId=668", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['marketProgramName'] == 'NE Clean Peak' or d[0]['marketProgramName'] == 'ES WMA Daily Dispatch'

def test_GetSimCaseParameters():  
    response = url_header.get_response("/DerApi/SimulationEngine/GetSimCaseParameters?siteId=35&caseId=182", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['simulationCaseId'] == 182

def test_GetSiteMarketProgramAssignments():
    response = url_header.get_response("/DerApi/SimulationEngine/GetSiteMarketProgramAssignments?siteId=43&caseId=668", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200

def test_GetSimulationStatus():
    response = url_header.get_response("/DerApi/SimulationEngine/GetSimulationStatus?caseId=930", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['message'] == ' Date run: 2023-10-13 03:16:11 (UTC)'

def test_GetMissingData():
    response = url_header.get_response("/DerApi/SimulationEngine/GetMissingData?caseId=930", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200

def test_GetTaxStatusList():
    response = url_header.get_response("/DerApi/SimulationEngine/GetTaxStatusList", path2, headers)
    assert response.status_code == 200

def test_GetSimulationCaseReportName():
    response = url_header.get_response("/DerApi/SimulationEngine/GetSimulationCaseReportName?caseId=930", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0] == 'Scale Microgrid Solutions Operating Bowery Farms_930_20240601_20250531.xlsx'

def test_GetIndividualSimulationCase():
    response = url_header.get_response("/DerApi/SimulationEngine/GetSimulationCase?studyCaseId=930", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d['updatedAt'] == '2023-10-13T03:16:11.98' 
    assert d['id'] == 930
    assert d['siteId'] == 2
    assert d['includeYear2Savings'] == 0
    assert d['seasonalAllocationCaseId'] == 324
    assert d['monthlyAllocationCaseId'] == 728

def test_GetAllSimulationCases():
    response = url_header.get_response("/DerApi/SimulationEngine/GetSimulationCases?siteId=2&isKpi=false", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['siteId'] == 2
    assert d[0]['isKpi'] == None


# def test_AddSimulationCase():

#     payload = json.dumps({
#     "id": 0,
#     "siteId": 1,
#     "includeYear2Savings": 0,
#     "seasonalAllocationCaseId": 40,
#     "monthlyAllocationCaseId": 228,
#     "start": "2023-06-01T00:00:00-04:00",
#     "finish": "2024-05-01T00:00:00-04:00",
#     "baseStart": "2022-01-01T00:00:00-05:00",
#     "baseFinish": "2022-06-30T00:00:00-04:00",
#     "name": "202306_202405_1668735319806"
#     })

#     response = url_header.post_response("/DerApi/SimulationEngine/AddSimulationCase", path2, headers, payload)
#     assert response.status_code == 200
#     #assert response.text == 0