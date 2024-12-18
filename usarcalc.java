package javapoo;

public class usarcalc {

	public static void main(String[] args) {
		calculadora c1 = new calculadora();
		
		double resp =  c1.somar(4.5, 100.45);
		System.out.println(resp);
		
		calculadora c2 = new calculadora();
		double resp1 = c2.somar(2.3,1,22.3);
		System.out.println(resp1);
		
	}

}
