import requests
import json
from settings.token_settings import *
from settings.generate_token import *
from utils.header import url_header

def test_Get_DER_Electric_Rates():
    response = url_header.get_response("/DerApi/Site/GetDerElectricRates?siteId=19", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['siteId'] == 19

def test_Get_DER_Electric_Rates_Tariff():  
    response = url_header.get_response("/DerApi/Site/GetDerElectricRateTariff?electricRateId=56", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['electricRateId'] == 56

def test_Get_DER_Electric_Rates_Tariff_PDM():
    response = url_header.get_response("/DerApi/Site/GetDerPowerRateTariff_PDM?electricRateId=43", path2, headers)
    d = json.loads(response.text)
    assert response.status_code == 200
    assert d[0]['powerPdmRateTariffId'] == 8

    
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
    print(response.text)
    print(response.status_code)
    #assert response.text == 0