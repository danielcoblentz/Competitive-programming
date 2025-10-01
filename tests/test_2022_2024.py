import unittest
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestProblems(unittest.TestCase):
    def run_script(self, script_path, input_text):
        # Run the script with the workspace python and return stdout text
        py = sys.executable
        p = subprocess.run([py, str(script_path)], input=input_text.encode('utf-8'), capture_output=True)
        out = p.stdout.decode('utf-8').replace('\r\n', '\n')
        return p.returncode, out.strip(), p.stderr.decode('utf-8')

    def test_2022_problem9_examples(self):
        script = ROOT / '2022 problems' / '2022Problem9.py'
        inp = "4\n1\n2\n3\n7\n"
        rc, out, err = self.run_script(script, inp)
        self.assertEqual(rc, 0, f"Script exited nonzero: {err}")
        expected = "2\n3\n5\n34"
        self.assertEqual(out, expected)

    def test_2022_problem8_examples(self):
        script = ROOT / '2022 problems' / '2022Problem8.py'
        inp = "4\ncow\nbuzz\nzigzag\nzzz\n"
        rc, out, err = self.run_script(script, inp)
        self.assertEqual(rc, 0, f"Script error: {err}")
        expected = "Buzz!Buzz!Buzz!Buzz!\nBuzz!Buzz!Buzz!bzzbzzBuzz!Buzz!\nbzzBuzz!Buzz!Buzz!bzzBuzz!Buzz!Buzz!Buzz!Buzz!\nbzzbzzbzzBuzz!Buzz!Buzz!"
        self.assertEqual(out, expected)

    def test_2022_problem3_examples(self):
        script = ROOT / '2022 problems' / '2022Problem3.py'
        # the script expects a sequence of totals, ending with a negative value; do NOT prefix with a count
        inp = "0\n1\n5\n17\n-1\n"
        rc, out, err = self.run_script(script, inp)
        self.assertEqual(rc, 0, f"Script error: {err}")
        expected = "1 {}\n0\n1 {2,3}\n14 {2,7,8}"
        self.assertEqual(out, expected)

    def test_2024_problem7_example(self):
        script = ROOT / '2024 problems' / '2024Problem7.py'
        # example from earlier work (small grid): 1 test, 3x3, grid values such that after -3 flood, there is 1 island
        inp = "1\n3 3\n4 4 4\n4 1 4\n4 4 4\n"
        rc, out, err = self.run_script(script, inp)
        self.assertEqual(rc, 0, err)
        # After subtracting 3: 1 1 1 / 1 0 1 / 1 1 1 => a single island
        self.assertEqual(out.strip(), "1")

    def test_2024_problem8_preprocess(self):
        script = ROOT / '2024 problems' / '2024Problem8.py'
        # small source with one #ifdef A block and else
        source = [
            "#ifdef A",
            "int a;",
            "#else",
            "int b;",
            "#endif",
            "<EOF>",
            "A",
            "",
        ]
        inp = "\n".join(source) + "\n"
        rc, out, err = self.run_script(script, inp)
        self.assertEqual(rc, 0, err)
        # first case (A defined) should include int a; and comment
        lines = out.splitlines()
        self.assertTrue("int a;" in lines[1])

if __name__ == '__main__':
    unittest.main()
