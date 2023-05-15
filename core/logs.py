import logging


class ComponentLog:
    def __init__(self):
        # Gets or creates a logger
        logger = logging.getLogger('component_log')

        # set log level
        logger.setLevel(logging.WARNING)

        # define file handler and set formatter
        file_handler = logging.FileHandler('component_log.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(file_handler)

    def upload_log_to_db(self, path):
        """
        will upload the component log to the automation run db
        """


class Dmesg:

    def set_stamp(self, obj, stamp):
        obj.connection.exec_command(f'echo {stamp} > /dev/kmsg')

    def get_err_from_block(self, obj, stamp):
        """get block of data from EOF till stamp"""
        obj.connection.exec_command(f'grep - e "{stamp}" file | tail - n1')

