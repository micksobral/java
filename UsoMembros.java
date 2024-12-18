package membros;

public class UsoMembros {
	public static void main(String[] args) {
		DataNascimento dt = new DataNascimento();
		DataNascimento dt2 = new DataNascimento();
		dt.dia=12;
		dt.mes=02;
		dt.ano=1991;
		System.out.println("a data de nascimento é:" + "é %d &d &d/n",dt.dia,  dt.mes,dt.ano);
	}

}
