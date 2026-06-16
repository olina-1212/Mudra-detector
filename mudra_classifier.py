class MudraClassifier:

    def classify(self, fingers):

        if fingers == [1, 1, 1, 1, 1]:
            return "Pataka"

        elif fingers == [1, 1, 1, 0, 1]:
            return "Tripataka"

        elif fingers == [1, 1, 1, 0, 0]:
            return "Ardhapataka"

        elif fingers == [0, 1, 1, 0, 0]:
            return "Kartarimukha"

         elif fingers == [0, 1, 1, 0, 1]:
            return "Mayura"

         elif fingers == [1, 0, 1, 1, 1]:
            return "Arala"

        elif fingers == [1, 0, 1, 0, 1]:
            return "Sukhatunda"

        elif fingers == [0, 0, 0, 0, 0]:
            return "Sukhatunda"

        return "Unknown"