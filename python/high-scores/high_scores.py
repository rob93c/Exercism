class HighScores(object):

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        self.scores.sort(reverse=True)
        return self.scores[0]

    def personal_top_three(self):
        self.scores.sort(reverse=True)
        return self.scores[:3]
