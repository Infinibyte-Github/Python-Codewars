class RomanNumerals:
    @staticmethod
    def to_roman(n : int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numeral = ""
        
        for i in range(len(values)):
            while n >= values[i]:
                n -= values[i]
                roman_numeral += symbols[i]
    
        return roman_numeral

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
        result = 0
        prev_value = 0
        
        for c in roman_num:
            value = roman_to_int_map[c]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value
        
        return result