from subprocess import Popen, PIPE, TimeoutExpired
import unittest


class Test_prog_2(unittest.TestCase):
    ENCODING = 'utf-8'
    PROCESS_WITH_ARGS = ('python', 'prog_2.py')
    PROCESS_TIMEOUT = 5  # seconds
    INPUT_SIGNATURE = 'Enter data:'
    # EXCEPTION_SIGNATURE = 'ValueError:'
    MESSAGE_SIGNATURE_LACK_OF_NUM = 'No data.'
    MESSAGE_SIGNATURE_INCORRECT_CHARACTERS = 'Invalid data.'

    def run_subprocess(self, input_value):
        global proc
        try:
            proc = Popen(self.PROCESS_WITH_ARGS,
                         stdin=PIPE,
                         stdout=PIPE,
                         stderr=PIPE)
            out_value, err_value = proc.communicate(input_value.encode(self.ENCODING),
                                                    timeout=self.PROCESS_TIMEOUT)
        except TimeoutExpired:
            proc.kill()
            out_value, err_value = proc.communicate()
        return out_value.decode(self.ENCODING), err_value.decode(self.ENCODING)

    def test_normal_input(self):
        input_data = [
            ('2 6 7 -4 3 -1 2.2', '[15.2, 5, 2.0, 6.0, 7.0, -4.0, 3.0, -1.0, 2.2]')
        ]

        for input_str, expect_str in input_data:
            output_str, error_str = self.run_subprocess(input_str)
            actual_result = output_str.strip().split(self.INPUT_SIGNATURE)[-1].strip()
            self.assertEqual(actual_result, expect_str)

    def test_lack_of_num(self):
        input_str = '\n'
        output_str, err_str = self.run_subprocess(input_str)
        self.assertIn(self.MESSAGE_SIGNATURE_LACK_OF_NUM, output_str)

    def test_incorrect_characters(self):
        bad_input_data = [
            '1 е 3\nt\n',
        ]

        for input_str in bad_input_data:
            output_str, error_str = self.run_subprocess(input_str)
            self.assertIn(self.MESSAGE_SIGNATURE_INCORRECT_CHARACTERS, output_str)


if __name__ == '__main__':
    unittest.main()
