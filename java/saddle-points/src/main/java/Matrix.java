import java.util.*;

class Matrix {

    private List<List<Integer>> matrix;

    Matrix(List<List<Integer>> values) {
        matrix = values;
    }

    public Set<MatrixCoordinate> getSaddlePoints() {
        Set<MatrixCoordinate> result = new HashSet<>();
        for (int r = 0; r < matrix.size(); r++) {
            int hi = Collections.max(matrix.get(r));
            for (int c = 0; c < matrix.get(r).size(); c++)
                if (matrix.get(r).get(c) == hi) {
                    int lo = matrix.get(r).get(c);
                    for (List<Integer> aMatrix : matrix)
                        if (aMatrix.get(c) < hi)
                            lo = aMatrix.get(c);
                    if (lo == hi)
                        result.add(new MatrixCoordinate(r, c));
                }
        }
        return result;
    }
}