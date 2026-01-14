import cocotb
import logging

from cocotb.binary import BinaryValue

from cocotb.triggers import Timer

def mux_model(a,b):
    expected_val=(a>>b)&1
    

    return expected_val


@cocotb.test()
async def mux_test(dut):

    for a in range(256):
        for b in range(8):

            dut.din.value = a
            dut.sel.value = b

            await Timer(1,"ns")

            output=dut.dout.value
            assert mux_model(a,b)==output, "Error in calculation"





            
 
