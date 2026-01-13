module ring_counter(
    input  wire clk,
    input  wire rst,      // synchronous active-high reset
    output reg  [3:0] count
);

    always @(posedge clk) begin
        if (rst)
            count <= 4'b0001;             // IMPORTANT: one-hot init
        else
            count <= { count[0], count[3:1] };    // rotate right
    end

     initial begin
	     $dumpfile("dump.vcd");
     $dumpvars(0,ring_counter);
end

endmodule

