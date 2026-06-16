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

        return "Unknown"