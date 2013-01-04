import java.util.ArrayList;
import java.util.List;

/**
 * Created by IntelliJ IDEA.
 * User: czhu
 * Date: 13-1-4
 * Time: 下午2:47
 * To change this template use File | Settings | File Templates.
 */
public class NumberSpliter {

    public static void main(String args[]){
        String[] str = {"1","2","3","5","6","9"};
        splitArray(str);
    }

    public static List<List<String>> splitArray(String[] str)    {
        List<List<String>> lli = new ArrayList();
        List<String> li = new ArrayList();
        lli.add(li);

        for (int index = 0; index < str.length; index++) {
            li.add(str[index]);
            if(index==0||index!=str.length-1){
                if ((Integer.parseInt(str[index+1]) - Integer.parseInt(str[index])) != 1) {
                    li= new ArrayList();
                    lli.add(li);
                }
            }

        }
        return lli;
    }
}
