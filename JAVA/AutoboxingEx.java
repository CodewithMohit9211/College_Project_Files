// Example:
class AutoboxingEx
{
    public static void main(String arg[])
    {
        int a=20;
        Integer n1 = new Integer(a); // autoboxing
        Integer n2 = a;              //autoboxing
        System.out.println("n1 : " +n1);
        System.out.println("n2: " +n2);

        Integer n3 = new Integer(50); //unboxing
        int b = n3;
        System.out.print("b: " +b);
    }
}