
TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/mux.v
TOPLEVEL      := mux    # Verilog or SystemVerilog TOP file module name
MODULE        := mux_test  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim

