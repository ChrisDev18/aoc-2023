import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part1 {

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
                for (Character c : line.toCharArray()) {
                    if (Character.isDigit(c)) {
                        if (first == 'x')
                            first = c;
                        last = c;
                    }
                }

                if (first == 'x' || last == 'x') {
                    System.out.println("No digits in line");;
                }

                total += Integer.parseInt("" + first + last);

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Sum of calibration values: " + total);
    }

}
