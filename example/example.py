import cocotb
import logging
from cocotb.binary import BinaryValue

@cocotb.test()
async def printing(dut):
    print("Test started")
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Test started")
    a=BinaryValue(n_bits=8,value=34,bigEndian=False)
    if a[0]==0:
        print("HYess")



