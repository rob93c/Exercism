class RaindropConverter {

/*	If the number has 3 as a factor, output ‘Pling’.
	If the number has 5 as a factor, output ‘Plang’.
	If the number has 7 as a factor, output ‘Plong’.
	If the number does not have 3, 5, or 7 as a factor, just pass the number’s digits straight through. */

    private String convert(int number) {
    	String rain = "";
        if(number % 3 == 0) {
        	rain += "Pling";
        } 
        if(number % 5 == 0) {
        	rain += "Plang";
        } 
        if(number % 7 == 0) {
        	rain += "Plong";
        }
        if(rain.isEmpty()) {
        	rain = Integer.toString(number);
        } 
        return rain;
    }
}