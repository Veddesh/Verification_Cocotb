TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/tff.v
TOPLEVEL      := tff    # Verilog or SystemVerilog TOP file module name
MODULE        := tff_test  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim


