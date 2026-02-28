import pytest
import logging
logger = logging.getLogger(__name__)

def test_delete_booking(api):
    logger.info('start request delete /booking/1')
    response = api.post('/booking/1')
    assert response.ok, "response is'nt ok'"
    logger.info('response status ok')
    assert response.body(), "there is'nt body'"
    logger.info('there is body')
