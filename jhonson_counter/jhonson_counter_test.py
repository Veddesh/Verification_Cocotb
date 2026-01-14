import cocotb
from cocotb.triggers import RisingEdge,Timer,ClockCycles
import logging

from cocotb.clock import Clock




def jhonson_counter_model(count):
    mask=(1<<4)-1

    x=(count>>1)&mask

    y=(count)&1

    inv_y=y^1

    z=(((inv_y)<<3)|(x))& mask

    return z


async def reset_stimuli(dut):
    logging.getLogger().setLevel(logging.INFO)
    dut.rst.value=1
    await ClockCycles(dut.clk,2,True)
    dut.rst.value=0
    await RisingEdge(dut.clk)


@cocotb.test()
async def jhonson_counter_test(dut):
    logging.getLogger().setLevel(logging.INFO)
    cocotb.start_soon(Clock(dut.clk,10,"ns").start())
    await reset_stimuli(dut)

    if dut.count.value==0:
        
        logging.info("Reset is working correctly")

    else:
        logging.warning("Reset not working correctly")
    await RisingEdge(dut.clk)
    for i in range(20):
        
        prev_output=dut.count.value
        await RisingEdge(dut.clk)
        output=dut.count.value



        assert jhonson_counter_model(prev_output)==output, f"The jhonson counter has failed by giving output {output} after count {prev_output} when expected count was {jhonson_counter_model(prev_output)}"
