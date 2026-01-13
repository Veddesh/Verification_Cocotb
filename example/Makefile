TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/example.v
TOPLEVEL      := example    # Verilog or SystemVerilog TOP file module name
MODULE        := example  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim

