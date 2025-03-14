public class pila {
    private long[] anreglo;
    private int top;
    private int n;

    public pila(int n) {
        this.n = n;
        this.anreglo = new long[n];
        this.top = -1;
    }

    public void push(long e) {
        if (isFull()) {
            throw new RuntimeException("Pila llena");
        }
        anreglo[++top] = e;
    }

    public long pop() {
        if (isEmpty()) {
            throw new RuntimeException("Pila vacía");
        }
        return anreglo[top--];
    }

    public long peek() {
        if (isEmpty()) {
            throw new RuntimeException("Pila vacía");
        }
        return anreglo[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args) {
        pila pila = new pila(5);

        // Prueba de la pila
        pila.push(10);
        pila.push(20);
        pila.push(30);

        System.out.println("Elemento en la cima: " + pila.peek());

        System.out.println("Elemento eliminado: " + pila.pop());
        System.out.println("Elemento eliminado: " + pila.pop());

        System.out.println("Elemento en la cima después de pop: " + pila.peek());

        pila.push(40);
        pila.push(50);

        System.out.println("La pila está llena? " + pila.isFull());
    }
}