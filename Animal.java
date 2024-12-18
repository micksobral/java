package encapsulamento;

public class Animal {
	private String nome, tutor, raça,rg, dataDeNasc;
	private int idade;
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	public String getDataDeNasc() {
		return dataDeNasc;
	}
	public void setDataDeNasc(String dataDeNasc) {
		this.dataDeNasc = dataDeNasc;
	}
	public String getRg() {
		return rg;
	}
	public void setRg(String rg) {
		this.rg = rg;
	}
	public String getRaça() {
		return raça;
	}
	public void setRaça(String raça) {
		this.raça = raça;
	}
	public String getTutor() {
		return tutor;
	}
	public void setTutor(String tutor) {
		this.tutor = tutor;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	}

