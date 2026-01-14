import cocotb
from cocotb.triggers import RisingEdge,Timer
from cocotb.clock import Clock
import random

async def reset_stimuli(dut):
    dut.rst.value=1
    await Timer(25,"ns")
    
    dut.rst.value=0
    await RisingEdge(dut.clk)


def tff_model(t,q):
    if t==1:
        expected_value=q^1
    elif t==0:
        expected_value=q

    return expected_value

@cocotb.test()
async def tff_test(dut):
    cocotb.start_soon(Clock(dut.clk,10,"ns").start())
    
    await reset_stimuli(dut)
    
    assert dut.q.value==0, "Reset is working incorrectly"

    
    for i in range(20):
        t=random.randint(0,1)

        dut.t.value=t
        prev_output=dut.q.value

        await RisingEdge(dut.clk)
        await Timer(1,"ns")

        output=dut.q.value

        assert tff_model(t,prev_output)==output, "Tff is sampling incorrectly"



