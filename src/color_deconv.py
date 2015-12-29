# color deconv info sourced from:
# - http://www.mecourse.com/landinig/software/cdeconv/cdeconv.html
# - http://web.hku.hk/~ccsigma/color-deconv/color-deconv.html
# double leng, A, V, C, log255=Math.log(255.0);
# int i,j;
# double [] MODx = new double[3];
# double [] MODy = new double[3];
# double [] MODz = new double[3];
# double [] cosx = new double[3];
# double [] cosy = new double[3];
# double [] cosz  = new double[3];
# double [] len = new double[3];
# double [] q = new double[9];
# byte [] rLUT = new byte[256];
# byte [] gLUT = new byte[256];
# byte [] bLUT = new byte[256];

# ==== [Algorithm in Pseudocode] ==================================

# Note: may need to identify the background color first

# set LEN and normalize COS
# zero(COS[i])
# MOD[i] = assign predefined constants
# LEN[i] = normalize MOD[i]
# COS[i] = MOD[i]/len[i], unless LEN[i] == zero

# if COS[1] is [0,0,0] (unspecified)
#   zero COS[1]

# if COS[2] is [0,0,0] (unspecified)
#   foreach a in x,y,z in COS
#     if a[0]^2 + a[0]^2 > 1
#       # this means color has a negative R component
#       a[2] = 0
#     else
#       a[2] = sqrt(1.0 - (a[0]^2 + a[1]^2))

# then, normalize COS[2]
# leng = dist(COS[2])
# COS[2] = COS[2] / leng

# remove zeros (realllyy?)
# COS[i] = 0.001 if COS[i] == 0

# invert matrix
#  .... wow this article is so much simpler than the java code (MATRICES!!)
# - http://web.hku.hk/~ccsigma/color-deconv/color-deconv.html
# M = COS
# D = inv(M)



# apply matrix deconvolution


# ===============================================================

MOD_HNE1 = {
    'x': [],
    'y': [],
    'z': []
}

MOD_HNE2 = {
    'x': [],
    'y': [],
    'z': []
}


# H&E1
# GL Haem matrix
MODx[0]= 0.644211; #0.650;
MODy[0]= 0.716556; #0.704;
MODz[0]= 0.266844; #0.286;

# GL Eos matrix
MODx[1]= 0.092789; #0.072;
MODy[1]= 0.954111; #0.990;
MODz[1]= 0.283111; #0.105;

# Zero matrix
MODx[2]= 0.0;
MODy[2]= 0.0;
MODz[2]= 0.0;

# H&E 2
# GL Haem matrix
MODx[0]= 0.49015734;
MODy[0]= 0.76897085;
MODz[0]= 0.41040173;

# GL Eos matrix
MODx[1]= 0.04615336;
MODy[1]= 0.8420684;
MODz[1]= 0.5373925;

# Zero matrix
MODx[2]= 0.0;
MODy[2]= 0.0;
MODz[2]= 0.0;
