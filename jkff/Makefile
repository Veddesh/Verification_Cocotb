TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/jkff.v
TOPLEVEL      := jkff    # Verilog or SystemVerilog TOP file module name
MODULE        := jkff_test  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim


