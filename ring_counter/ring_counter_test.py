import cocotb 
import logging
from cocotb.triggers import RisingEdge,Timer

from cocotb.clock import Clock

async def rst_stimuli(dut):
    dut.rst.value=1
    await Timer(25,units="ns")
    dut.rst.value=0
    await RisingEdge(dut.clk)


def ring_counter_model(count):
    mask=(1<<4)-1
    lsb=(count)&1
    right_shifted=(count>>1)&(mask)

    next_count=((lsb<<3)|(right_shifted))&(mask)
    


    return next_count





@cocotb.test()
async def ring_counter_test(dut):

    cocotb.start_soon(Clock(dut.clk,10,"ns").start())
    logging.getLogger().setLevel(logging.INFO)

    await rst_stimuli(dut)
    if dut.count.value==1:
        logging.info("The reset is working fine")
    else:
        logging.info("The reset has failed")

    for i in range(20):
        prev_output=dut.count.value
        await RisingEdge(dut.clk)

        output=dut.count.value

        if ring_counter_model(prev_output)==output:
            logging.info("The test case has passed correctly by giving count %d after %d",output,prev_output)
        else:
            logging.info("The test case has failed by giving output %d instead of output %d after the count %d",output,ring_counter_model(prev_output),prev_output)
