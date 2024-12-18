package encapsulamento;

public class zoo {
	public static void main(String[] args) {
		Animal a1 = new Animal();
		
		a1.setIdade(5);
		a1.setNome("maya"); 
		a1.setTutor("micka"); 
		a1.setRaça("pastor alemao"); 
		a1.setRg("5844484"); 
		a1.setDataDeNasc("20082024");
		
		System.out.println("idaed do animal:"+ a1.getIdade());
		
		System.out.println("nome:"+ a1.getNome());
		System.out.println("idade:"+ a1.getTutor());
		System.out.println("tutor:"+ a1.getRaça());
		System.out.println("raça:"+ a1.getRg());
		System.out.println("rg:"+ a1.getDataDeNasc());
		;
				}
}
