import pytest
import jsonschema
import logging
logger = logging.getLogger(__name__)

@pytest.mark.parametrize('method, bookingid, firstname, lastname',
                    [('put', 1, 'lana', 'lancu'),
                     ('put', 1, 'lata', 'lyncu'),
                     ('put', 1, 'lona', 'loncu'),
                     ('put', 1, 'laja', 'lencu'),
                     ('put', 1, 'lena', 'luncu'),
                     ('patch', 1, 'laka', 'lencu'),
                     ('patch', 1, 'latu', 'loncu'),
                     ('patch', 1, 'lono', 'luncu'),
                     ('patch', 1, 'lajo', 'lyncu'),
                     ('patch', 1, 'lene', 'lunci')
                    ]
                     )
def test_put_booking(api_request,
                     method: str,
                     bookingid: int,
                     firstname,
                     lastname,
                     totalprice=111,
                     deposit=True,
                     checkin = "2026-02-01",
                     checkout = "2026-02-03",
                     additional = "Breakfast"
                     ):
    data = {
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : deposit,
        "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
    },
    "additionalneeds" : additional
}
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
    
    logger.info(f'start request {method} /booking/{bookingid}')
    response = api_request.fetch(f'/booking/{bookingid}', method=method, data=data)
    assert response.ok, f"response is'nt ok, {response.status}"
    logger.info('response status ok')
    assert response.body(), "there is'nt body'"
    logger.info('there is body')
    data = response.json()
    logger.info('get response json, start validate json schema')
    jsonschema.validate(data, schema)
    logger.info('json schema is valid ')

    
