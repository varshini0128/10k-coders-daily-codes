import java.lang.*;
class Student
{
int id;
String name;
public Student(int x,String n)
{
id=x;
name=n;
}
void display()
{
System.out.println("Student id is" + id);
System.out.println("Student name is" + name);
}
}
public class DCDEMO
{
public static void main(String[] args){
Student S=new Student(101,"VARSH");
S.display();
}
}
