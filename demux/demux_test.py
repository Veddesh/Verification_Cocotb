import cocotb

from cocotb.triggers import Timer
import logging
from cocotb.binary import BinaryValue


def demux_model(din_bv,sel_bv):
    x=sel_bv.integer
    y=-(x-7)
    z=din_bv.binstr

    expected_output="0"*(y) + z + "0"*(x)

    return expected_output


@cocotb.test()
async def demux_test(dut):
    for a in range(0,2):
        for b in range(0,8):
            logging.getLogger().setLevel(logging.INFO)

            dut.din.value=a
            dut.sel.value=b

            din_bv=BinaryValue(n_bits=1,value=a,bigEndian=False)
            sel_bv=BinaryValue(n_bits=3,value=b,bigEndian=False)
            output_bv=BinaryValue(n_bits=8,value=0,bigEndian=False)

            await Timer(1,"ns")

            output=dut.dout.value

            output_bv.integer=output

            if demux_model(din_bv,sel_bv)==output_bv.binstr:
                logging.info("The test has passed for the inputs a and b %d and %d and output got is %s and expected output is %s",a,b,output_bv.binstr,demux_model(din_bv,sel_bv)) 

            else:
                logging.warning("The test case has failed at inputs a and b %d, %d and output got is %s output but expected output was %s",a,b,output_bv.binstr, demux_model(din_bv,sel_bv))




