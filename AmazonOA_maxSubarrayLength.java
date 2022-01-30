import java.util.ArrayList;
import java.util.List;

// O(n) refined solution
class AmazonOA_maxSubarrayLength{

    public static void main(String[] args){
        print("result: " + maxSubarrayLength(new int[]{-1,1,1,-1,-1,1,1,-1}));
    }

    public static void print(String s)  { System.out.println(s); }

    public static int maxSubarrayLength(int[] b){
        int l = b.length;
        // save cnt and end index of negatives
        int negCnt = 0;
        int firstNeg = -1;
        int lastNeg  = -1;

        // get count of neg nums and store first and last index of negs
        for (int i=0; i<l; i++){
            if ((b[i] == -1)  &&  (firstNeg == -1))
                firstNeg = i;

            if (b[i] == -1){
                lastNeg = i;
                negCnt ++;
            }
        }

        // if count of negatives is even or 0, return whole list bc its product will be 1
        if (negCnt % 2 == 0)
            return l;
        
        // if only one neg number, these will equal, so return whichever side of list is longer
        if (firstNeg == lastNeg){
            ArrayList<Integer> list = new ArrayList<Integer>();
            for (int n : b) list.add(n);

            List<Integer> left  = list.subList(0, firstNeg);
            List<Integer> right = list.subList(firstNeg, l-1);
            return Math.max(left.size(), right.size());
        }

        else{
            // find diff between start of list and firstNeg (-1 for 0 index)
            int firstDiff = l - 1 - firstNeg;
            // find diff between end of list and lastNeg
            int lastDiff  = l - 1 - lastNeg;
            // return length of list minus whichever is smaller or either if equal
            return Math.max(firstDiff, lastDiff);
        }
    }
}

