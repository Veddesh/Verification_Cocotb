import cocotb
import logging
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue



def pri_model(input_bin):
    exp_val='000'
 
    if input_bin.binstr[0] == '1':
        exp_val = '111'  
    elif input_bin.binstr[1] == '1':
        exp_val = '110'
    elif input_bin.binstr[2] == '1':
        exp_val = '101'
    elif input_bin.binstr[3] == '1':
        exp_val = '100'
    elif input_bin.binstr[4] == '1':
        exp_val = '011'
    elif input_bin.binstr[5] == '1':
        exp_val = '010'
    elif input_bin.binstr[6] == '1':
        exp_val = '001'
    elif input_bin.binstr[7] == '1':
        exp_val = '000'
   
    return exp_val

@cocotb.test()
async def priority_encoder_test(dut):
    input_bin=BinaryValue(n_bits=8,bigEndian=False,value=0)

    output_bin=BinaryValue(n_bits=3,bigEndian=False,value=0)
    for a in range(0,256):
        dut.en.value=1
        dut.i.value=a
        input_bin.integer=a
        await Timer(1,units="ns")
        output=dut.y.value
        output_bin.integer=output


        if pri_model(input_bin)==output_bin.binstr:
            print("Test has passed with values input: %0d and output : %0d",a,output)
        else:
             print("Test has failed with values input: %0d and output : %0d, where expected output was %s",a,output,pri_model(input_bin))
