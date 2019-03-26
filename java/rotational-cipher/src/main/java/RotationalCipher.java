public class RotationalCipher {

	private int shiftKey;

    public RotationalCipher(int shiftKey) {
        this.shiftKey = shiftKey;
    }

    public String rotate(String data) {
    	char[] c = data.toCharArray();
    	for(int i = 0; i < c.length; i++) {
    		if(Character.isLetter(c[i])) {
    			if(Character.isUpperCase(c[i])) {
    				c[i] = (char)('A' + (c[i] - 'A' + shiftKey) % 26);
    			} else {
    				c[i] = (char)('a' + (c[i] - 'a' + shiftKey) % 26);
    			}
    		}
    	}
    	return new String(c);
    }
}
