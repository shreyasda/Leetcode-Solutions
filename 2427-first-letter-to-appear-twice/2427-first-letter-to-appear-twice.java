class Solution {
    public char repeatedCharacter(String s) {
        ArrayList<Character> characters = new ArrayList<>();
        for(char c: s.toCharArray()){
            if(characters.contains(c)){
                return c;
            }
            else{
                characters.add(c);
            }
        }
        return '\0';
    }
}