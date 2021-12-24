package Demo;

public class Demo {
    public static void main (String []args) {
        Dier d = new Konijn();
    }
}

class Dier {
    int leeftijd = 14;
}

class Konijn extends Dier {
    String vacht =  "wit";
}