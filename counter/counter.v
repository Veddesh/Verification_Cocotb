module counter #(
    parameter          WIDTH=4
) (
    input              clk,
    input              rst,
    output [WIDTH-1:0] count
);

    reg [WIDTH-1:0] cnt;

    always @(posedge clk) begin
        if (rst == 1'b1)
            cnt<= {WIDTH{1'b0}};
        else
            cnt <= cnt + 1'b1;
    end

    assign count = cnt;


initial begin
$dumpfile("dump.vcd");
$dumpvars(0,counter);
end

 endmodule
