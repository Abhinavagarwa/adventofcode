import java.io.BufferedReader;
import java.io.FileReader;

public class day1part1{
  public static void main(String args[]){
    String text="""
     1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
    """;
    try{
        BufferedReader br= new BufferedReader(new FileReader("/workspaces/adventofcode/2023/day1part1.txt"));
        int val=0;
        for(String line : br.lines().toList()){
            int first=-1;
            int last=-1;
            for(String c: line.split("")){
                if(Character.isDigit(c.charAt(0))){
                    if(first==-1){
                        first=Integer.parseInt(c);
                    }
                    last=Integer.parseInt(c);
                }    
            }
            first*=10;
            val+=first+last;
        }
         System.out.println((val));
    }
    catch(Exception e){
        e.printStackTrace();
    }
  }
}