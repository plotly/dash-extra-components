from pytest_dash.wait_for import (
    wait_for_element_by_css_selector
)


def test_table_of_contents(dash_threaded):
    from test_apps.table_of_contents import app
    selenium = dash_threaded.driver
    dash_threaded(app)

    toc_elem = wait_for_element_by_css_selector(selenium, '#toc')

    elements = toc_elem.find_elements_by_xpath('//a[contains(@href, "toc")]')
    assert 9 == len(elements), 'Nine toc elements were not created'

