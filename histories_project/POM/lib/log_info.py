import logging

logging.basicConfig(filename='test_run.txt', format='%(asctime)s %(message)s', level=logging.INFO)


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
