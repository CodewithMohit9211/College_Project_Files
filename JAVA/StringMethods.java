class StringMethods {
    public static void main(String args[]) {
        String s = "java programming";
        String s1 = "PYTHON";

        System.out.println("Upper Case : " + s.toUpperCase());
        System.out.println("Lowercase : " + s1.toLowerCase());
        System.out.println("Trim : " + s.trim());
        System.out.println("Start With : " + s.startsWith("Sa"));
        System.out.println("Ends with: " + s.endsWith("g"));
        System.out.println("Char at: " + s.charAt(3));
        System.out.println("Length: " + s.length());
        System.out.println("substring: " + s.substring(2, 4));

        String r = s.replace("java", "python");
        System.out.println(r);
        System.out.println("Contains: " + r.contains("java"));

        int index = s.indexOf("a");
        System.out.println("Index OF: " + index);

        int index2 = s.lastIndexOf("g");
        System.out.println("last Index of: " + index2);

        String str1 = "Hello";
        String str2 = "Javatpoint";

        // Concatenating one string
        String str4 = str1.concat("Javatpoint");
        System.out.println(str4);
    }
}