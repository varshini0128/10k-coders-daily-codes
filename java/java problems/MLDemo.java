import java.lang.*;
class Csea
{
void display()
{
System.out.println("welcome to CSEA");
}
}
class Cseb extends Csea
{
void show()
{
System.out.println("welcome to CSEB");
}
}
class Csec extends Cseb
{
void print ()
{
System.out.println("welcome to CSEC");
}
}
public class MLDemo
{
public static void main(String args[])
{
Csec c = new Csec();
c.display();
c.show();
c.print();
}
}

