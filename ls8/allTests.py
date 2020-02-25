import unittest
from cpu import *
import io
import sys
import os

class TestLs8(unittest.TestCase):
    def test_call(self):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        cpu = CPU()
        cpu.load("./examples/call.ls8")
        cpu.run()
        cpu.halt = True

        sys.stdout = old_stdout

        what_was_printed = buffer.getvalue()
        sys.stdout.close()

        self.assertEqual(what_was_printed, "20\n30\n36\n60\n")

    def test_stack(self):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        cpu = CPU()
        cpu.load("./examples/stack.ls8")
        cpu.run()
        cpu.halt = True

        sys.stdout = old_stdout

        what_was_printed = buffer.getvalue()
        self.assertEqual(what_was_printed, "2\n4\n1\n")
    
    def test_print8(self):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        cpu = CPU()
        cpu.load("./examples/print8.ls8")
        cpu.run()
        cpu.halt = True

        sys.stdout = old_stdout

        what_was_printed = buffer.getvalue()
        self.assertEqual(what_was_printed, "8\n")

    def test_mult(self):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        cpu = CPU()
        cpu.load("./examples/mult.ls8")
        cpu.run()
        cpu.halt = True

        sys.stdout = old_stdout

        what_was_printed = buffer.getvalue()
        self.assertEqual(what_was_printed, "72\n")

    def test_sctest(self):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        cpu = CPU()
        cpu.load("./examples/sctest.ls8")
        cpu.run()
        cpu.halt = True

        sys.stdout = old_stdout

        what_was_printed = buffer.getvalue()
        self.assertEqual(what_was_printed, "1\n4\n5\n")



if __name__ == '__main__':
    unittest.main()