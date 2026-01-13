TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/ring_counter.v
TOPLEVEL      := ring_counter  # Verilog or SystemVerilog TOP file module name
MODULE        := ring_counter_test  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim


