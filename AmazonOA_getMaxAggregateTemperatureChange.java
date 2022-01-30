class AmazonOA_getMaxAggregateTemperatureChange{

    public static void main(String[] args){ 
        print("expected: 5, actual: " + getMaxAggregateTemperatureChange(new int[]{-1,2,3}));
    }
    
    public static void print(String s)  { System.out.println(s); }

    public static int getMaxAggregateTemperatureChange(int[] tc){
        int l = tc.length;
        int maxAg = 0;
        int pdSum = 0;
        int tcSum = 0;

        // sum whole tc arr and decrement later on
        for (int num : tc) tcSum+=num;

        for (int i=0; i<l; i++){
            pdSum += tc[i];
            int temp = Math.max(pdSum, tcSum);
            maxAg  = Math.max(maxAg, temp);
            tcSum -= tc[i];
        }

        return maxAg;
    }
}

