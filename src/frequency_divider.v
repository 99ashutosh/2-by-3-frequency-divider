module frequency_divider(clk,reset,mc,pos_count,neg_count,clk_out);
input [3:0] mc;  
input clk;
input reset;
output clk_out;
     
output reg [3:0] pos_count, neg_count;
reg c;
wire [1:0] r_nxt;

always @(posedge clk)
if (reset)
    pos_count =0;
else 
    pos_count= pos_count +1;
     
always @(negedge clk)
if (reset)
begin
    neg_count =0; pos_count=0;
end
else  if (neg_count ==(mc) && pos_count ==(mc+1)) 
begin
    neg_count = 0;pos_count=0;
end
else 
    neg_count= neg_count +1;

assign clk_out = (pos_count +neg_count> (mc));
endmodule