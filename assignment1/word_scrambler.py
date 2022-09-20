def main():
    def get_input():
        # takes user input until the user interrupt
        interrupt = False
        data = load_dictionary()
        while not interrupt:
            user_input = input("Please enter word: ")

            if user_input == 'q':
                interrupt = True
                exit()
            else:
                unscrambler(user_input, data)

    def load_dictionary():
        # acts as a file handler that reads and cleans the words in the words file
        with open('words.txt', 'r') as f:
            data = f.readlines()

            for i in range(0, len(data)):
                data[i] = data[i].strip().lower()

            return data

    def unscrambler(user_input, data):
        # function takes in the user input and cleaned word list and does the comparison
        wlen = 6
        words = []

        for word in data:
            # de-duplicates letters in both inputs to ensure all letters used exist in both words
            sword = ''.join(sorted(word))
            suser_input = ''.join(sorted(user_input))
            sorted_set_word = ''.join(sorted(set(word)))
            sorted_set_user_input = ''.join(sorted(set(user_input)))

            if sword == suser_input:
                words.append(word)
            # Checks if there is a word in the original input
            elif str(word) in str(user_input):
                words.append(word)
            # checks to ensure only the same letters are found in both words
            elif sorted_set_word == sorted_set_user_input:
                words.append(word)

        # Sorts words by length
        while wlen != 2:
            print(f'{wlen} letter words')
            for x in set(words):
                if len(x) == wlen:
                    print(x)
            wlen -= 1

    get_input()


if __name__ == '__main__':
    main()
