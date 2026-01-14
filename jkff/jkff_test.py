import cocotb
from cocotb.triggers import RisingEdge,Timer
from cocotb.clock import Clock
import random



def jkff_model(j,k,prev_output):

    if j==0 and k==0:
        expected_value=prev_output
    elif j==1 and k==0:
        expected_value=1
    elif j==0 and k==1:
        expected_value=0
    else:
        expected_value=prev_output^1

    return expected_value

async def reset_stimulus(dut):
    dut.rst.value=1
    await Timer(25,"ns")
    dut.rst.value=0
    await RisingEdge(dut.clk)


@cocotb.test()
async def jkff_test(dut):
    cocotb.start_soon(Clock(dut.clk,10,"ns").start())
    await reset_stimulus(dut)
    assert dut.q.value==0, "Reset is working incorrectly"

    for i in range(20):
        j=random.randint(0,1)
        k=random.randint(0,1)

        dut.j.value=j
        dut.k.value=k
        prev_output=dut.q.value

        await RisingEdge(dut.clk)
        await Timer(1,units="ns")

        output=dut.q.value

        assert jkff_model(j,k,prev_output)==output, "Wrong sampling of jkff has occurred"

