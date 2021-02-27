import Testing.OnePassTests as op
import os

test_logs = []


class TestLogData(object):
    def __init__(self, module_name: str, func_name: str, actual, expected, result: bool) -> None:
        super().__init__()
        self.module_name = module_name
        self.func_name = func_name
        self.actual = actual
        self.expected = expected
        self.result = result
       
    def get_message(self):
        return ('Function: ' + self.func_name + '\n' + 'Actual: ' + str(self.actual) + '\t' 
            + 'Expected: ' + str(self.expected) + '\t' + 'Result: ' + str(self.result))

def add_log(module_name: str, func_name: str, actual, expected, result: bool) -> None:
    log = TestLogData(module_name, func_name, actual, expected, result)
    test_logs.append(log)

    
def equal(module_name: str, func_name: str, actual, expected) -> None:
    result = actual == expected
    add_log(module_name, func_name, actual, expected, result)

def is_none(module_name: str, func_name: str, actual) -> None:
    expected = None
    result = actual == expected
    add_log(module_name, func_name, actual, expected, result)

def is_not_none(module_name: str, func_name: str, actual) -> None:
    expected = 'not None'
    result = not actual == None
    add_log(module_name, func_name, actual, expected, result)

def print_results():
    for log in test_logs:
        print (log.get_message())

def clear_console():
    clear = lambda: os.system('cls')
    clear()

def start():
    op.start_tests()
    clear_console()
    print_results()