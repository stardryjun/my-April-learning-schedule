public class Person {
    String name;
    int age;
    String sex;

    {
        System.out.println("我是代码块");   //代码块中的内容会在对象创建时仅执行一次
    }

    Person(String name, int age, String sex){
        System.out.println("我被构造了");
        this.name = name;
        this.age = age;
        this.sex = sex;
    }

    public static void main(String[] args) {
        new Person("a",1,"1");
        new Person("b",1,"1");
        new Person("c",1,"1");
    }
}