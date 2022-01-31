import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        System.out.printf("expected: %s, actual: %s%n", "aabbccdd", maxCommonCharacters("aaaaabbbbbcccdd"));
    }
    
    public static String maxCommonCharacters(String s){
        // get counts 
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c : s.toCharArray())
            map.put(c, map.getOrDefault(c, 0) + 1);
        
        // get min
        int min = Integer.MAX_VALUE;
        for (char c : map.keySet())
            min = Math.min(min, map.get(c));
        
        // create new str and return
        String res = "";
        for (char c : map.keySet()){
            res += String.valueOf(c).repeat(min);
        }
        
        return res;
    }
}
