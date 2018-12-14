from pytest_dash.utils import (
    import_app,
    wait_for_element_by_css_selector,
    wait_for_text_to_equal
)


def test_pager(dash_threaded, selenium):
    dash_threaded(import_app('test_apps.pager'))

    pager_elem = wait_for_element_by_css_selector(selenium, '#pager')

    wait_for_text_to_equal(selenium, '#page-content', 'You are on page 1')

    elems = pager_elem.find_elements_by_css_selector('span')

    assert 10 == len(elems)

    for i, elem in enumerate(elems[:-2]):
        elem.click()
        wait_for_text_to_equal(
            selenium, '#page-content', 'You are on page {}'.format(i + 1))
