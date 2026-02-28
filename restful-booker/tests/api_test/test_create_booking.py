import pytest
import jsonschema
import logging
logger = logging.getLogger(__name__)

def test_create_booking(api):
    data = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-02-01",
            "checkout" : "2026-02-02"
    },
    "additionalneeds" : "Breakfast"
}
    schema = {
        "type" : "object",
        "properties" : {
            "bookingid" : {"type" : "string"},
            "booking" : {"type" : "object",
                         "properties" : {
                             "firstname" : {"type" : "string"},
                             "lastname" : {"type" : "string"},
                             "totalprice" : {"type" : "int"},
                             "depositpaid" : {"type" : "boolean"},
                             "bookingdates" : {
                                 "type" :  "object",
                                 "properties" : {
                                     "checkin" : {"type" : "string"},
                                     "checkout" : {"type" : "string"}}
                             },
                             "adittionalneeds" : {"type" : "string"}},
                         },
            "required" : ["firstname", "lastname", "totalprice"]
        }
    }
    logger.info('start request post /booking')
    response = api.post('/booking', data=data)
    assert response.ok, "response is'nt ok'"
    logger.info('response status ok')
    assert response.body(), "there is'nt body'"
    logger.info('there is body')
    data = response.json()
    logger.info('get response,start validate json schema')
    jsonschema.validate(data, schema)
    logger.info('json schema is valid ')
