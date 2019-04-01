import java.util.List;

public class BinarySearch {

	private List<Integer> list;

	public BinarySearch(List<Integer> list) {
		this.list = list;
	}

	public int indexOf(int num) throws ValueNotFoundException {
		return indexOf(0, list.size() -1, num);
	}

	public int indexOf(int low, int high, int num) throws ValueNotFoundException {
		int mid = (low + high) / 2;

		if (low > high) {
			throw new ValueNotFoundException("Value not in array");
		} else if (num == list.get(mid)) {
			return mid;
		} else if (num > list.get(mid)) {
			return indexOf(mid + 1, high, num);
		}
		return indexOf(low, mid - 1, num); 
	}
}