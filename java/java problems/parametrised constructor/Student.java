import java.lang.*;
class Student
{
int id;
string name;
Student(int x,string n)
{
id=x;
name=n;
}
void display()
{
System.out.println("student id is"+id);
System.out.println("student name is"+name);
}
}
class DCDEMO
{
public static void main(String[] args)
{
Student S=new Student(101,"ram");
S.display();
}
}
