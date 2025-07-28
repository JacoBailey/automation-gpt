import seleniumbase, time

class ModuleTimeoutReachedError(Exception):
    """Error is used for when the  module has reached the selected timeout before a selector has been found."""
    f'Module has reached timeout. No selectors found.'
    pass

def multi_selector_search(browser_object, selector_list, module_timeout=15):
    """Enables user to search for multiple selectors and return the first one found or return error"""
    start_time = time.time()
    while time.time() - start_time < module_timeout:
        for selector in selector_list:
            try: 
                browser_object.wait_for_element_visible(selector, timeout=0.01)
                return selector
            except seleniumbase.common.exceptions.NoSuchElementException:
                continue
    raise ModuleTimeoutReachedError