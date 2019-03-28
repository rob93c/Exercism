import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WordCount {
   
    public Map<String, Integer> phrase(String str) {
        
        Map<String, Integer> wordCounts = new HashMap<>();

        str = str.replaceAll(" '|' |'$", " ");

        Matcher matcher = Pattern.compile("['\\w]+").matcher(str);

        while(matcher.find()) {
            String word = matcher.group().toLowerCase();
            wordCounts.put(word, wordCounts.getOrDefault(word, 0) + 1);
        }
        return wordCounts;
    }
}