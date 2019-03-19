class PigLatinTranslator {
	
	public String translate(String str) {
   		String[] words = str.split(" ");
    	String newStr = "";
    	for (String word: words) {
    		if (!newStr.equals("")) newStr += " ";
    		newStr += translateWord(word);
    	}
    	return newStr;
    }

	public String translateWord(String word) {
		if(word.indexOf("a") == 0 || word.indexOf("e") == 0 || word.indexOf("i") == 0 || word.indexOf("o") == 0 || word.indexOf("u") == 0 || word.indexOf("xr") == 0 || word.indexOf("yt") == 0) {
			return word + "ay";
		} else if(word.indexOf("sch") == 0 || word.indexOf("thr") == 0) {
			word = word.substring(3) + word.substring(0, 3) + "ay";
		} else if(word.indexOf("th") == 0 || word.indexOf("qu") == 0 || word.indexOf("ch") == 0) {
			word = word.substring(2) + word.substring(0, 2) + "ay";
		} else if(word.indexOf("qu") == 1) {
			word = word.substring(3) + word.substring(0, 1) + "quay";
		} else if(word.length() == 2 && word.indexOf("y") == 1) {
			word = word.substring(1, 2) + word.substring(0, 1) + "ay";
		} else if(!(word.indexOf("a") == 0 || word.indexOf("e") == 0 || word.indexOf("i") == 0 || word.indexOf("o") == 0 || word.indexOf("u") == 0) &&
				  !(word.indexOf("a") == 1 || word.indexOf("e") == 1 || word.indexOf("i") == 1 || word.indexOf("o") == 1 || word.indexOf("u") == 1) &&
				    word.indexOf("y") == 2) {
			word = word.substring(2) + word.substring(0, 2) + "ay";
		} else if(!word.substring(0, 1).equals("a") || !word.substring(0, 1).equals("e") || !word.substring(0, 1).equals("i") || !word.substring(0, 1).equals("o") || !word.substring(0, 1).equals("u")) {
			word = word.substring(1) + word.substring(0, 1) + "ay";
		}
		return word;
	}
}