class PigLatinTranslator {
	
	public String translate(String str) {
   		String[] words = str.split(" ");
    	String newStr = "";
    	for (String word: words) {
    		if (newStr != "") newStr += " ";
    		newStr += translateWord(word);
    	}
    	return newStr;
    }

	public String translateWord(String word) {
		// case 1: starting with vowel (char(0)) or with "xr"/"yt"--> append "ay" to the end
		if(word.indexOf("a") == 0 || word.indexOf("e") == 0 || word.indexOf("i") == 0 || word.indexOf("o") == 0 || word.indexOf("u") == 0 || word.indexOf("xr") == 0 || word.indexOf("yt") == 0) {
			return word + "ay";
		}
		// case 2: starting with "sch" or "thr" or "th" or "qu" or "ch" --> take first substring and move it to the end, THEN append "ay"
		else if(word.indexOf("sch") == 0 || word.indexOf("thr") == 0) {
			word = word.substring(3) + word.substring(0, 3) + "ay";
		}
		// case 3: starting with "th" or "qu" or "ch" --> take first substring and move it to the end, THEN append "ay"
		else if(word.indexOf("th") == 0 || word.indexOf("qu") == 0 || word.indexOf("ch") == 0) {
			word = word.substring(2) + word.substring(0, 2) + "ay";
		}
		// case 4: starting with consonant FOLLOWED by "qu" --> take first 3 chars and move it to the end, THEN append "ay"
		else if(word.indexOf("qu") == 1) {
			word = word.substring(3) + word.substring(0, 1) + "quay";
		}
		// case 5: y is 2nd letter while .length()=2 --> switch the 2 letters and append "ay"
		else if(word.length() == 2 && word.indexOf("y") == 1) {
			word = word.substring(1, 2) + word.substring(0, 1) + "ay";
		}
		// case 6: y is 3rd after 2 consonants --> take first 2 chars and move it to the end, THEN append "ay"
		else if(!(word.indexOf("a") == 0 || word.indexOf("e") == 0 || word.indexOf("i") == 0 || word.indexOf("o") == 0 || word.indexOf("u") == 0) &&
				!(word.indexOf("a") == 1 || word.indexOf("e") == 1 || word.indexOf("i") == 1 || word.indexOf("o") == 1 || word.indexOf("u") == 1) &&
				  word.indexOf("y") == 2) {
			word = word.substring(2) + word.substring(0, 2) + "ay";
		}
		// case 7: starting with consonant --> take first char and move it to the end, THEN append "ay"
		else if(word.substring(0, 1) != "a" || word.substring(0, 1) != "e" || word.substring(0, 1) != "i" || word.substring(0, 1) != "o" || word.substring(0, 1) != "u") {
			word = word.substring(1) + word.substring(0, 1) + "ay";
		}
		return word;
	}
}