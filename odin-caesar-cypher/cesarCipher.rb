

def cesar_cipher(string, n)
  letter = string.chars.map {|c| c.ord}
  shift_letters = letter.map {|c| ((c + n) < 123 ? (c + n) : (c + n) - 26).chr}.join
  puts shift_letters

end

cesar_cipher("string!", 5)
