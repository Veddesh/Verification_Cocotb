// adder.v
module adder (
    input  logic [3:0] a,
    input  logic [3:0] b,
    output logic [4:0] sum,
    input rst);
    
    
    assign sum = a + b;
    
    initial begin
	    $dumpfile("waves.vcd");
	    $dumpvars(0,adder);
    end


endmodule
