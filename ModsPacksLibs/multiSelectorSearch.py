import seleniumbase, time

class moduleTimeoutReached(Exception):
    'Module has reached timeout.'
    pass

def multiSelectorSearch(browserObject, locatorList, moduleTimeout=15):
    startTime = time.time()
    while time.time() - startTime < moduleTimeout:
        for locator in locatorList:
            try: 
                browserObject.wait_for_element_visible(locator, timeout=0.1)
                break
            except seleniumbase.common.exceptions.NoSuchElementException:
                continue
        return locator
    raise moduleTimeoutReached