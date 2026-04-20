import json

class ScoreManagement:
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores
    
    def average_score(self):
        return sum(self.scores) / len(self.scores)
    
    def save_to_file(self, filename):
        json_data = {
            "name": self.name,
            "scores": self.scores,
            "average_score": self.average_score()
        }
        json.dump(json_data, open(filename, 'w'), indent=4)
        
    def load_from_file(self, filename):
        json_data = json.load(open(filename, 'r'))
        self.name = json_data["name"]
        self.scores = json_data["scores"]
        self.average_scores = json_data["average_score"]

score_manager = ScoreManagement("Alice", [85, 90, 78])
print(f"Average score for {score_manager.name}: {score_manager.average_score():.2f}")
score_manager.save_to_file("scores.json")
new_score_manager = ScoreManagement("", [])
new_score_manager.load_from_file("scores.json")
print(f"Loaded data for {new_score_manager.name}: Scores: {new_score_manager.scores}, Average Score: {new_score_manager.average_score():.2f}")