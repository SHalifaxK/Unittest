/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javatest;

/**
 *
 * @author kantomaa
 */
public class Person {
    private String fname;
    private String Sname;
    
    public Person(String fname,String Sname){
        this.fname = fname;
        this.Sname = Sname;
    }
    
    public String getName(){
        return fname+", "+Sname;
    }
}
