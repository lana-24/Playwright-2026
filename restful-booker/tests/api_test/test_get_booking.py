import pytest
import jsonschema
import logging

logger = logging.getLogger(__name__)

def test_get_booking_id(api):
    schema = {"type" : "array",
                      "items" : {"properties" : {"bookingid" : {"type" : "string"}
                                              }},
                      "required" : ["bookingid"]
                      }
    # request get
    logger.info('start request get /booking')
    response = api.get('/booking')
    assert response.ok, "response is'nt ok'"
    logger.info('response status ok')
    assert response.body(), "there is'nt body'"
    logger.info('there is body')
    data = response.json()
    logger.info('get response,start validate json schema')
    jsonschema.validate(data, schema)
    logger.info('json schema is valid ')

#@pytest.parametrize("bookingid", [])
#def test_get_booking_spesific_id(api, bookingid: int):
def test_get_booking_spesific_id(api):
    schema = {"type" : "object",
              "properties" : {"firstname" : {"type" : "string"},
                              "lastname" : {"type" : "string"},
                              "totalprice" : {"type" : "integer"},
                              "depositpaid" : {"type" : "boolean"},
                              "bookingdates" : {"type" : "object",
                                                "properties" : {
                                                    "checkin" : {"type" : "string"},
                                                    "checkout" : {"type": "string"}}
                                        
                                                },
                              "additionalneeds" : {"type" : "string"},
                               },
              "required" : ["firstname", "lastname", "totalprice"]
                      }
    # request get
    logger.info('start request get /booking/1')
    response = api.get('/booking/1')
    assert response.ok, "response is'nt ok'"
    logger.info('response status ok')
    assert response.body(), "there is'nt body'"
    logger.info('there is body')
    data = response.json()
    logger.info('get response,start validate json schema')
    jsonschema.validate(data, schema)
    logger.info('json schema is valid ')

