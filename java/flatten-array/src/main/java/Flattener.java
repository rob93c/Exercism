import java.util.LinkedList;
import java.util.List;

public class Flattener {

	public List<Object> flatten(List sequence) {
		
		List<Object> finalList = new LinkedList<>();
		
		for(Object obj : sequence) {
			if(obj instanceof List) {
				finalList.addAll(flatten((List) obj));
			} else {
				if(obj != null) {
					finalList.add(obj);
				}
			}
		}
		return finalList;
	}
}
