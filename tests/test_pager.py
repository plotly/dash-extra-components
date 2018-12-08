from pytest_dash.utils import (
    wait_for_element_by_css_selector,
    wait_for_text_to_equal
)


def test_pager(dash_subprocess, selenium):
    dash_subprocess('test_apps.pager')

    pager_elem = wait_for_element_by_css_selector(selenium, '#pager')
    # content = wait_for_element_by_css_selector(selenium, '#page-content')

    wait_for_text_to_equal(selenium, '#page-content', 'You are on page 1')

    elems = pager_elem.find_elements_by_css_selector('span')

    assert 10 == len(elems)

    for i, elem in enumerate(elems[:-2]):
        elem.click()
        wait_for_text_to_equal(
            selenium, '#page-content', 'You are on page {}'.format(i + 1))
