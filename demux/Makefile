TOPLEVEL_LANG ?= verilog
SIM           ?= icarus
VERILOG_SOURCES = $(shell pwd)/demux.v
TOPLEVEL      := demux    # Verilog or SystemVerilog TOP file module name
MODULE        := demux_test  # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim
