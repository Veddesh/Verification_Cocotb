module demux(
    input  wire        din,
    input  wire [2:0]  sel,
    output reg  [7:0]  dout
);

always @(*) begin
    dout = 8'b00000000;     // default: all outputs 0
    dout[sel] = din;        // route input to selected output
end

initial begin

        $dumpfile("dump.vcd");
        $dumpvars(0,demux);
end

endmodule

