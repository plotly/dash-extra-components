import time


from pytest_dash.utils import (
    import_app,
    wait_for_text_to_equal,
    wait_for_element_by_css_selector
)
from selenium.webdriver.common.keys import Keys


def clear_input(input_element):
    # selenium clear doesn't play nice with this component
    input_element.send_keys(
        Keys.BACKSPACE * (len(input_element.get_attribute('value')) + 1)
    )


def test_suggestions_input(dash_threaded, selenium):
    app = import_app('test_apps.suggestions_input')
    dash_threaded(app)

    suggestion_input = wait_for_element_by_css_selector(
        selenium, '#suggestions')
    triggerless_input = wait_for_element_by_css_selector(
        selenium, '#triggerless'
    )

    # Tests all suggestion types.
    suggestion_input.send_keys('$Term\t')
    wait_for_text_to_equal(selenium, '#suggestions-output', 'Terminator')

    clear_input(suggestion_input)
    time.sleep(1)
    suggestion_input.send_keys('@call')
    time.sleep(1)
    suggestion_input.send_keys('\t')
    wait_for_text_to_equal(selenium, '#suggestions-output', 'callback')

    clear_input(suggestion_input)
    time.sleep(1)
    suggestion_input.send_keys('#fi')
    time.sleep(1)
    suggestion_input.send_keys('\t')
    wait_for_text_to_equal(selenium, '#suggestions-output', 'five')

    triggerless_input.send_keys('Preda\t')
    wait_for_text_to_equal(selenium, '#triggerless-output', 'Predator')
