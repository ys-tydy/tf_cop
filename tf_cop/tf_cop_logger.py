import pprint

pp = pprint.PrettyPrinter(indent=4, width=30, depth=1)


class TfCopLogger:
    """
    logging
    """

    def __init__(self):
        self._color_set = {
            "BLACK": '\033[30m',
            "RED": '\033[31m',
            "GREEN": '\033[32m',
            "YELLOW": '\033[33m',
            "BLUE": '\033[34m',
            "PURPLE": '\033[35m',
            "CYAN": '\033[36m',
            "WHITE": '\033[37m',
            "END": '\033[0m',
            "BOLD": '\038[1m',
            "UNDERLINE": '\033[4m',
            "INVISIBLE": '\033[08m',
            "REVERCE": '\033[07m'
        }
        self._output_log = ""
        self._program_error_log = ""
        self._system_log = ""
        self._resource_num = 0
        self._pass_num = 0
        self._warn_num = 0
        self._alert_num = 0

    def skip(self, message: str):
        """
        add test skip log
        :param message: (str)
        :return: None
        """
        self._output_log += self._color_set["YELLOW"]
        self._output_log += "[SKIP] " + message + "\n"
        self._output_log += self._color_set["END"]

    def passed(self, resource_dict: dict, review_dict: dict, text: str):
        """
        add test pass log
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :param text: (str)
        :return: None
        """
        self._pass_num += 1
        self._output_log += self._color_set["GREEN"]
        self._output_log += "[PASS] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += self._color_set["END"]

    def warn(self, resource_dict: dict, review_dict: dict, text: str):
        """
        add test warn log
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :param text: (str)
        :return: None
        """
        self._warn_num += 1
        self._output_log += self._color_set["YELLOW"]
        self._output_log += "[WARN] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pp.pformat(resource_dict) + "\n"
        self._output_log += self._color_set["END"]

    def alert(self, resource_dict: dict, review_dict: dict, text: str):
        """
        add test alert log
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :param text: (str)
        :return: None
        """
        self._alert_num += 1
        self._output_log += self._color_set["RED"]
        self._output_log += "[ALERT] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pp.pformat(resource_dict) + "\n"
        self._output_log += self._color_set["END"]

    def add_resource_info(self, resource_name: str, obj_name: str):
        """
        add resource info log
        :param resource_name: (str)
        :param obj_name: (str)
        :return: None
        """
        self._resource_num += 1
        self._output_log += "\n==========================================================\n"
        self._output_log += "RESOURCE " + self._color_set["UNDERLINE"]
        self._output_log += resource_name.upper() + "." + obj_name.upper() + "\n"
        self._output_log += self._color_set["END"]
        self._output_log += "==========================================================\n"

    def output(self, color: bool = False):
        """
        get full output
        :param color: (bool)
        :return: output: (str)
        """
        if self._program_error_log:
            self._output_log += self._color_set["CYAN"]
            self._output_log += self._program_error_log
        self._output_log += "\n" + self.output_summary()
        if color:
            return self._output_log
        else:
            return self.__remove_color(self._output_log)

    def output_summary(self, color: bool = False):
        """
        gesummary output
        :param color: (bool)
        :return: summary_output: (str)
        """
        res = "\n =======================\n"
        res += "| RESOURCE NUM\t: " + str(self._pass_num) + "\t|\n"
        res += "| PASS NUM\t: " + str(self._pass_num) + "\t|\n"
        res += "| WARN NUM\t: " + str(self._warn_num) + "\t|\n"
        res += "| ALERT NUM\t: " + str(self._alert_num) + "\t|\n"
        res += " =======================\n"
        if color:
            return res
        else:
            return self.__remove_color(res)

    def add_program_error_log(self, error_message: str):
        """
        add program error log
        :param error_message: (str)
        :return: None
        """
        self._program_error_log += "\n--------------------------------------------\n"
        self._program_error_log += self._color_set["RED"]
        self._program_error_log += error_message
        self._program_error_log += self._color_set["END"]
        self._program_error_log += "\n--------------------------------------------\n"

    def add_system_log(self, system_log: str):
        """
        add system log
        :param system_log: (str)
        :return: None
        """
        self._system_log += "\n--------------------------------------------\n"
        self._system_log += system_log
        self._system_log += "\n--------------------------------------------\n"

    def system_log(self, color: bool = False):
        """
        system log
        :param color: (bool)
        :return: system_log: (str)
        """
        if color:
            return self._system_log
        else:
            return self.__remove_color(self._system_log)

    def program_error_log(self, color: bool = False):
        """
        program error log
        :param color: (bool)
        :return: program_error_log: (str)
        """
        if color:
            return self._program_error_log
        else:
            return self.__remove_color(self._program_error_log)

    def __remove_color(self, text):
        """
        remove color srt
        :param text: (str)
        :return: text: (str)
        """
        res = text
        for color in self._color_set.keys():
            res = res.replace(self._color_set[color], "")
        return res
