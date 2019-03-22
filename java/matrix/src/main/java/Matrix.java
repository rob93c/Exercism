import java.util.*;

public class Matrix {

	private int[][] matrix;

    public Matrix(String matrixAsString) {
        String[] strRows = matrixAsString.split("\n");
        matrix = new int[strRows.length][];
        for(int i = 0; i < strRows.length; i++) {
        	matrix[i] = Arrays.stream(strRows[i].split("\\s")).mapToInt(num -> Integer.parseInt(num)).toArray();
        }
    }

    public int[] getRow(int rowNumber) {
    	return matrix[rowNumber];
    }

    public int[] getColumn(int columnNumber) {
    	int[] array = new int[matrix.length];
    	int i = 0;
    	for(int[] row : matrix) {
    		array[i] = row[columnNumber];
    		i++;
    	}
    	return array;
    }
}
