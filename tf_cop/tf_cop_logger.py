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
        self._pass_num = 0
        self._warn_num = 0
        self._alert_num = 0

    def skip(self, message):
        self._output_log += self._color_set["YELLOW"]
        self._output_log += "[SKIP] " + message + "\n"
        self._output_log += self._color_set["END"]

    def passed(self, resource_dict, review_dict, text):
        self._pass_num += 1
        self._output_log += self._color_set["GREEN"]
        self._output_log += "[PASS] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += self._color_set["END"]

    def warning(self, resource_dict, review_dict, text):
        self._warn_num += 1
        self._output_log += self._color_set["YELLOW"]
        self._output_log += "[WARN] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pp.pformat(resource_dict) + "\n"
        self._output_log += self._color_set["END"]

    def alert(self, resource_dict, review_dict, text):
        self._alert_num += 1
        self._output_log += self._color_set["RED"]
        self._output_log += "[ALERT] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pp.pformat(resource_dict) + "\n"
        self._output_log += self._color_set["END"]

    def add_resource_info(self, resource_name, obj_name):
        self._output_log += "\n==========================================================\n"
        self._output_log += "RESOURCE " + self._color_set["UNDERLINE"]
        self._output_log += resource_name.upper() + "." + obj_name.upper() + "\n"
        self._output_log += self._color_set["END"]
        self._output_log += "==========================================================\n"

    def output(self, color: bool = False):
        if self._program_error_log:
            self._output_log += self._color_set["CYAN"]
            self._output_log += self._program_error_log
        self._output_log += "\n" + self.output_summary()
        if color:
            return self._output_log
        else:
            return self.__remove_color(self._output_log)

    def output_summary(self, color: bool = False):
        res = "\n =======================\n"
        res += "| PASS NUM\t: " + str(self._pass_num) + "\t|\n"
        res += "| WARN NUM\t: " + str(self._alert_num) + "\t|\n"
        res += "| ALERT NUM\t: " + str(self._alert_num) + "\t|\n"
        res += " =======================\n"
        if color:
            return res
        else:
            return self.__remove_color(res)

    def add_program_error_log(self, error_message: str):
        self._program_error_log += "\n--------------------------------------------\n"
        self._program_error_log += self._color_set["RED"]
        self._program_error_log += error_message
        self._program_error_log += self._color_set["END"]
        self._program_error_log += "\n--------------------------------------------\n"

    def add_system_log(self, system_log: str):
        self._system_log += "\n--------------------------------------------\n"
        self._system_log += system_log
        self._system_log += "\n--------------------------------------------\n"

    def system_log(self, color: bool = False):
        if color:
            return self._system_log
        else:
            return self.__remove_color(self._system_log)

    def program_error_log(self, color: bool = False):
        if color:
            return self._program_error_log
        else:
            return self.__remove_color(self._program_error_log)

    def __remove_color(self, text):
        res = text
        for color in self._color_set.keys():
            res = res.replace(self._color_set[color], "")
        return res
