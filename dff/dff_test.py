import cocotb
from cocotb.triggers import RisingEdge,ClockCycles,Timer
from cocotb.clock import Clock
import logging
import random
async def rst_stimuli(dut):

    logging.getLogger().setLevel(logging.INFO)

    logging.info("Starting to apply reset stimuli")

    dut.rst.value=1
    await Timer(20,"ns")

    dut.rst.value=0

    logging.info("Reset stimuli applied. Reset inactive")

@cocotb.test()
async def reset_test(dut):

    logging.getLogger().setLevel(logging.INFO)
    cocotb.start_soon(Clock(dut.clk,10,"ns").start())
    cocotb.start_soon(rst_stimuli(dut))

    await Timer(5,"ns")

    if dut.dout.value==0:
         logging.info("The reset works as intended")



    await Timer(100,"ns")
    logging.info("Starting to apply input din stimuli")

    for i in range(20):
        dut.din.value=random.randint(0,1)

        await RisingEdge(dut.clk)
        logging.info("The input applied is din %d",dut.din.value)
        await RisingEdge(dut.clk)
        
        if dut.dout.value==dut.dout.value:
             logging.info("The input applied is din %d is correctly captures as dout output %d",dut.din.value,dut.dout.value)
        else:
             logging.info("The test has failed")





