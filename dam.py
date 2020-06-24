#maxi. capacity
mc=250e100
#current level
cc=199.5e85
#rain water
ro=25e8
#water collected after rain
mcc=cc+ro-(ro*.25)
#change due to heavy rainfall
dc=mcc+(mcc*.15)
#change due to ground water
a=dc+(dc*.05)
#change due toevaporated water
b=a-(a*.05)
#change dueto irrigation purpose.this is current water levelS
cw=b-(b*.15)
print("current status of dam:",cw,"cu.m")
