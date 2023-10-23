package day03;

public class Animal {
	boolean flag_sound = true;
	
	public void bbeonguri() {
		flag_sound = false;
	}
	
	public static void main(String[] args) {
		Animal a = new Animal();
		System.out.println(a.flag_sound);
		a.bbeonguri();
		System.out.println(a.flag_sound);
	}

}
