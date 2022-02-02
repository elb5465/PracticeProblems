class Solution {
    public int countSubstrings(String s) {
        int l = s.length();
        int win = 0;
        int cnt = 0;
        
        HashSet<Character> set = new HashSet<Character>();
        for (char c : s.toCharArray())
            set.add(c);
    
        if (set.size() == 1) {
            // do addition of all combos
            int sum = 0;
            for (int i=1; i<=l; i++){
                sum += i;
            }
            return sum;
        }
        
        while (win != l){
            for (int i=0; i+win<l; i++){
                if (checkIfPalindrome(s, i, win))
                    cnt ++;
            }
            win ++;
        }
        return cnt;
    }
    
    public boolean checkIfPalindrome(String s, int i, int win){
        // System.out.println(s.substring(i,i+win+1));
        String subStr = s.substring(i,i+win+1);
        int l = subStr.length();
        String rev = "";
        
        for (int n=0; n<l; n++)
            rev += subStr.charAt(l-n-1);
        
        // System.out.println(rev.equals(subStr));
        return rev.equals(subStr);
    }
}

// passes 129/130 test cases except: 
//"dbabcccbcdbbbadabbdabaabcbbabaacdadcdbbbbdddbcbbbcbcabacacdaadaadc
dccbacdaadadcbaacabbddabdadcabbccadacadaaacbbddaaababacaabbbacaccbcbba
bddbbcccaaacbcdcabcbacdbddcdcadaaadcbccbbcabbcbdaadcbddaacacdadacbbdab
cdcdadccaccdbdddddcabdbcdbaadacadadbabdcdbbadaacdbadcdabdbbcabbbdaacaa
aaadcaabaaaadabaaddcaabdddcbcadcbdbbdbcbcdbadcadacbbcdccddaccccacbacaa
cbbdadadcacabdabadbbcdbcaaccdbdcabcadbacbccddbabbdacbcbbcbcabcacdaaccc
aadcdbdccabcaaacaddadcabacdccaaaddaaadbccdbbcccdddababcdbcddcbdddbbbda
adaccbcaabbcbdbadbabbacdbbbdaaccdcabddacadabcccacdabacbcdbcbdabddacacb
dbcaacacaabbaaccddabaadbbaabaddbcacbacdbbbacdccabbcdbbbdbdbbcacabdddbd
baaabbcdcbabcbbbccdcdcdcaaddadccbabbacaddcaddcadcdccaccacabbaababdbbcb
dcdccccccdadbdbdcdbdadcdcacdaabaacabaacdacdbaaccadbcddbdccabbcabcadcbd
adbcdadbbbccacbcbbcaaaabdacbadacaadcadaacdacddcbbabdacacaabccdaccbbcbb
cbcaacdabdcbcdbccdbcbcbddaacdacaaaddcaddcadccacbaddbbbccbbbcbbcbadcabb
ccbbaadaacacabddbdbddcadbdaaccadbcccabdcdbadbbacbcbbcdcabcddcddddabddb
dabdcabdbdbbbcdbcdabbdcb"
