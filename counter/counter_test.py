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
        
        if x==15 and counter_model(x)==0:
            logging.info("Overflow has correctly occured after 15 to 0")
        elif counter_model(x)==dut.count.value:
                logging.info("Counter has correctly given output value %d after %d",dut.count.value,x)
        else:
            logging.info("Error in counting after count value %d, the count value got is %d",x,dut.count.value)



