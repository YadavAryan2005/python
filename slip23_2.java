import javax.swing.*;

class slip23_2 extends JFrame {
    JMenuBar jb;
    JMenu j1, j2, j3;
    JMenuItem i1, i2, i3, i4, i5;

    slip23_2() {
        setVisible(true);
        jb = new JMenuBar();
        jb.contains(0, 0);
        j1 = new JMenu("File");
        j2 = new JMenu("Edit");
        j3 = new JMenu("Search");
        jb.add(j1);
        jb.add(j2);
        jb.add(j3);
        i1 = new JMenuItem("undo");
        i2 = new JMenuItem("redo");
        i3 = new JMenuItem("cut");
        i4 = new JMenuItem("copy");
        i5 = new JMenuItem("paste");
        j2.add(i1);
        j2.add(i2);
        j2.add(i3);
        j2.add(i4);
        j2.add(i5);
        add(jb);
    }

    public static void main(String[] args) {
        new slip23_2();
    }
}