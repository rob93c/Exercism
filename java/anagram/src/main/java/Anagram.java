import java.util.*;

public class Anagram {
	String search;

	public Anagram(String word) {
		search = word;
	}

	public List<String> match(List<String> input) {
		List<String> output = new ArrayList<>();
		for(int i = 0; i < input.size(); i++) {
			if(search.length() == input.get(i).length() && !search.equalsIgnoreCase(input.get(i))) {
				char[] word1 = search.toLowerCase().toCharArray();
				char[] word2 = input.get(i).toLowerCase().toCharArray();
				Arrays.sort(word1);
				Arrays.sort(word2);
				if(Arrays.equals(word1, word2)) {
					output.add(input.get(i));
				}
			}
		}
		return output;
	}
}