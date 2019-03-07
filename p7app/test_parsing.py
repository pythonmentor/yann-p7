#!/usr/bin/python3
# -*- coding: Utf-8 -*
from p7app import parser as script

from io import BytesIO
import json

import requests 




#test if our function send a sentence in lower case
def test_in_lower_case():
    pa = script.SentenceParse()
    x = "TEST"
    assert pa.in_lower_case(x) == "test"



def test_deleting_stop_words():
    useless_sentence = "afin ailleurs openclassroom"
    pa = script.SentenceParse()
    assert pa.deleting_stop_words(useless_sentence) == "openclassroom"


def test_deleting_special():
    special_sentence = "openclassroom,paris:france"
    pa = script.SentenceParse()
    assert pa.deleting_special(special_sentence) == "openclassroom paris france"


def test_deleting_several_spaces():
    sentence = "openclassroom  paris"
    pa =  script.SentenceParse()
    assert pa.deleting_several_spaces(sentence) == "openclassroom paris"


def test_returning_cleaned_sentence():
    sentence = "TEST,openclassroom ailleurs:hamdi"
    pa = script.SentenceParse()
    assert pa.returning_cleaned_sentence(sentence) == "test openclassroom hamdi"

# -tc- petit exemple de test avec mock
def test_sending_to_api_handles_correct_result(monkeypatch)
    FAKE_ADDRESS = "adresse de test, rue du test 77, openclassrooms"
    FAKE_LAT: 49.0
    FAKE_LNG: 3.0
        
    class MockGet:
        def __init__(self, url):
            pass
        
        def json(self):
            return {
                "results": [{
                    "formatted_address": FAKE_ADDRESS,
                    "geometry": {
                        "location: {
                            "lat": FAKE_LAT,
                            "lng": FAKE_LNG
                        }
                    }
                }]
            }
        
    monkeypatch.setattr("p7app.parser.request.get", MockGet)
    pa = script.SentenceParse()
    pa.sending_to_api("petit test avec mock")
    assert pa.address == FAKE_ADDRESS
    assert pa.lat == FAKE_LAT
    assert pa.lng == FAKE_LNG
    
def test_sending_to_api(monkeypatch):
    "mock for the api request"
    pa = script.SentenceParse()
    results = "7 Cité Paradis, 75010 Paris, France"
        
    def mockreturn(requests):
        return results
    monkeypatch.setattr(requests, "get", mockreturn)
    assert pa.sending_to_api("openclassroom") == results
