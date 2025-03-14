public class Cola {
    
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int size;

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.size = 0;
    }

    public void insert(long e) {
        if (isFull()) {
            throw new RuntimeException("Cola llena");
        }
        fin = (fin + 1) % n;
        arreglo[fin] = e;
        size++;
    }

    public long remove() {
        if (isEmpty()) {
            throw new RuntimeException("Cola vacía");
        }
        long e = arreglo[inicio];
        inicio = (inicio + 1) % n;
        size--;
        return e;
    }

    public long peek() {
        if (isEmpty()) {
            throw new RuntimeException("Cola vacía");
        }
        return arreglo[inicio];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == n;
    }

    public int size() {
        return size;
    }

    public static void main(String[] args) {
        Cola cola = new Cola(5);

        // Prueba de la cola
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);

        System.out.println("Elemento en el frente: " + cola.peek());

        System.out.println("Elemento eliminado: " + cola.remove());
        System.out.println("Elemento eliminado: " + cola.remove());

        System.out.println("Elemento en el frente después de remove: " + cola.peek());

        cola.insert(40);
        cola.insert(50);

        System.out.println("La cola está llena? " + cola.isFull());
    }

}