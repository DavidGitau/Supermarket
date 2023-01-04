/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javafront;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author LioN
 */
public class JavaFront {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws InterruptedException {
        Loader Ld = new Loader();
        Ld.setVisible(true);
        for (int i=0; i<100; i++){
                Thread.sleep(100);
                Ld.Progress.setValue(i);
                Ld.jLabel2.setText(i+" %");
            // TODO code application logic here
        }
        Ld.dispose();
        
    }
    
}
