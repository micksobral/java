package Heranca;

public class Professor extends Pessoa {
	double salario;

	public Professor(String nome, String cpf, String telefone) {
		super(nome, cpf, telefone);	
	}
	public void aplicarProva() {
		System.out.println("professor em diversao");
	
}
	public void cerrtificarAluno() {
		System.out.println("meljor hora");
	}
}