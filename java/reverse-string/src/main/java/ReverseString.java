class ReverseString {

    private String reverse(String inputString) {
    	if(inputString.equals("")) {
    		return inputString;
    	} else if(inputString == null) {
            throw new IllegalArgumentException("The string can't be null.");
    	} else {
    		char[] input  = inputString.toCharArray();
			int start = 0;
			int end = input.length-1;
			char temp;
    		while(end>start) {
    			temp = input[start];
    			input[start] = input[end];
    			input[end] = temp;
    			end--;
    			start++;
    		}
    		return new String(input);
    	}
    }
}