import cocotb

from cocotb.triggers import Timer
import logging
from cocotb.binary import BinaryValue


def demux_model(din,sel):
    

    expected_output=(din<<sel)

    return expected_output


@cocotb.test()
async def demux_test(dut):
    for a in range(0,2):
        for b in range(0,8):
            logging.getLogger().setLevel(logging.INFO)

            dut.din.value=a
            dut.sel.value=b
            
            

            await Timer(1,"ns")

            output=dut.dout.value

            assert output==demux_model(a,b), "Error in computation"



