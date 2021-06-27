import com.example.tutorial.protos.User;
import com.example.tutorial.protos.Users;

import java.io.FileNotFoundException;
import  java.io.*;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        User.Builder chirag = User.newBuilder();
        chirag.setId(1);
        chirag.setName("Ashok");
        chirag.setPassword("123");
        chirag.setContactNumber(8965986598l);

        try {
            FileOutputStream outputFile = new FileOutputStream("output_binary");
            try {
                chirag.build().writeTo(outputFile);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }catch (IOException e){
            System.out.println("Not Working!");
        }

        deserialize("output_binary");
    }

    public static void deserialize(String fileName){
        try {
            FileInputStream inputFile = new FileInputStream(fileName);
            User user = User.parseFrom(inputFile);
            System.out.println(user.toString());
        }catch (IOException e){
            System.out.println("Not Working!");
        }
    }
}