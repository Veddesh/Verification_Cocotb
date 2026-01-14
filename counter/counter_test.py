import cocotb
from cocotb.triggers import RisingEdge,ClockCycles
import logging
from cocotb.clock import Clock
from cocotb.triggers import Timer






async def reset_stimuli(dut):
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Starting to apply reset stimuli")
    dut.rst.value=1
    await Timer(25,"ns")
    dut.rst.value=0
    await RisingEdge(dut.clk)
    logging.info("Reset done")


def counter_model(count):

    mask=(1<<4)-1

    next_count= (count+1)&(mask)

    return next_count








@cocotb.test()
async def counter_test(dut):
    cocotb.start_soon(Clock(dut.clk,10,"ns").start())
    await reset_stimuli(dut)
    
    if dut.count.value==0:
        logging.info("The reset is working correctly")
    else:
        logging.warning("The reset is not working")
    
    for i in range(20):
        x=dut.count.value

        await RisingEdge(dut.clk)

        output=dut.count.value
        
        assert counter_model(x)==output, "Errror in counting"

