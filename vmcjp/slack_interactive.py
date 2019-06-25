import os
import logging

help_message = "May I help you? please type `help` command."

TEST_ORG_ID = os.environ["test_org"] #for test
#BUTTON = "vmcjp/precheck_button.json"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
