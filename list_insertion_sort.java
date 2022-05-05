import java.util.LinkedList;

public static class Main {
    public static void main(String args[]) {
        LinkedList<Integer> keys = new LinkedList<>();
        keys.add(5);
        keys.add(7);
        keys.add(8);
        keys.add(5);
        keys.add(-6);
        keys.add(0);
        keys.add(-99999);
        System.out.println(keys);
        System.out.println(list_insertion_sort(keys));
    }
    
    public static <T extends Comparable<T>> LinkedList<T> list_insertion_sort(LinkedList<T> keys) {
        LinkedList<T> ordered_list = new LinkedList<>();
        for (T key: keys) {
            int position = 0;
            for (T ordered : ordered_list) {
                if (ordered.compareTo(key) < 0) {
                    position++;
                } else {
                    break;
                }
            }
            ordered_list.add(position, key);
        }
        return ordered_list;
    }
}