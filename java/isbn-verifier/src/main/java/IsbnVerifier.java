public class IsbnVerifier {

    public static String undasher(String code) {
    	return code.replaceAll("\\-", "");
    }	

    public static boolean isValid(String stringToVerify) {
    	int sum = 0;
    	int count = 10;
    	String str = undasher(stringToVerify);

    	if(str.length() != 10 || !str.matches("[0-9]{9}(X|[0-9])$")) {
    		return false;
    	} else {
    		for(String ch: str.split("")) {
    			if(ch.equals("X")) {
    				ch = "10";
    			}
    			sum += (Integer.parseInt(ch) * count);
    			count--;
    		}
    		return (sum % 11) == 0;
    	}
    }
    
}
