class IsogramChecker {
    private boolean isIsogram(String phrase) {
    	phrase = phrase.replace("-", "").replace(" ", "").toLowerCase();
		return (phrase.chars().distinct().count() == phrase.length());
    }
}
