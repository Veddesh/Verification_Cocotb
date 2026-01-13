module dff (
    input  wire clk,
    input  wire rst,
    input  wire din,
    output reg dout
);
    always @(posedge clk) begin
    
    if(rst==1'b1)
	    dout<=1'b0;
    else
	    dout<=din;
    
    end

    initial begin
	$dumpfile("dump.vcd");
	$dumpvars(0,dff);
	    end
endmodule

