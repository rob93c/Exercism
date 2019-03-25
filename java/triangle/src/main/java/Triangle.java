public class Triangle {

    private double side1, side2, side3;

    public Triangle(double side1, double side2, double side3) throws TriangleException {
        if(side1 + side2 <= side3 || side2 + side3 <= side1 || side3 + side1 <= side2) {
            throw new TriangleException();
        }
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public boolean isEquilateral() {
        if(side1 == side2 && side1 == side3) {
            return true;
        } else return false;
    }

    public boolean isIsosceles() {
        if((side1 == side2 && side1 == side3) ||
           (side1 == side2 && side1 != side3) || 
           (side1 == side3 && side1 != side2) || 
           (side2 == side3 && side2 != side1)) {
            return true;
        } else return false;
    }

    public boolean isScalene() {
        if(side1 != side2 && side1 != side3) {
            return true;
        } else return false;
    }

}
