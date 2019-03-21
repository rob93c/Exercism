public class DifferenceOfSquaresCalculator {

    public int computeSquareOfSumTo(int input) {
        int sum = 0;
        int squareOfSum = 0;
        for(int i = 1; i <= input; i++) {
        	sum += i;
        	squareOfSum = sum * sum;
        }
        return squareOfSum;
    }

    public int computeSumOfSquaresTo(int input) {
        int sum = 0;
        for(int i = 1; i <= input; i++) {
        	sum += (i * i);
        }
        return sum;
    }

    public int computeDifferenceOfSquares(int input) {
        return computeSquareOfSumTo(input) - computeSumOfSquaresTo(input);
    }
}