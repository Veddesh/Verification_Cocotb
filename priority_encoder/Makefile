TOPLEVEL_LANG ?= verilog
SIM ?= icarus
VERILOG_SOURCES = $(shell pwd)/priority_encoder.v
TOPLEVEL := priority_encoder # Verilog or SystemVerilog TOP file module name
MODULE   := priority_encoder_test # Python file name
 
 
include $(shell cocotb-config --makefiles)/Makefile.sim
