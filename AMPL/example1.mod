#AMPL model for "Pillow" problem Operations Research

reset;

#OPTIONS -------------------------------------
option solver cplex;
option cplex_options 'sensitivity';



#PARAMETERS AND SETS --------------------------

set I;  # set of items to be made

param fab{I} >=0;    #fabric of item
param sew{I} >=0;    #sew of item
param fill{I} >=0;    #fill of item
param pro{I} >=0;  #profit of item

param fabMax >=0;  #max fabric
param sewMax >=0;  #max sewing
param fillMax >=0;  #max fill


#DECISION VARIABLES ----------------------------
var x{I} >=0;  #number of each item to be pilfered


#OBJECTIVE --------------------------------------
maximize profit: sum{i in I} pro[i]*x[i];


#CONSTRAINTS ------------------------------------
subject to fab_limit: sum{i in I} fab[i]*x[i] <= fabMax;
subject to sew_limit: sum{i in I} sew[i]*x[i] <= sewMax;
subject to fill_limit: sum {i in I} fill[i]*x[i] <= fillMax;


#DATA ------------------------------------------
data example1.dat;

#COMMANDS --------------------------------------
solve;

display x;
display fab_limit, fab_limit.up, fab_limit.slack;
#display volume_limit, volume_limit.up, volume_limit.slack;
#display availability,availability.up,availability.down, availability.slack;


