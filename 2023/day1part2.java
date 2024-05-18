import java.io.BufferedReader;
import java.io.FileReader;

public class day1part2{
  public static void main(String args[]){
    String text="""
    two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
    """
    String num[]=[one,two,three,four,five,six,seven,eight,nine];
    Map<String,String> numbers= new Hashmap<>();
    numbers.put("one","1");
    numbers.put("two","2");
    numbers.put("three","3");
    numbers.put("four","4");
    numbers.put("five","5");
    numbers.put("six","6");
    numbers.put("seven","7");
    numbers.put("eight","8");
    numbers.put("nine","9");
    try{
        BufferedReader br= new BufferedReader(new FileReader("/workspaces/adventofcode/2023/day1part2.txt"));
        int val=0;
        for(String line : text.split("/n")){//br.lines().toList()){
            for(Map.Entry<String, String> : number.entrySet()){[]
                line.replace(entry.getKey(), entry.getValue());
            
            }
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