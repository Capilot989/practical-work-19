class MorseMsg:
    """
        A class for handling Morse code messages and extracting vowels/consonants.

        This class provides methods to decode Morse code messages in English or Russian,
        and extract vowels or consonants from the decoded text.

        Attributes:
            MORSE_ENG: Dictionary mapping Morse code to English letters
            MORSE_RU: Dictionary mapping Morse code to Russian letters
            VOWELS: String containing all vowels in both English and Russian
            message: The Morse code message (space-separated Morse symbols)
        """
    MORSE_ENG = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }

    MORSE_RU = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э',
        '..--': 'Ю', '.-.-': 'Я'
    }

    VOWELS = "AEIOUYАЕЁИОУЫЭЮЯ"

    def __init__(self, message: str) -> None:
        """
        Initialize a new MorseMsg instance.

        Args:
            message: Morse code message with space-separated Morse symbols
        """
        self.message = message

    def eng_decode(self) -> str:
        """
        Decode Morse code to English.

        Returns:
            Decoded English string
        """
        letters = self.message.split()
        translated_message = [self.MORSE_ENG[letter] for letter in letters]
        return ''.join(translated_message)

    def ru_decode(self) -> str:
        """
        Decode Morse code to Russian.

        Returns:
            Decoded Russian string
        """
        letters = self.message.split()
        translated_message = [self.MORSE_RU[letter] for letter in letters]
        return ''.join(translated_message)

    def get_vowels(self, lang: str) -> list[str]:
        """
        Extract vowels from the decoded message.

        Args:
            lang: Language for decoding - "eng" for English, any other for Russian

        Returns:
            List of vowel characters from the decoded message
        """
        translated = self.eng_decode() if lang == "eng" \
            else self.ru_decode()
        result = list(filter(lambda x: x in self.VOWELS, translated))
        return result

    def get_consonants(self, lang: str) -> list[str]:
        """
        Extract consonants from the decoded message.

        Args:
            lang: Language for decoding - "eng" for English, any other for Russian

        Returns:
            List of consonant characters from the decoded message
        """
        translated = self.eng_decode() if lang == "eng" \
            else self.ru_decode()
        result = list(filter(lambda x: x not in self.VOWELS, translated))
        return result

    def __str__(self):
        return f'{self.message}'
