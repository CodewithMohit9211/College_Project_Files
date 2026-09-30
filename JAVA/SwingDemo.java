import javax.swing.*;
import java.awt.*;

class SwingAllDemo {

    public static void main(String[] args) {

        JFrame f = new JFrame("All Java Swing Components");
        f.setLayout(new FlowLayout());

        // ==============================
        // ButtonDemo.java
        // ==============================
        JButton b = new JButton("Register");
        f.add(b);

        b.addActionListener(e ->
            JOptionPane.showMessageDialog(f, "Registration Successful")
        );


        // ==============================
        // CheckBoxDemo.java
        // ==============================
        JCheckBox c1 = new JCheckBox("Java");
        JCheckBox c2 = new JCheckBox("Python");

        f.add(c1);
        f.add(c2);


        // ==============================
        // ComboBoxDemo.java
        // ==============================
        String[] courses = {"BCA", "BSc IT", "BSc CS"};
        JComboBox<String> course = new JComboBox<>(courses);

        f.add(new JLabel("Course:"));
        f.add(course);


        // ==============================
        // LabelDemo.java
        // ==============================
        JLabel label = new JLabel("Student Name:");
        f.add(label);


        // ==============================
        // ListDemo.java
        // ==============================
        String[] hobbies = {"Reading", "Music", "Sports"};
        JComboBox<String> hobby = new JComboBox<>(hobbies);

        f.add(new JLabel("Hobbies:"));
        f.add(hobby);


        // ==============================
        // PasswordDemo.java
        // ==============================
        JLabel passwordLabel = new JLabel("Password:");
        JPasswordField password = new JPasswordField(15);

        f.add(passwordLabel);
        f.add(password);


        // ==============================
        // RadioButtonDemo.java
        // ==============================
        JLabel genderLabel = new JLabel("Gender:");

        JRadioButton male = new JRadioButton("Male");
        JRadioButton female = new JRadioButton("Female");

        ButtonGroup group = new ButtonGroup();
        group.add(male);
        group.add(female);

        f.add(genderLabel);
        f.add(male);
        f.add(female);


        // ==============================
        // SpinnerDemo.java
        // ==============================
        JLabel ageLabel = new JLabel("Age:");

        JSpinner age = new JSpinner(
            new SpinnerNumberModel(18, 2, 100, 1)
        );

        f.add(ageLabel);
        f.add(age);


        // ==============================
        // TextAreaDemo.java
        // ==============================
        JLabel addressLabel = new JLabel("Address:");
        JTextArea address = new JTextArea(4, 20);

        f.add(addressLabel);
        f.add(address);


        // ==============================
        // TextFieldDemo.java
        // ==============================
        JLabel nameLabel = new JLabel("Name:");
        JTextField textField = new JTextField(15);

        f.add(nameLabel);
        f.add(textField);


        // ==============================
        // Frame Settings
        // ==============================
        f.setSize(500, 500);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
