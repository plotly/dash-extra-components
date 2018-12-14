import json
import time


from pytest_dash.utils import (
    import_app,
    wait_for_element_by_css_selector
)


def test_page_logic(dash_threaded, selenium):
    dash_threaded(import_app('test_apps.pager2'))

    first = wait_for_element_by_css_selector(
        selenium, '#pager > span:first-child')

    first.click()
    output = wait_for_element_by_css_selector(selenium, '#output')

    time.sleep(2)
    payload = json.loads(output.text)

    # Assert that the total of pages are 33546/5 + 1 for the rest.
    assert 6710 == payload['total']

    assert 0 == payload['start']
    assert 5 == payload['end']

    last = wait_for_element_by_css_selector(
        selenium, '#pager > span:last-child')
    last.click()
    time.sleep(1)

    payload = json.loads(output.text)

    # Last page got only one item.
    assert 33545 == payload['start']
    assert 33546 == payload['end']

