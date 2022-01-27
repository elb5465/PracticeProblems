import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        // reverse string
        String hello = "hello";
        String res = "";
        
        for (int i=0; i<hello.length(); i++){
            res += String.valueOf(hello.charAt(hello.length()-i-1));
        }
        
        System.out.println(res);
        
        // print out count of each letter in the string
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (char c : hello.toCharArray()){
            if (map.containsKey(String.valueOf(c))) {
                // add count 
                map.put(String.valueOf(c), map.get(String.valueOf(c)) + 1);
            }
            else {
                map.put(String.valueOf(c), 1);
            }
        }
        for (HashMap.Entry entry : map.entrySet()){
            System.out.println("" entry.getKey()+ entry.getValue());
        }
    }
}
