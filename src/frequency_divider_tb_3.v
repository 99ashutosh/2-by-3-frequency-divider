`timescale 1ns/100ps
module frequencydivider_tb;
reg clk,reset;
reg [3:0] mc;
wire [3:0] pos_count, neg_count;
wire clk_out;
     
frequency_divider t1(clk,reset,(mc-4'b0001),pos_count,neg_count,clk_out);
   initial
   begin
        clk= 1'b0;
        mc=4'b0011;
   end
   always
    #5  clk=~clk; 
    initial
    begin
         reset=1'b1;
         #5 reset=1'b0;
         #200 $finish;
   end
     
   initial
   $monitor("clk=%b,reset=%b,pos_count=%b,neg_count=%b,clk_out=%b",clk,reset,pos_count,neg_count,clk_out);
     
   initial
   begin
      $dumpfile("src/freqdiv.vcd");
      $dumpvars(0,frequencydivider_tb);
   end
endmodule
   
