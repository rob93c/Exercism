public class Robot {

    private String name;

    public Robot() {
        this.reset();
    }

    public String getName() {
        String name = "";

        for (int i = 1; i <= 2; i++) {
            name += Character.toString((char) randomBetween(65, 90));
        }
        for (int i = 1; i <= 3; i++) {
            name += Character.toString((char) randomBetween(48, 57));
        }
        return name;
    }

    public void reset() {
        this.name = this.getName();
    }

    private int randomBetween (int min, int max) {
        return min + (int)(Math.random() * ((max - min) + 1));
    }

}