module jkff(
    input  wire clk,
    input  wire rst,   // active-HIGH reset
    input  wire j,
    input  wire k,
    output reg  q
);

always @(posedge clk or posedge rst) begin
    if (rst)
        q <= 1'b0;
    else
        q <= (j & ~q) | (~k & q);
end

initial begin
$dumpfile("dump.vcd");
$dumpvars(0,jkff);
end

endmodule

