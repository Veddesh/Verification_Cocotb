TOPLEVEL_LANG = verilog
VERILOG_SOURCES = dff.v
TOPLEVEL = dff
MODULE = dff_test
WAVES=1
include $(shell cocotb-config --makefiles)/Makefile.sim


view:
	gtkwave sim_build/*.fst &


clean::
	@rm -rf sim_build *.vcd *.xml __pycache__

