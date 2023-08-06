import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('newlogfile.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def getDropDown(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
