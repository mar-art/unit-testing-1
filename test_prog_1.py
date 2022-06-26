from subprocess import Popen, PIPE, TimeoutExpired
import unittest


class Test_prog_1(unittest.TestCase):
    ENCODING = 'utf-8'
    PROCESS_WITH_ARGS = ('python', 'prog_1.py')
    PROCESS_TIMEOUT = 5  # seconds
    INPUT_SIGNATURE = 'Enter data:Enter max length:'
    EXCEPTION_SIGNATURE = 'ValueError:'
    MESSAGE_SIGNATURE_LACK_OF_WORDS = 'No data.'

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
            ('testing is wonderful\n5\n', 'testing is*** wonderful'),
            ('testing is my favorite pastime\n9\n',
             'testing** is******* my******* favorite* pastime**')
        ]

        for input_str, expect_str in input_data:
            output_str, error_str = self.run_subprocess(input_str)
            actual_result = output_str.strip().split(self.INPUT_SIGNATURE)[-1].strip()
            self.assertEqual(actual_result, expect_str)

    def test_invalid_input(self):
        bad_input_data = [
            'testing is not wonderful\nt\n',
            'testing is not wonderful\n\n',
            'testing is not wonderful\n1.3\n'
        ]

        for input_str in bad_input_data:
            output_str, error_str = self.run_subprocess(input_str)
            self.assertIn(self.EXCEPTION_SIGNATURE, error_str)

    def test_lack_of_words(self):
        input_str = '\n4\n'
        output_str, err_str = self.run_subprocess(input_str)
        self.assertIn(self.MESSAGE_SIGNATURE_LACK_OF_WORDS, output_str)


if __name__ == '__main__':
    unittest.main()
