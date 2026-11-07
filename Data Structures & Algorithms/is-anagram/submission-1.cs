public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char,int> map = new Dictionary<char,int>();

        foreach (char c in s) {
            map[c] = map.GetValueOrDefault(c) + 1;
        }

        foreach (char c in t) {
            map[c] = map.GetValueOrDefault(c) - 1;
        }

        foreach (var kvp in map) {
            if (kvp.Value != 0) return false;
        }

        return true;
    }
}
