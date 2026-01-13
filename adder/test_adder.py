import cocotb
import logging
import random
from cocotb.triggers import Timer
from cocotb.utils import get_sim_time
 
@cocotb.test()
async def test(dut):
      logging.getLogger().setLevel(logging.INFO);
      err = 0
      for i in range(10):
          a = random.randint(0,15)
          b = random.randint(0,15)
          dut.a.value = a;
          dut.b.value = b;
          await Timer(10,units = 'ns')
          sum = dut.sum.value
          
          if(sum == (a + b)):
            logging.info('Test Passed: a:%0d, b:%0d and sum:%0d @ %0s',a,b,sum,str(get_sim_time(units='ns')))
          else:
            logging.error('Test Failed: a:%0d, b:%0d and sum:%0d @ %0s',a,b,sum,str(get_sim_time(units='ns')))
            err = err + 1
          
          
      if(err > 0):
          logging.error('Number of failed test cases : %0d',err)
      else:
          logging.info('All the test cases Passed')  


