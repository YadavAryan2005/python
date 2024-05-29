
//  Write an applet application to display smiley face
import java.awt.*;
import java.applet.*;

class demo extends Applet {
    public void paint(Graphics g) {
        g.setColor(Color.black);
        g.fillOval(50, 50, 100, 100);
    }
}
/* <applet code="demo.class" width=500 height=500></applet> */