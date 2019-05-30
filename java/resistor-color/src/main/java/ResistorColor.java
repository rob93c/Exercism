public class ResistorColor {

    private final static String[] listcolors = new String[] {
            "black", 
            "brown", 
            "red", 
            "orange", 
            "yellow", 
            "green", 
            "blue", 
            "violet", 
            "grey", 
            "white"
    };

    private static int res;

    public int colorCode(String color) {
        for(int i = 0; i < listcolors.length; i++) {
            if(color == listcolors[i]) {
                res = i;
            }
        }
        return res;
    }

    public String[] colors() {
        return listcolors;
    }
}
