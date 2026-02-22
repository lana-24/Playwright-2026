import jsonschema
from typing import Literal

def booked_ui(data: dict):
    schema = {
        "type" : "object",
        "properties" : {"bookingid" : {"type" : "int"},
                        "roomid" : {"type" : "int"},
                        "firstname" : {"type" : "string"},
                        "lastname" : {"type" : "string"},
                        "depositpaid" : {"type" : "boolean"},
                        "bookingdates" : {"checkin" : {"type" : "string"},
                                          "checkout" : {"type" : "string"}}
                        },
        "required" : ["bookingid","firstname","lastname"]
    }
    jsonschema.validate(data, schema)

def booked_api(data: dict):
    schema = {
        "type" : "object",
        "properties" : {"bookingid" : {"type" : "int"},
                        "booking" : {"firstname" : {"type" : "string"},
                                     "lastname" : {"type" : "string"},
                                     "totalprice" : {"type" : "int"},
                                     "depositpaid" : {"type" : "boolean"},
                                     "bookingdates" : {
                                         "checkin" : {"type" : "string"},
                                         "checkout" : {"type" : "string"}},
                                     "additionalneeds" : {"type" : "string"}
                                     }
                        },
        "required" : ["bookingid", "booking"]
    }
    jsonschema.validate(data, schema)
