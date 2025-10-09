public class JavaStringDemo
{
public static void main(String[] args)
{
String title="Java Tutorials";
String SiteName="www.btechsmartclass.com";
System.out.println("length of title: "+title.length());
System.out.println("char at index 3: "+title.charAt(3));
System.out.println("Index of 'T': "+title.indexOf('T'));
System.out.println("last Index of 'a': " + title.lastIndexOf('a'));
System.out.println("empty: "+title.isEmpty());
System.out.println("ends with '.com': " + SiteName.endsWith(".com"));
System.out.println("equals: " + SiteName.equals(title));
System.out.println("substring: " + SiteName.substring(9, 14));
System.out.println("uppercase: " + SiteName.toUpperCase());
}
}

