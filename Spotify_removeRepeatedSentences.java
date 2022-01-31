import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<String>();
        list.add("hello there");
        list.add("hi there");
        list.add("hello there");
        System.out.println(removeRepeatedSentences(list));
    }
    
    public static ArrayList<String> removeRepeatedSentences(ArrayList<String> list){
        HashSet<String> set = new HashSet<String>();
        set.addAll(list);
        list.clear();
        list.addAll(set);
        return list;
    }
}
