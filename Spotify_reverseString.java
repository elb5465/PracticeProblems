import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        System.out.println(reverseString("hello"));
    }
    
    public static String reverseString(String s){
        String result = "";
        int l = s.length();
      
        if (l<=1) return s;
        
        for (int i=0; i<l; i++)
            result += s.charAt(l-i-1);
        
        return result;
    }
}
