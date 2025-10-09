import java.lang.*;
class Csea
{
void display()
{
System.out.println("welcome to Csea");
}
}
class Cseb extends Csea
{
void show()
{
System.out.println("welcome to Cseb");
}
}
class csec extends Cseb
{
void print ()
{
System.out.println("welcome to Csec");
}
}
public class MLDemo
{
public static void main(String args[])
{
Cse c = new Csec();
c.display();
c.show();
c.print();
}
}

