"""CPU functionality."""

import sys
import re

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.pc = 0
        self.halted = False
        self.instructions = {
            0b10000010: self.ldi, 
            0b01000111: self.prn, 
            0b00000001: self.hlt, 
            0b10100010: self.mult}
    
    def mult(self):
        #multiply binary numbers and store results into first register
        first_register_num = self.ram[self.pc+1]
        second_register_num = self.ram[self.pc+2]
        
        first_num = self.reg[first_register_num]
        second_num = self.reg[second_register_num]

        product = first_num * second_num

        self.reg[first_register_num] = product

        self.pc += 3

    def ldi(self):
        value = self.ram[self.pc+2]
        register_num = self.ram[self.pc+1]

        self.reg[register_num] = value
        self.pc += 3

    def prn(self):
        register_num = self.ram[self.pc+1]
        print(self.reg[register_num])
        self.pc += 2

    def hlt(self):
        self.halted = True
        self.pc += 1

    def ram_read(self, address):
        print(self.ram[address])

    def ram_write(self, address, instruction):
        self.ram[address] = instruction

    def load(self, file):
        """Load a program into memory."""

        address = 0

        program = []

        #whole file
        f = open(file)
        list_of_lines = f.read().split("\n")

        for line in list_of_lines:
            sliced_string = line[:8]
            if re.search(r"[0-1]{8}", sliced_string) is not None:
                program.append(int(sliced_string,2))

        for instruction in program:
            self.ram_write(address, instruction)
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        while not self.halted:
            instruction = self.ram[self.pc]

            if instruction in self.instructions:
                self.instructions[instruction]()
            else:
                print(f"Unknown instruction at index {self.pc}")
                sys.exit(1)