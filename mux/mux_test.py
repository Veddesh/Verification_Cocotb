import cocotb
import logging

from cocotb.binary import BinaryValue

from cocotb.triggers import Timer

def mux_model( din_binaryvalue, sel_binaryvalue):
    if  sel_binaryvalue.binstr=="000":
        expected_val=din_binaryvalue.binstr[7]
    elif  sel_binaryvalue.binstr=="001":
        expected_val=din_binaryvalue.binstr[6]
    elif  sel_binaryvalue.binstr=="010":
        expected_val=din_binaryvalue.binstr[5]
    elif  sel_binaryvalue.binstr=="011":
        expected_val=din_binaryvalue.binstr[4]
    elif  sel_binaryvalue.binstr=="100":
        expected_val=din_binaryvalue.binstr[3]
    elif  sel_binaryvalue.binstr=="101":
        expected_val=din_binaryvalue.binstr[2]
    elif  sel_binaryvalue.binstr=="110":
        expected_val=din_binaryvalue.binstr[1]
    elif  sel_binaryvalue.binstr=="111":
        expected_val=din_binaryvalue.binstr[0]

    return expected_val


@cocotb.test()
async def mux_test(dut):

    for a in range(256):
        for b in range(8):

            dut.din.value = a
            dut.sel.value = b

            din_binaryvalue = BinaryValue(n_bits=8,bigEndian=False,value=0)
            sel_binaryvalue = BinaryValue(n_bits=3,bigEndian=False,value=0)
            output_binaryvalue=BinaryValue(n_bits=1,bigEndian=False,value=0)

            din_binaryvalue.integer=a
            sel_binaryvalue.integer=b

            await Timer(1, units="ns")

    
            output=dut.dout.value
            output_binaryvalue.integer=output

            if mux_model(din_binaryvalue, sel_binaryvalue)==output_binaryvalue.binstr:
                pass
            else:
                logging.warning("Test has failed at the input %d %d, expected output %d, got goutput %s",a,b,output,mux_model(din_binaryvalue,sel_binaryvalue))




            
 
