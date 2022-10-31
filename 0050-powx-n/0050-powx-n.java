class Solution {
    public double myPow(double x, int n) {
        if(n==0) return 1;
        if(n<0) return 1.0/pow(x,-1L*n);
        return pow(x,n);
    }
    double pow(double x,long n){
        if(n==1) return x;
        double res = pow(x,n/2);
        if(!(n%2)) return res*res;
        return res*res*x;
    }
}
