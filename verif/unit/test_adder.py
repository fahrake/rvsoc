import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def random_adds(dut):
    for _ in range(1000):
        a = random.randint(0, 2**32 - 1)
        b = random.randint(0, 2**32 - 1)
        dut.a.value = a
        dut.b.value = b
        await Timer(1, "ns")
        assert int(dut.y.value) == (a + b) & 0xFFFFFFFF, f"{a} + {b} gave {int(dut.y.value)}"
