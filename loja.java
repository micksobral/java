package javapoo;

public class loja {
	private String modelo;
    private String cor;
    private double preco;

    
    public loja(String modelo, String cor, double preco) {
        this.modelo = modelo;
        this.cor = cor;
        this.preco = preco;
    }

    
    public String Modelo() {
        return modelo;
    }

    public String Cor() {
        return cor;
    }

    public double Preco() {
        return preco;
    }

   
    public void Modelo(String modelo) {
        this.modelo = modelo;
    }

    public void Cor(String cor) {
        this.cor = cor;
    }

    public void Preco(double preco) {
        this.preco = preco;
    }

    
    public void imprimir() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Cor: " + cor);
        System.out.println("Preço: R$ " + preco);
    }

}
