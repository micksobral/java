package fundaamentos02;
import java.util.Scanner;
public class exemplo2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int aluno= 0,x=0;
		double nota =0, media= 0, soma = 0;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("quantos alunos na sala:");
		aluno = sc.nextInt();
		
		while (x<aluno) {
			System.out.println("digite sua nota:");
			nota += sc.nextDouble();
			x++;
			
			
		}
		media = soma/aluno;
		System.out.println("a media é:"+media);

	}

}
