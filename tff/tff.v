module tff(
    input  wire clk,
    input  wire rst,
    input  wire t,
    output reg  q
);

always @(posedge clk) begin
    if (rst)
        q <= 1'b0;
    else if (t)
        q <= ~q;
    else
        q <= q;   // optional, can be omitted
end
initial begin

	$dumpfile("dump.vcd");
	$dumpvars(0,tff);
end
endmodule

