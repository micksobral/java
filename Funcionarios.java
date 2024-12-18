package Heranca;

public class Funcionarios extends Pessoa {

	public Funcionarios(String nome, String cpf, String telefone) {
		super(nome, cpf, telefone);
		
	}
	public void receber() {
		System.out.println("precebeu");
}
	public void dever() {
		System.out.println("devendo");
}
}