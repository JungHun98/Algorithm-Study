import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    static char[][] board;
    static int R, C;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int answer = 0;
    static boolean[][] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] size = br.readLine().split(" ");
        R = Integer.parseInt(size[0]);
        C = Integer.parseInt(size[1]);

        board = new char[R][C];
        visit = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            board[i] = line.toCharArray();
        }

        Set<Character> tempSet = new HashSet<>();
        dfs(0, 0, tempSet);

        System.out.println(answer);
    }

    static void dfs(int x, int y, Set<Character> alphaSet) {
        alphaSet.add(board[x][y]);

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= R || ny >= C) continue;

            if (!alphaSet.contains(board[nx][ny])) {
                alphaSet.add(board[nx][ny]);
                dfs(nx, ny, alphaSet);
            }
        }

        answer = Math.max(answer, alphaSet.size());

        alphaSet.remove(board[x][y]);
    }
}
