

TOPLEVEL_LANG = verilog

VERILOG_SOURCES = ../counter/counter.v
TOPLEVEL = counter
MODULE = counter_test

WAVES=1

include $(shell cocotb-config --makefiles)/Makefile.sim

view:
	gtkwave sim_build/*.fst &


clean::
	@rm -fr __pycache__ *.vcd *.xml *.o counter
