import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part2 {

    public static void main(String[] args) {
        final String FILENAME = "src/main/java/calibration.txt";

        int total = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME))) {

            String line;
            // for each line in the calibration document
            while ((line = reader.readLine()) != null) {
                char first = 'x';
                char last = 'x';

                // iterate through each character
                char[] charArray = line.toCharArray();
                for (int i = 0; i < charArray.length; i++) {
                    char c = charArray[i];
                    if (Character.isDigit(c)) {
                        if (first == 'x')
                            first = c;
                        last = c;
                    } else {
                        int val = getNumeral(line.substring(i));
                        if (val != -1) {
                            if (first == 'x')
                                first = Character.forDigit(val, 10);
                            last = Character.forDigit(val, 10);
                        }
                    }
                }

                if (first == 'x' || last == 'x') {
                    System.out.println("No digits in line");
                }

                total += Integer.parseInt("" + first + last);

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Sum of calibration values: " + total);
    }

    private static int getNumeral(String line) {
        String[] numArray = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < numArray.length; i++) {
            String num = numArray[i];

            if (line.length() < num.length())
                continue;

            String substr = line.substring(0, num.length());

            // if the current numeral being checked matches given point of string
            if (substr.equals(num))
                return (i + 1);
        }

        // if no numerals have been detected at the given point in string
        return -1;
    }

}
