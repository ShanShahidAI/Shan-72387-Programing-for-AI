import json
from pathlib import Path


class Experiment:
    """Represents an AI experiment with validated accuracy."""
#Shan_72387_PFAI_Week04
    def __init__(self, experiment_id, model_name, dataset_name, accuracy):
        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")

        self.experiment_id = experiment_id
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.accuracy = accuracy
#Shan_72387_PFAI_Week04
    def to_dictionary(self):
        """Convert the experiment object to a JSON-serializable dictionary."""
        return {
            "experiment_id": self.experiment_id,
            "model_name": self.model_name,
            "dataset_name": self.dataset_name,
            "accuracy": self.accuracy,
        }


def main():
    """Create experiments, save them to JSON, and load the best one."""

    base_folder = Path(__file__).resolve().parent
    json_path = base_folder / "data" / "experiments.json"

    json_path.parent.mkdir(parents=True, exist_ok=True)

    experiments = [
        Experiment("EXP-001", "Logistic Regression", "Student Data", 0.84),
        Experiment("EXP-002", "Decision Tree", "Student Data", 0.88),
        Experiment("EXP-003", "K-Nearest Neighbours", "Student Data", 0.91),
    ]
#Shan_72387_PFAI_Week04
    records = [exp.to_dictionary() for exp in experiments]

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
    print("Experiments saved to JSON successfully.")
#Shan_72387_PFAI_Week04
    with json_path.open("r", encoding="utf-8") as file:
        loaded_data = json.load(file)

    loaded_experiments = [
        Experiment(
            item["experiment_id"],
            item["model_name"],
            item["dataset_name"],
            item["accuracy"],
        )
        for item in loaded_data
    ]
#Shan_72387_PFAI_Week04
    best_experiment = max(loaded_experiments, key=lambda exp: exp.accuracy)

    print("\nBest Experiment:")
    print(f"ID: {best_experiment.experiment_id}")
    print(f"Model: {best_experiment.model_name}")
    print(f"Accuracy: {best_experiment.accuracy}")

#Shan_72387_PFAI_Week04
if __name__ == "__main__":
    main()
