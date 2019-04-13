public class DnDCharacter {

    public static final int dice_throws = 4;
    public static final int dice_sides = 6;
    public int strength, dexterity, constitution, intelligence, wisdom, charisma, hitpoints;

    /**
     * DnDCharacter constructor
     * @return [DnDCharacter]
     */
    public DnDCharacter() {
        this.strength =     ability();
        this.dexterity =    ability();
        this.constitution = ability();
        this.intelligence = ability();
        this.wisdom =       ability();
        this.charisma =     ability();
        this.hitpoints = 10 + this.modifier(this.getConstitution());
    }

    public int ability() {
        int dice[] = new int[dice_throws];
        int dice_result = 0;
        int low_result = 0;
        
        for(int i = 0; i < dice_throws; i++) {
            dice[i] = (int)(Math.random() * dice_sides) + 1;
        }
        for (int i = 0; i < dice_throws; i++) {
            if (dice[i] < dice[low_result]) {
                low_result = i;
            }
        }
        for(int i = 0; i < dice_throws; i++) {
            if(i != low_result) {
                dice_result += dice[i];
            }
        }
        return dice_result;
    }

    public int modifier(int input) {
        int modi = input - 10;
        modi = Math.floorDiv(modi, 2);
        return modi;
    }

    public int getStrength() {
        return this.strength;
    }

    public int getDexterity() {
        return this.dexterity;
    }

    public int getConstitution() {
        return this.constitution;
    }

    public int getIntelligence() {
        return this.intelligence;
    }

    public int getWisdom() {
        return this.wisdom;
    }

    public int getCharisma() {
        return this.charisma;
    }

    public int getHitpoints() {
        return this.hitpoints;
    }

}
