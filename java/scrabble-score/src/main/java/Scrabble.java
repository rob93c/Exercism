class Scrabble {

	private int count = 0;
	private final String word;
   
    public Scrabble(String word) {
        this.word = word.toUpperCase();
    }

    public int getScore() {
        for(int i = 0; i < word.length(); i++) {
        	char letter = word.charAt(i);
        	count = count + getSingleValue(letter);
        }
        return count;
    }

    public int getSingleValue(char letter) {
    	int value = 0;
    	letter = Character.toUpperCase(letter);
    	if(letter == 'A' || letter == 'E' || letter == 'I' || letter == 'O' || letter == 'U' || 
           letter == 'L' || letter == 'N' || letter == 'R' || letter == 'S' || letter == 'T') {
    		value = 1;
    	} else if(letter == 'D' || letter == 'G') {
    		value = 2;
    	} else if(letter == 'B' || letter == 'C' || letter == 'M' || letter == 'P') {
    		value = 3;
    	} else if(letter == 'F' || letter == 'H' || letter == 'V' || letter == 'W' || letter == 'Y') {
    		value = 4;
    	} else if(letter == 'K') {
    		value = 5;
    	} else if(letter == 'J' || letter == 'X') {
    		value = 8;
    	} else if(letter == 'Q' || letter == 'Z') {
    		value = 10;
    	} else value = 0;

    	return value;
    }

}
