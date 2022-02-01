boolean solution(int[] a) {
    int l = a.length;
    int[] b = new int[l];
    int j = l-1;
    
    for (int i=0; i<l; i++){
        if (i%2==0)
            b[i] = a[i/2];
        else{
            b[i] = a[j];
            j--;
        }
    }
    
    int prev = -100000;
    for (int n : b){
        if (n <= prev){
            System.out.printf("n:%d < prev:%d%n", n, prev);
            return false;
        }
        prev = n;
        System.out.printf("%d, ", n);
    }
    
    return true;
}


// input: a: [1, 4, 5, 6, 3]
// output: false (1, 3, 4, 6, n:5 < prev:6)

// input: a: [-98, -82, -70, -49, 58, 26, -69, -79, -98]
// output: false (-98, n:-98 < prev:-98)

// input: a: [-79, -48, -42, 4, 9, 55, 70, 84, 62, 40, 7, -28, -46, -74]
// output: true (-79, -74, -48, -46, -42, -28, 4, 7, 9, 40, 55, 62, 70, 84)
