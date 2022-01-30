class AmazonOA_findTotalPower{

    public static void main(String[] args){
        print("result: " + findTotalPower(new int[]{2,3,2,1}));
    }

    public static void print(String s)  { System.out.println(s); }

    public static int findTotalPower(int[] p){
        int l = p.length;
        int total=0;
        int i=0, j=-1;
        int min=Integer.MAX_VALUE, sum=0;

        while (i!=l-1){
            if (j==l-1){
                i ++;
                j = i;
                sum = 0;
                min = p[j];
            }
            else{
                j ++;
            }

            min   = Math.min(min, p[j]);
            sum   += p[j];
            total += min * sum;

            // print("min, sum, total");
            // print(""+ min +" * "+ sum +" = "+ sum*min);
        }

        return total;
    }
}

