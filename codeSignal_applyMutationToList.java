int[] solution(int n, int[] a) {
    int l = a.length;
    int res[] = new int[l];
    
    for (int i=0; i<l; i++){
        System.out.println("" + i);
        //exclude a[i-1]
        if (i==0){
            res[i] += a[i];
            
            if (i+1 < l)
                res[i] += a[i+1];
        }
        
        //exclude a[i+1]
        else if (i==l-1){
            res[i] = a[i-1] + a[i];
        }
        
        // otherwise, add all three to result
        else{
            if (i-1 >= 0)
                res[i] = a[i-1] + a[i];
            if (i+1 < l)
                res[i] += a[i+1];
        }
    }
    
    return res;
}
