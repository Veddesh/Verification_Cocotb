import cocotb
from cocotb.triggers import RisingEdge,ClockCycles
from cocotb.clock import Clock



@cocotb.test()
async def reset_test(dut):
    cocotb.start_soon(Clock(dut.clk_i,10,"ns").start())
    await Reset(dut,2)
    assert dut.cnt_o.value==0,"The counter value is not 0 after reset"






@cocotb.test()
async def counter_test(dut):
    cocotb.start_soon(Clock(dut.clk_i,10,"ns").start())
    await Reset(dut,2)
    for i in range(1,16):
        await RisingEdge(dut.clk_i)
        assert dut.cnt_o.value==i,f"Count value not correct at {i}"
    await RisingEdge(dut.clk_i)
    assert dut.cnt_o.value==0,"Value not o after overflow"

async def Reset(dut,Cycles):
    await RisingEdge(dut.clk_i)
    dut.rst_i.value=1
    await ClockCycles(dut.clk_i,Cycles)
    dut.rst_i.value=0
    await RisingEdge(dut.clk_i)
