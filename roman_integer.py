def romanToInt(s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)-1):
            curr_value = roman_map[s[i]]
            next_value = roman_map[s[i+1]]
            if curr_value < next_value :
                total -= curr_value
            else :
                total += curr_value
        last_symbol = s[-1]
        total += roman_map[last_symbol]
        return total

value = romanToInt("LVIII")
print(value)