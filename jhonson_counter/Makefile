TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/jhonson_counter.v
TOPLEVEL      := jhonson_counter    # Verilog or SystemVerilog TOP file module name
MODULE        := jhonson_counter_test  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim


