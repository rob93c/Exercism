class PigLatinTranslator {
	
	public String translate(String str) {
// case 1: starting with vowel (char(0)) or with "xr"/"yt"--> append "ay" to the end
		if(str.indexOf("a") == 0 || str.indexOf("e") == 0 || str.indexOf("i") == 0 || str.indexOf("o") == 0 || str.indexOf("u") == 0 || str.indexOf("xr") == 0 || str.indexOf("yt") == 0) {
			return str + "ay";
		}
// case 2: starting with "sch" or "thr" or "th" or "qu" or "ch" --> take first substring and move it to the end, THEN append "ay"
		else if(str.indexOf("sch") == 0 || str.indexOf("thr") == 0) {
			str = str.substring(3) + str.substring(0, 3) + "ay";
		}
// case 3: starting with "th" or "qu" or "ch" --> take first substring and move it to the end, THEN append "ay"
		else if(str.indexOf("th") == 0 || str.indexOf("qu") == 0 || str.indexOf("ch") == 0) {
			str = str.substring(2) + str.substring(0, 2) + "ay";
		}
// case 4: starting with consonant FOLLOWED by "qu" --> take first 3 chars and move it to the end, THEN append "ay"
		else if(str.indexOf("qu") == 1) {
			str = str.substring(3) + str.substring(0, 1) + "quay";
		}
// case 5: y is 2nd letter while .length()=2 --> switch the 2 letters and append "ay"
		else if(str.length() == 2 && str.indexOf("y") == 1) {
			str = str.substring(1, 2) + str.substring(0, 1) + "ay";
		}
// case 6: y is 3rd after 2 consonants --> take first 2 chars and move it to the end, THEN append "ay"
		else if(!(str.indexOf("a") == 0 || str.indexOf("e") == 0 || str.indexOf("i") == 0 || str.indexOf("o") == 0 || str.indexOf("u") == 0) &&
				!(str.indexOf("a") == 1 || str.indexOf("e") == 1 || str.indexOf("i") == 1 || str.indexOf("o") == 1 || str.indexOf("u") == 1) &&
				  str.indexOf("y") == 2) {
			str = str.substring(2) + str.substring(0, 2) + "ay";
		}
// case 7: starting with consonant --> take first char and move it to the end, THEN append "ay"
		else if(str.substring(0, 1) != "a" || str.substring(0, 1) != "e" || str.substring(0, 1) != "i" || str.substring(0, 1) != "o" || str.substring(0, 1) != "u") {
			str = str.substring(1) + str.substring(0, 1) + "ay";
		}
// case 8: whole phrase
		else if (str.indexOf(" ") > -1) {
			String[] arr = str.split(" ");
			for(int i = 0; i < arr.length; i++) {
				str = translate(arr[i]);
			}
		}
		return str;
	}
}