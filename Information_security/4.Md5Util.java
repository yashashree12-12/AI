import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Md5Util {

    /** Returns the MD5 digest of the given text as a lowercase hex string. */
    public static String md5(String text) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hash = md.digest(text.getBytes(StandardCharsets.UTF_8));
            return toHex(hash);
        } catch (NoSuchAlgorithmException e) {
            // MD5 is always present in the standard JRE; this is unlikely to happen
            throw new RuntimeException("MD5 algorithm not available", e);
        }
    }

    private static String toHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * 2);
        for (byte b : bytes) {
            sb.append(Character.forDigit((b >>> 4) & 0xF, 16));
            sb.append(Character.forDigit(b & 0xF, 16));
        }
        return sb.toString();
    }

    // quick demo
    public static void main(String[] args) {
        String input = (args.length > 0) ? String.join(" ", args) : "Yashashree";
        System.out.println("Input : " + input);
        System.out.println("MD5   : " + md5(input)); // hello -> 5d41402abc4b2a76b9719d911017c592
    }
}
//javac Md5Util.java


